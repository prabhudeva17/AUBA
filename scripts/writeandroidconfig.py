#!/usr/bin/env	python2.7

import csv
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import HexColor

width, height = letter

#--get data from CSV file---
data=readcsv0("Android_Device_Config")
'''
file=open("../CSV/Android_Device_Config.csv","r")
csv_reader=csv.reader(file,delimiter=',')
data=[]
for row in csv_reader:
	data.append(row[0])
'''
#--pdf filepath--
c=canvas.Canvas("./android_device_config.pdf")
img_path="./scripts/jpg/android_device_config.jpg"

heading=[
		'TYPE','MODEL','BRAND','Manufacturer','Hardware','TimeZone','Language',
		'Android_ID','IMEI Number','Serial Number','Firmware','Security Patch Date',
		'Service Provider','Roaming Status','Network Role'
		]

#--draw straightline--
c.setLineWidth(.3)
c.line(30,710,580,710)

#--Draw ICON----
c.drawImage(img_path,80,720,width=60,height=60)

#--Heading---
c.setFillColor(HexColor('#4285F4'))
c.setFont('Helvetica', 20)
c.drawString(170,750,"ANDROID DEVICE CONFIGURATION")

y=660
a=0
while a<len(heading):
	c.setFillColor(HexColor('#F65314'))
	c.setFont('Helvetica', 15)
	c.drawString(100,y,heading[a])
	c.drawString(270,y,":")
	c.setFillColor(HexColor('#7B0099'))
	c.drawString(290,y,data[a])
	a=a+1
	y=y-35

c.showPage()
c.save()
