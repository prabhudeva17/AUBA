#!/usr/bin/env	python2
'''
Extract email-ID using regex and validate it 
write to CSV file then count top20
'''
import re
import sys
from validate_email import validate_email
import csv
from collections import Counter

# --get mail data--
rawfile=open(sys.argv[1],"r")
a=rawfile.read()
rawfile.close()
#print a

# --Extract mail using Regex---
def extract():
						#UserID@Domain
	match=re.findall(r'[\w\.\-\_\,]+@[\w\.\-\_]+',a)
	return match

emailids=extract()

# --Validate the mail for More appropriate results--
valid_email=[]
def validating_email():

	for emailid in emailids:
		is_valid = validate_email(emailid)
		if is_valid:
			valid_email.append(emailid)

validating_email()

# --Top 20 Count of Email--
topemailid=Counter(valid_email)
for top in topemailid.most_common()[:20]:
	print top


# --Write Email and its Count to CSV file--
file=open("./CSV/Email.csv","w")
fieldname=['Email','Count']
csv_writer=csv.DictWriter(file,fieldnames=fieldname)
csv_writer.writeheader()

for top in topemailid.most_common():
	csv_writer.writerow({'Email':top[0],'Count':top[1]})

del valid_email
del topemailid
