#!/usr/bin/env	python2.7
# -*- coding: utf-8 -*-
'''
Youtube Activity
Watched,channel,time and Searched,time write to csv
'''
import re
from wrcsv import *

#--activity in HTML format--
a=gethtmldata()

#--Regex Expression--
searched=re.findall(r'href="https://www.youtube.com/results\?search_query=[\w\s\_\-\+\|\!\#\&\(\)\;\:\,\.]+">([\w\s\(\)\!\;\,\:\#\&\|\-]+)</a><br>([\w\s\,\:]+)</div>',a)
watched=re.findall(r'href="https://www.youtube.com/watch\?v=[\w\s\_\-\+\|\!\#\&\(\)\;\:\,\.]+">([\w\s\_\-\+\|\!\#\&\(\)\;\:\,\.]+)</a><br><a href="https://www.youtube.com/channel/[\w\s\_\-\+\|\!\#\&\(\)\;\:\,\.]+">([\w\s]+)</a><br>([\w\s\,\:]+)</div>',a)

#--write data to csv file-- 
writecsv("Youtube_Searched",['Video','Date'],searched)
writecsv("Youtube_Watched",['Video','Channel','Date'],watched)

#--read data from csv file--
readcsv("Youtube_Searched")
readcsv("Youtube_Watched")
#--print output to terminal--