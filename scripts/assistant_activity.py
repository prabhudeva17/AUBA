#!/usr/bin/env  python2
'''
Voice Assistant MyActivity Questions and Answer, 
Other Activity like Phone Call, Message, Opening Application
'''
import re
from collections import Counter
from wrcsv import *

#--activity in HTML format-- 
a=gethtmldata()

#--Regex Expression--
voice_assistant_qanswer=re.findall(r'">([\w\s\&\;\#]+)</a><br>([\w\s\.]+)<br>([\w\s\,\:]+)</div>?',a)
others_assistant=re.findall(r'Selected\s([\w\s\+\,]+)<br>([\w\s\,\:]+)</div>?',a)

#--write data to csv file--
writecsv("Google_Assistant",['Question','Answer','Time'],voice_assistant_qanswer)
writecsv("Google_Assistant_others",['Name','others','Time'],others_assistant)

#--read data from csv file--
readcsv("Google_Assistant")
readcsv("Google_Assistant_others")
#--print output to terminal--

'''
for i in voice_assistant_qanswer:
	print "Question",i[0]
	print "\tAnswer",i[1]
	print "-"*100

topother=Counter(others_assistant)
print "*"*100+"Other Activity"
for i in topother.most_common()[:20]:
	print i
'''