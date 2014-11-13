import csv
import numpy as np
import matplotlib.pyplot as plot
with open('china_mapdata.csv','rb') as csvfile:
      reader=csv.DictReader(csvfile)
      lat=[row['lat'] for row in reader]
      lat=[[float(lat1)] for lat1 in lat]
with open('china_mapdata.csv','rb') as csvfile1 :
      reader=csv.DictReader(csvfile1)
      lng=[row['long'] for row in reader]
      lng=[[float(lng1)] for lng1 in lng]
plot.figure(figsize=(320,100))
plot.plot(lng,lat,'.',color='black')
plot.savefig('map.png')
#plot.show()
