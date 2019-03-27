#!/usr/bin/env	python2.7
'''
Get Latitude and Longitude and timestamp data
parse to API Get the Full Details and write to CSV file
read the CSV file to Print Top Country 
----------HeatMap----------
plot the most location latitude and longitude in world_map
to Figure out the Trace of the Person 
'''
import requests,ast,math,csv,time
from wrcsv import *
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

#--activity in json format--
b=getjsondata()

def getlatlon():

	'''
	get latitude logitude timestamp data 
	convert timestamp to normal format
	reduce the latitude and logitude data by taking approx of DOT after 2 digit
	'''

	lat, lon, epoch_time = [], [], []
	for i in b['locations']:
		lat.append(i["latitudeE7"]/100000.0)
		lon.append(i["longitudeE7"]/100000.0)
		epoch_time.append(int(i["timestampMs"].encode('utf-8'))/1000)

	timestamp=[]
	for i in epoch_time:
		localtime=time.strftime("%a, %d %b %Y %H:%M:%S %Z", time.localtime(i))	
		timestamp.append(localtime)
		#--not UTC +5:30 for that use gmtime()--

	latlon=zip(lat,lon,timestamp)
	#print latlon

	# -- Reduce the location trace for most visted places which results in overflow of data for api request-- 
	duplicate, uniqlatlon = [], []
	for i in latlon:    
		if math.trunc(i[0]) not in duplicate and math.trunc(i[1]) not in duplicate:
			duplicate.append(math.trunc(i[0]))                                             
			duplicate.append(math.trunc(i[1]))                                                 
			uniqlatlon.append(i)

	return uniqlatlon

uniqlatlon=getlatlon()

def createcsv(file):

	'''
	Get Location details by API Request
	Write the data to CSV file
	'''

	csv_file=file
	file=open(csv_file+".csv","w")
	fieldname=['Country','State','City','Street','Location Name','Date&Time','osm_key','osm_value','Latitude','Longitude']
	csv_writer=csv.DictWriter(file,fieldnames=fieldname)
	csv_writer.writeheader()

	#--try if some lat lon location data is None--
	try: 

		for i in uniqlatlon:                                                       
			#print i     
			latdata=float(i[0])/100
			londata=float(i[1])/100                                                                  
			url="https://photon.komoot.de/reverse?lon=%s&lat=%s"%(londata,latdata)                   
			print url                                           
			response=requests.get(url)                           
			if len(response.content) > 42:                  
				response_dict=ast.literal_eval(response.content)
				print response_dict['features'][0]['properties']['country']

				d1=response_dict['features'][0]['properties']['country']
				d2=None
				d3=None
				d4=None
				d5=None
				d6=None
				d7=None
				#--None if their is data of certain lot lon--

				if 'state'  in response_dict['features'][0]['properties']:
					print response_dict['features'][0]['properties']['state']
					d2=response_dict['features'][0]['properties']['state']

				if 'city'  in response_dict['features'][0]['properties']:
					print response_dict['features'][0]['properties']['city']
					d3=response_dict['features'][0]['properties']['city']

				if 'street'  in response_dict['features'][0]['properties']:	
					print response_dict['features'][0]['properties']['street']
					d4=response_dict['features'][0]['properties']['street']

				if 'name'  in response_dict['features'][0]['properties']:
					print response_dict['features'][0]['properties']['name']
					d5=response_dict['features'][0]['properties']['name']

				if 'osm_key'  in response_dict['features'][0]['properties']:
					print response_dict['features'][0]['properties']['osm_key']
					d6=response_dict['features'][0]['properties']['osm_key']

				if 'osm_value'  in response_dict['features'][0]['properties']:
					print response_dict['features'][0]['properties']['osm_value']
					d7=response_dict['features'][0]['properties']['osm_value']

				csv_writer.writerow({'Country':d1,'State':d2,'City':d3,'Street':d4,'Location Name':d5,'Date&Time':i[2],'osm_key':d6,'osm_value':d7,'Latitude':latdata,'Longitude':londata})
	except:          
		print "error"

	file.close()


def heatmap(file):

	'''
	 Get data from CSV File such as latitude and logitude and country 
	 plot the data in worls map which a trace of location foms a HEATMAP
	'''

	f=open(file+".csv","r")
	reader = csv.reader(f)
	next(reader)
	lats, lons, country = [], [], []
	for row in reader:
	    lats.append(float(row[8]))
	    lons.append(float(row[9]))
	    country.append(row[0])
	f.close()

	uniq_country=[]
	for i in country:
	    if i not in uniq_country:
	        uniq_country.append(i)

	# --Map the data into world map to get Trace of location --
	map = Basemap(projection='cyl')
	plt.title("TraceMap")
	map.drawcoastlines()
	map.drawmapboundary(fill_color="#7777ff")
	map.fillcontinents(color="#ddaa66",lake_color="#7777ff")

	map.drawmeridians(np.arange(0, 360, 30))
	map.drawparallels(np.arange(-90, 90, 30))

	x, y = map(lons, lats)
	map.plot(x, y, 'ro', markersize=3)
	x,y=map(-170,-82)

	#--country label at bottom--
	plt.text(x,y,uniq_country,fontsize=6,fontweight='bold')
	plt.savefig('heatmap.png',dpi=1000,bbox_inches='tight')

	#--plt.show to show the map at run time--
	#plt.show()


file="./CSV/Brief_LocationHistory"

#--create CSV file with Detailed location--
createcsv(file)

#--create HEATMAP to Visulize the trace--
heatmap(file)