#!/usr/bin/env	python2
# -*- coding: utf-8 -*-
'''
GooglePlayMusic 
Listened Musics,Artists,time and Searched Music,time write to csv file
Top Musics Listened and searched
'''
import re
from wrcsv import *

#--activity in HTML format--
a=gethtmldata()

#--Regex Expression--
listened=re.findall(r'>Listened to ([\w\s\_\-\+\|\!\#\&\(\)\;\:\,\.]+?)<br>([\w\s\_\-\+\|\!\#\(\)\:\,\.]+)<br>([\w\s\,\:]+)</div>',a)
searched=re.findall(r'href="https://play.google.com/music/search/[\w\+]+">([\w\s\_\-\+\|\!\#\&\(\)\;\:\,\.]+)</a><br>([\w\s\,\:]+)</div>',a)

#--write data to csv file--
writecsv("Music_Searched",['Song','Date'],searched)
writecsv("Music_Listened",['Song','Artists','Date'],listened)

#--read data from csv file--
readcsv("Music_Searched")
readcsv("Music_Listened")
#--print output to terminal--