# Weather_reporter

The project will take latitude, longitude and time period(press enter to use the default that is set to wednesday night) and display the temperature at that time of the day on the world map.
The input will be accepted through command line and the output(temperature) is displayed on the command line and also on world map in a html page.

## Requirments:

Python 3.x is required to run the project. Ensure Python3 is installed on the machine.

os,sys,logging and webbrowser pacakges are included in python standard libraries.
Installation of packages will be taken care in the weather_report.sh shell script.

### Required Packages:

1) requests
2) folium
3) pandas

## How to install and run the project

1) clone the repo to the local machine.
2) Open the terminal and traverse to the project folder location where the weather_report.sh is present.
3) Run the command "chmod u+x weather_report.sh" (will make the file executable for the present user)
4) run the "./weather_report.sh" command on the terminal.
5) enter the latitude(sample input 38.8894 N), longitude(sample input 77.0352 W) and time period value(press enter for default value or type any day) when prompted.
6) The output will be displayed on the terminal and a html page will be opened displaying the location with temperature and forecast.
