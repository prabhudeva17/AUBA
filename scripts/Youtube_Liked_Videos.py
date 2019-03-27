#!/usr/bin/env	python2.7
'''
Youtube 
Liked Videos and its Descriptions 
YouTube/playlist/likes.json
'''
from wrcsv import *

#--activity in json format--
b=getjsondata()

title=[]
description=[]

for i in b:
	title.append(i['snippet']['title'])
	description.append(i['snippet']['description'])

video=zip(title,description)

#--print output to terminal--
for i in video[:20]:
	print "Title:",i[0]
	print "Description: ",i[1]
	print "-"*100