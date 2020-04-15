#!/usr/bin/env python
# coding: utf-8

# In[1]:


#This file takes the dataframe, and uses the Google Maps API called Geocode to find latitude and longitude based on Written Adresses
import csv
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from collections import Counter
import googlemaps

#reads the original csv file
df=pd.read_csv('TestingCentres.csv', sep=';')
gmaps_key=googlemaps.Client(key='<Google Maps API KEY>')



# In[2]:


#Create address for area
df["Simple Address"]=df["Area"]+ ", "+df["City"]+", " +df["Province"]


# In[3]:


#Get Google Maps Information from address
df["Google Maps Info"]=df["Simple Address"].apply(gmaps_key.geocode)
lat=[]
long=[]

#Extract latitude and longitude from map location
for i in range(len(df)):    
   lat.append((df.iloc[i,5])[0]["geometry"]["location"]["lat"])
   long.append((df.iloc[i,5])[0]["geometry"]["location"]["lng"]) 

#Add lat and long to datframe
df["Latitude"]=lat
df["Longitude"]=long

#Create csv that includes Google Maps Info + Lat/Long
df.to_csv('testingCentres_ginfo.csv', index=False, header=True)

#Create csv that only includes Lat/Long
df=df.drop(columns="Google Maps Info")
df.to_csv('testingCentres_latlong.csv', index=False, header=True)

