import requests
import sys
import pandas as pd
import folium
import webbrowser
import os
import logging

def get_coords(lat,lon):

    la = lat.split(" ")
    lo = lon.split(" ")
    latitude= la[0]
    longitude= lo[0]
        
    if la[1] == 'S':
        latitude = "-"+la[0]
            
    if lo[1] == 'W':
        longitude= "-"+lo[0]
 
    return latitude,longitude
 
def main():
    
    end_point= "https://api.weather.gov/points/"

    logging.basicConfig(filename="logs/logfile.log",format='%(asctime)s %(message)s',filemode='w')
    logger = logging.getLogger()   
    logger.setLevel(logging.DEBUG)
 
    period_name = "Wednesday Night"
    if len(sys.argv[3]) > 0:
        period_name = sys.argv[3]

    # formatting the input coordinates into Decimal degree format
    latitude,longitude = get_coords(sys.argv[1],sys.argv[2]) # SAMPLE 38.8894 N 77.0352 W
    url= end_point + latitude +","+ longitude    
    logger.info("Connecting to "+url)

    try:
        # request made to the endpoint
        response = requests.get(url,timeout=4)
        response.raise_for_status()
        logger.info("Response recieved from "+url)

        # request made to the endpoint in the forecast section
        Forecast_response=requests.get(response.json()["properties"]["forecast"],timeout=4)
        Forecast_response.raise_for_status()
        logger.info("Forecast response recieved")
             
    except requests.exceptions.HTTPError as errh:
        logger.error(errh) 
        print("Following error has occurred\n",errh)
    except requests.exceptions.ConnectionError as errc:
        logger.error(errc) 
        print("Following error has occurred\n",errc)
    except requests.exceptions.Timeout as errt:
        logger.error(errt) 
        print("Following error has occurred\n",errt)
    except requests.exceptions.RequestException as err:
        logger.error(err) 
        print("Following error has occurred\n",err)

    else:

        # data is stored in data frame to display the temperature on map.
        period_df= pd.DataFrame(Forecast_response.json()["properties"]["periods"])
    
        # Creating a map using folium displays temperaturem temperature unit and forecast.
        location_map = folium.Map(location=[latitude,longitude],zoom_start=13,tiles="openstreetmap")
        popup_text = "Temperature : {}<br>Temp_unit : {}<br>Forecast : {}<br>"
        print(period_name)
        #traversing every period object from the response to find the period with mentioned period(default value is Wednesday Night)
        for i, period in period_df.iterrows():
            if period["name"].lower() == period_name.lower():
                popup_text = popup_text.format(period_df.iloc[i][5],
                               period_df.iloc[i][6],
                               period_df.iloc[i][12]
                               )
                folium.Marker(location = [latitude, longitude], popup= popup_text).add_to(location_map)
                location_map.save('map.html')
                webbrowser.open("file:///"+ os.getcwd()+"/"+"map.html")
                logger.info("Map saved and displayed successfully")
                print("Temperature is: ",period["temperature"]," "+period["temperatureUnit"])
                return
        print("Please enter a valid period!!")        
        """
        for period in Forecast_response.json()["properties"]["periods"]:
            if period["name"]== period_name:
                print("Temperature is: ",period["temperature"]," "+period["temperatureUnit"])
                return
        """      
        
if __name__ == '__main__':
    main()


#print(period_df.head(3))
#print(period_df.columns)
#print(os.getcwd()+"/"+"map.html")

#print(response)
#print(response.json())
#df1=pd.DataFrame(response.json()["properties"])
# df=period_df[period_df["name"]==period_name]
# print(df['temperature'].to_string()+df["temperatureUnit"].to_string())
#locations = period_df.groupby('name')
#print(locations.head(3))
#os.getcwd()
#num_of_args = len(sys.argv)
#print("Number of arguments is/are ", num_of_args)
#print(sys.argv[0])