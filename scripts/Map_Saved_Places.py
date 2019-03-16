#!/usr/bin/env 	python2
'''
Maps 
Maps(your places)/savedplaces.json
'''
from wrcsv import *

#--activity in json format--
b=getjsondata()

place=[]
location=[]

for i in b['features']:                   
	place.append(i['properties']['Title'])

for i in b['features']:                   
	if len(i['properties']['Location'])>2:
		location.append(i['properties']['Location']['Geo Coordinates'])
	else:                                
		location.append(i['properties']['Location'])
		
place_location=zip(place,location)

#--print output to terminal--
print "-"*100+"Saved Places"
for i in place_location:                  
	print"Place: ",i[0]               
	print "Location: ",i[1]
