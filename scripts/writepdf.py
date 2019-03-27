#!/usr/bin/env 	python2.7
'''
Generate PDF REPORT Script
'''

import csv
from wrcsv import *
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import HexColor
from reportlab.lib.units import mm

width, height = letter

#--pdf filepath--
c=canvas.Canvas("./report.pdf")

def coverpage():

	x, y = letter
	c.drawImage("./scripts/jpg/coverpage.jpg",0,0,width=x,height=y+50)
	c.showPage()


def androiddeviceconfig():

	data=readcsv0("Android_Device_Config")

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

	c.drawImage("./scripts/jpg/auba_logo.jpeg",10,10,width=30,height=10)
	c.showPage()

csvfiles=[
			"Android_Application_Activity",
			"Youtube_Searched",
			"Youtube_Watched",
			"Installed_Application",
			"Uninstalled_Application",
			"Music_Searched",
			"Music_Listened",
			"Google_Searchs",
			"Google_Visits",
			"Chrome_History",
			"Google_Assistant",
			"Google_Assistant_others",
			"Email",
			"Brief_LocationHistory"
		]

icon_img=[
			"./scripts/jpg/androidapp_activity.jpg",
			"./scripts/jpg/youtube_searched.jpg",
			"./scripts/jpg/youtube_watched.jpg",
			"./scripts/jpg/installed.jpg",
			"./scripts/jpg/uninsalled.jpg",
			"./scripts/jpg/playmusic_searched.jpg",
			"./scripts/jpg/playmusic_listened.jpg",
			"./scripts/jpg/google_search.jpg",
			"./scripts/jpg/google_visit.jpg",
			"./scripts/jpg/chrome_history.jpg",
			"./scripts/jpg/google_assistant.jpg",
			"./scripts/jpg/other_assistant.jpg",
			"./scripts/jpg/email.jpg",
			"./scripts/jpg/location.jpg"
		]

csvfileandiconimg=zip(csvfiles,icon_img)

def writepage(subhead):

	#--Draw straightline--
	c.setLineWidth(.3)
	c.line(30,710,580,710)

	#--Add Icon Img--
	c.drawImage(file[1],80,720,width=60,height=60)

	#--TOP-20 Heading--
	c.setFillColor(HexColor('#4285F4'))	#ocean blue
	c.setFont('Helvetica', 20)
	if file[0] != "Brief_LocationHistory":
		c.drawString(170,750,"TOP-20 %s"%file[0])
	else:
		c.drawString(170,750,"TOP %s"%file[0])

	#--subHeading and count--
	c.setFillColor(HexColor('#F65314'))	#red orange
	c.setFont('Helvetica', 15)
	c.drawString(80,680,"%s"%subhead)
	c.drawString(500,680,"COUNT")

	#--data and count--
	y=650
	a=0
	while a < len(data) and data[a] != subhead:
		if len(data[a])>1:
			c.setFont('Helvetica', 12)
			c.setFillColor(HexColor('#7B0099'))	#Voilet
			if len(data[a]) < 65:
				c.drawString(100,y,"%s"%data[a])
			else:
				c.drawString(100,y,"%s"%data[a][:65])

			c.setFillColor(HexColor('#E50914'))	#Red
			c.drawString(510,y,"%s"%count[a])
		a=a+1
		y=y-25

	c.drawImage("./scripts/jpg/auba_logo.jpeg",10,10,width=30,height=10)

	c.showPage()

#--write data to pdf file--

#insert cover page
coverpage()

#first write android device config
androiddeviceconfig()

#write all data to pdf
for file in csvfileandiconimg:

	#--loop each and every file and icon image one by one--
	#---To print data and count to pdf --

	if file[0] != "Brief_LocationHistory":
		data,count = readcsv(file[0])
		if data:
			writepage(file[0])
		else:
			print "!NO DATA To Print in PDF"

	#--for Brief_LocationHistory--
	else:

		data,count = toplocations(file[0],"Country")
		if data:
			writepage("Country")
		else:
			print "!NO DATA To Print in PDF"

		data,count = toplocations(file[0],"State")
		if data:
			writepage("State")
		else:
			print "!NO DATA To Print in PDF"

		data,count = toplocations(file[0],"City")
		if data:
			writepage("City")
		else:
			print "!NO DATA To Print in PDF"

#--Draw HeatMap--
image_path = './heatmap.png'
c.drawImage(image_path,0,400,width=600,height=400)
c.drawImage("./scripts/jpg/auba_logo.jpeg",10,10,width=30,height=10)
c.showPage()

#--Done Save the PDF--
c.save()
