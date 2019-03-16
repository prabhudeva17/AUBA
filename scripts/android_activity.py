#!/usr/bin/env 	python2
'''
Android Activity
Most Used Android Apps
'''
import re
from wrcsv import *

#--activity in HTML format-- 
a=gethtmldata()

#--Regex Expression--
androidapp=re.findall(r'\">([\w\s]+)</a><br>([\w\s\,\:]+)</div>',a)

#--write data to csv file--
writecsv("Android_Application_Activity",['APPLICATION','DATE'],androidapp)

#--read data from csv file--
readcsv("Android_Application_Activity")
#--print output to terminal--