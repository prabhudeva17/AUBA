#!/usr/bin/env	python2.7	
'''
--orchestra of whole scipts--
Unzip the data
mkdir CSV or check if already exist
run each and every script
print each Script output to terminal
finally remove the data
calculate the overall process time and print
'''

import zipfile,sys,os
import subprocess
from datetime import datetime

#--calculate the starttime--
start=datetime.now()

if not os.path.exists("./CSV"):
	os.mkdir('CSV')

#--extract zip file--
zip=zipfile.ZipFile(sys.argv[1])
zip.extractall()
print "Extraction Done!"

#--execute the scripts and print output to the screen--
def printoutput(script):
	p=subprocess.Popen(script,stdout=subprocess.PIPE)
	a=p.communicate()[0]
	print "!"*100
	b=a.split("\n")
	for i in b:
		print i


scripts = [
				['./scripts/Chrome_BrowserHistory.py',		'./Takeout/Chrome/BrowserHistory.json'],
				['./scripts/Chrome_BrowserExtension.py',	'./Takeout/Chrome/Extensions.json'],
				['./scripts/mail.py', 						'./Takeout/Mail/All mail Including Spam and Trash.mbox'],
				['./scripts/Map_Labeled_Places.py',		    './Takeout/Maps/My labeled places/Labeled places.json'],
				['./scripts/Map_Saved_Places.py', 			'./Takeout/Maps (your places)/Saved Places.json'],
				['./scripts/Youtube_Liked_Videos.py', 		'./Takeout/YouTube/playlists/likes.json'],
				['./scripts/location_history.py', 			'./Takeout/Location History/Location History.json'],
				['./scripts/android_activity.py', 			'./Takeout/My Activity/Android/MyActivity.html'],
				['./scripts/assistant_activity.py', 		'./Takeout/My Activity/Assistant/MyActivity.html'],
				['./scripts/playstoreapp.py', 				'./Takeout/My Activity/Google Play Store/MyActivity.html'],
				['./scripts/playmusic.py', 					'./Takeout/My Activity/Google Play Music/MyActivity.html'],
				['./scripts/googlesearch.py', 				'./Takeout/My Activity/Search/MyActivity.html'],
				['./scripts/youtube.py', 					'./Takeout/My Activity/YouTube/MyActivity.html'],
				['./scripts/android_device_config.py',		'./Takeout/Android Device Configuration Service/Device-3467564080470419407.html']
			]


for script in scripts:

	if os.path.exists(script[1]):
		printoutput(script)
	else:
		print "!!DATA NOT FOUND:-",script[1]

#--generate pdf report--
printoutput('./scripts/writepdf.py')

#--Remove the Takeout folder after finishing the analsis--
os.system('rm -rf ./Takeout')

#--calculate the stoptime--
stop=datetime.now()

#--print the totaltime taken to run the whole scripts--
print "Time Taken: ",stop-start
print "--------------------------XXXXXXXXXXXXXXXXX-------------------------"
