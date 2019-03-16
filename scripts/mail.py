#!/usr/bin/env	python2
'''
Extract email-ID using regex and validate it 
write to CSV file then count top20
'''
import re
from wrcsv import *

#--activity in mbox format--- 
#--but module call functionname is only gethtmldata--
a=gethtmldata()

#--Regex Expression--
username_email=re.findall(r'From: ([\w\s\"]+)<([\w\-\.\@\_]+)>',a)

# --Write Email-ID and Username to CSV file--
file=open("./CSV/Email.csv","w")
fieldname=['Email-ID','USERNAME']
csv_writer=csv.DictWriter(file,fieldnames=fieldname)
csv_writer.writeheader()

for i in username_email:
	csv_writer.writerow({'Email-ID':i[1],'USERNAME':i[0]})