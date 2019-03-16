#!/usr/bin/env	python2
'''
Chrome Browser History
Top Browser History History.json
'''
from wrcsv import *
import time

#--activity in json format--
b=getjsondata()

title, url, epoch_time = [], [], []
for i in  b["Browser History"]:
	title.append(i['title'].encode('utf-8'))
	url.append(i['url'].encode('utf-8')) 
	epoch_time.append(i['time_usec'])

timestamp=[]
for i in epoch_time:
	localtime=time.strftime("%a, %d %b %Y %H:%M:%S %Z", time.localtime(i/1000000))	
	timestamp.append(localtime)

history=zip(title,url,timestamp)

#--write data to csv file--
writecsv("Chrome_History",['Title','URL','Date'],history)

#--read data from csv file--
readcsv("Chrome_History")
#--print output to terminal--	