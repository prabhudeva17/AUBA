#!/usr/bin/env	python2
'''
Maps
Maps/My Labeled Places/Labeled places.json
'''
from wrcsv import *

#--activity in json format--
b=getjsondata()

print "-"*100+"Labeled Places"

name=[]
address=[]
latlon=[]
for i in b['features']:
	name.append(i['properties']['name'])
	address.append(i['properties']['address'])
	latlon.append(i['geometry']['coordinates'])

nameaddrlatlon=zip(name,address,latlon)

#--print output to terminal--
for i in nameaddrlatlon:
	print "Place: ",i[0]
	print "Address: ",i[1]
	print "Location: ",i[2]

