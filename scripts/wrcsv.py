#!/usr/bin/env 	python2.7
'''
custom module script function which is used mostly in the scripts
'''
#regexmatch for common_special_symbols=\w\s\_\-\+\|\!\#\&\(\)\;\:\,\.

from collections import Counter
import csv
import os
import sys
import json


#--get CSV folder path for csv files to store
path=os.path.abspath('./CSV')

#--parser for html data--
def gethtmldata():

	rawfile=open(sys.argv[1],"r")
	a=rawfile.read()
	rawfile.close()
	return a

#--parser for json data--
def getjsondata():

	rawfile=open(sys.argv[1],"r")
	a=rawfile.read()
	rawfile.close()
	b=json.loads(a)
	return b

#for android device config
def writecsv0(filename,varible):

	file=open(path+"/"+filename+".csv","w")
	csv_writer=csv.writer(file,delimiter=',')
	for i in varible:
		csv_writer.writerow([i])

#for android device config
def readcsv0(filename):

	filepath=path+"/"+filename+".csv"
	if os.path.exists(filepath):

		#--GETDATA to LIST--
		file=open(filepath,"r")
		csv_reader=csv.reader(file,delimiter=',')
		items=[]
		for i in csv_reader:
			items.append(i[0])
		file.close()

	return items

#--writecsv function to write all data to CSV--
def writecsv(filename,fieldname,variable):

	file=open(path+"/"+filename+".csv","w")
	csv_writer=csv.writer(file,delimiter=',')
	csv_writer.writerow(fieldname)

	for i in variable:
		csv_writer.writerow(i)

#--readcsv to count top-20 from csv and parse to writepdf module--
def readcsv(filename):

	data, count = [], []
	print "-"*100+filename
	filepath=path+"/"+filename+".csv"
	if os.path.exists(filepath):

		#--GETDATA to LIST--
		file=open(filepath,"r")
		csv_reader=csv.reader(file,delimiter=',')
		items=[]
		for i in csv_reader:
			items.append(i[0])
		file.close()

		#--COUNT TOP-20--
		topitems=Counter(items)
		del items

		#--if data file present but no regex match or no activity init--
		if len(topitems) > 1:
			for i in topitems.most_common()[:20]:
				print i
				data.append(i[0])
				count.append(i[1])

		else:
			print "!!No Activity FOUND!!"
			return None,None

	else:
		print "!NO CSV FILE FOUND!!"

	return data,count

#--Specially for location Scripts--
def toplocations(filename,value):

	print "-"*100+filename
	filepath=path+"/"+filename+".csv"
	if os.path.exists(filepath):

		file=open(filepath,"r")
		csv_reader=csv.reader(file,delimiter=',')

		if value == "Country":
			data = []
			for i in csv_reader:
				data.append(i[0])

		if value == "State":
			data = []
			for i in csv_reader:
				data.append(i[1])

		if value == "City":
			data = []
			for i in csv_reader:
				data.append(i[2])

		file.close()

		#--GET TOP COUNT--
		topcount=Counter(data)

		data, count = [], []

		if len(topcount) > 1:
			print "-"*50+"Top %s"%value
			for i in topcount.most_common()[:20]:
				print i
				data.append(i[0])
				count.append(i[1])
		else:
			print "!!No Activity FOUND!!"
			return None,None

	else:
		print "!NO CSV FILE FOUND!!"

	return data,count
