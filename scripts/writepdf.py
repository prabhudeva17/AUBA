#!/usr/bin/env 	python2
'''
Generate PDF REPORT Script 
'''

from wrcsv import *
from reportlab.pdfgen import canvas

#--pdf filepath--
c=canvas.Canvas("./report.pdf")


csvfiles=[
			"Android_Application_Activity",
			"Youtube_Searched","Youtube_Watched",
			"Installed","Uninstalled",
			"Music_Searched","Music_Listened",
			"Google_Searchs","Google_Visits",
			"Chrome_History",
			"Google_Assistant","Google_Assistant_others",
			"Email",
			"Brief_LocationHistory"
		]

for file in csvfiles:
	
	#---To print data and count to pdf --
	if file != "Brief_LocationHistory":
		data,count = readcsv(file)
		
		if data:

			c.drawString(50,750,"TOP-20 %s"%file)
			c.drawString(100,700,"%s"%file)  
			c.drawString(500,700,"COUNT")

			y=670
			a=0

			while a < len(data):
				c.drawString(100,y,"%s"%data[a])  
				c.drawString(500,y,"%s"%count[a])
				a=a+1
				y=y-20	

			c.showPage()

		else:
			print "!NO DATA To Print in PDF"


	# --Only for Location Data -- 
	if file == "Brief_LocationHistory":
		data1,count1,data2,count2,data3,count3 = toplocations(file)

		if data1:

			c.drawString(50,750,"TOP-20 %s"%file)
			c.drawString(100,700,"%s"%"Country")  
			c.drawString(500,700,"COUNT")

			y=670
			a=0
			while a < len(data1):
				c.drawString(100,y,"%s"%data1[a])  
				c.drawString(500,y,"%s"%count1[a])
				a=a+1
				y=y-20	

			c.showPage()
		
		else:
			print "!NO DATA To Print in PDF"

		if data2:
			c.drawString(50,750,"TOP-20 %s"%file)
			c.drawString(100,700,"%s"%"State")  
			c.drawString(500,700,"COUNT")

			y=670
			a=0
			while a < len(data2):
				c.drawString(100,y,"%s"%data2[a])  
				c.drawString(500,y,"%s"%count2[a])
				a=a+1
				y=y-20	

			c.showPage()
		
		else:
			print "!NO DATA To Print in PDF"	

		if data3:
			c.drawString(50,750,"TOP-20 %s"%file)
			c.drawString(100,700,"%s"%"City")  
			c.drawString(500,700,"COUNT")

			y=670
			a=0
			while a < len(data3):
				c.drawString(100,y,"%s"%data3[a])  
				c.drawString(500,y,"%s"%count3[a])
				a=a+1
				y=y-20	

			c.showPage()
		
		else:
			print "!NO DATA To Print in PDF"

image_path = './heatmap.png'
c.drawImage(image_path,0,400,width=600,height=400)
c.showPage()
c.save()