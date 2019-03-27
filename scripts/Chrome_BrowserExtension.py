#!/usr/bin/env	python2.7
'''
Chrome Acivity Extensions Used
Extension.json
'''
from wrcsv import *

#--activity in json format--
b=getjsondata()

extension=[]
for i in b['Extensions']:
	extension.append(i['name'])

#--print output to terminal--
for i in extension:
	print i
