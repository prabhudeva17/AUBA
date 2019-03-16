#!/usr/bin/env	python2
# -*- coding: iso-8859-15 -*-
'''
Search Activity
top google search engine searches
and visited by google search engine
'''
import re
from wrcsv import *

#--activity in HTML format-- 
a=gethtmldata()

#--Regex Expression--
searched=re.findall(r'href="https://www.google.com/search\?q=[\w\+\&\;\=\.\:\/\_\-\%]+">([\w\s\-\,\;\|\.\:]+)</a><br>([\w\s\,\:]+)</div>',a)
visited=re.findall(r'href="https://www.google.com/url\?q=[\w\d\:\/\.\&\;\=\_\-\%]+">([\w\s\:\,\-\.\|\;]+)</a><br>([\w\s\,\:]+)</div>',a)

#--write data to csv file-
writecsv("Google_Searchs",['Search','Time'],searched)
writecsv("Google_Visits",['Visit','Time'],visited)

#--read data from csv file--
readcsv("Google_Searchs")
readcsv("Google_Visits")
#--print output to terminal--