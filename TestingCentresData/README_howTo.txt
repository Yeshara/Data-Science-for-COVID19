README
The purpose of these scripts is to take in addresses, output the latitude and longitude and plot the coordinates on a map.
This was done using Python and the Google Maps API called Geocode.

To run these scripts you will need the following libraries:
Python:
-geopandas
-pandas
-matplotlib
-descartes
-shapely(if not installed with geopandas)
-numpy

Google:
-googlemaps
-You will also need an API key which you can get from signing up to The Google Maps API platform.

Jupyter Notebooks (.ipynb) and Python scripts (.py) are included, whichever is more suitable.
Running the Scripts:
1.Start by Running the TestingCentresGeocode file, this will output two csvs, one called testingCentres_ginfo,
which contains all the Google Maps information(if other info is needed it can then be extracted) and the latitude and
longitude of the testing centres. The other file is called testingCentres_latlong, this file does not contain all the 
Google Maps information but it does have the latitude and longitude. This file will be used in the next step.
2.Run the GeoMappingTestingCentres file, this takes lat/long and plots it on a map. The output of this is an image
file with the plotted Geolocation.Marker sizes and colours can be changed. 

Note:
-A .shp file(South_Africa_Polygon) is used for the map outline, different maps(in .shp format) can be found and
used for the plotting.