#!/usr/bin/env 	python2.7
# -*- coding: utf-8 -*-
'''
GooglePlaystore
Installed, Uninstalled, AllApplication and its time write to csv file
Top Count
'''
import re
from wrcsv import *

#--activity in HTML format--
a=gethtmldata()

#--Regex Expression--
allapplication=re.findall(r'<a.*?>([\w\s\:\;\&]+)</a><br>([\w\s\,\:]+)</div>',a)
installed=re.findall(r'Installed\xc2\xa0<a.*?>([\w\s\:\;\&]+)</a><br>([\w\s\,\:]+)</div>',a)
uninstalled=re.findall(r'Uninstalled\xc2\xa0<a.*?>([\w\s\:\;\&]+)</a><br>([\w\s\,\:]+)</div>',a)

#--write data to csv file--
writecsv("Installed_Application",['Installed','Date'],installed)
writecsv("Uninstalled_Application",['Uninstalled','Date'],uninstalled)
writecsv("AllApplication",['AllApplication','Date'],allapplication)

#--read data from csv file--
readcsv("Installed_Application")
readcsv("Uninstalled_Application")
readcsv("AllApplication")
#--print output to terminal--
