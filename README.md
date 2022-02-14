# Weather_reporter

The project will take latitude, longitude and time period(press enter to use the default that is set to wednesday night) and disply the temperature at that time of the day on the world map.
The input will be accepted through command line and the output(temperature) also displayed on the command line and on world map on html page.

## Requirments:

Python 3.x is required to run the project. Ensure if the python3 is installed on the machine.

os,sys and webbrowser are python standard libraries.

### Required Packages:

1) requests
2) folium
3) pandas
4) logging

## How to install and run the project

1) clone the repo.
2) Open the terminal and traverse to the project folder location.
3) Run the command chmod u+x weather_report.sh(will make the file executable for the present user)
4) run the ./weather_report.sh command on the terminal.
5) enter the latitude, longitude and time period value when prompted.
6) The output will be displyed on the terminal and a html page will be opened displaying the location with temperature and forecast.



on executing every time the logs will be rewritten to the logfile under logs folder that can be used for debugging purposes.
