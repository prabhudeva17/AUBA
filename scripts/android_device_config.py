#!/usr/bin/env	python2.7

import re
from wrcsv import *

a=gethtmldata()

data=[]

serialnum=re.findall(r'Serial Number\(s\):\s([\w\s\_\:]+)',a)

dtype=re.findall(r'Device Type:\s([\w\s]+)',a)

lang=re.findall(r'Locale:\s([\w\-]+)',a)

android_id=re.findall(r'Android ID:\s(\w+)',a)

imei=re.findall(r'IMEI\(s\):\s(\w+)',a)

timezone=re.findall(r'Timezone:\s([\w\/]+)',a)

model=re.findall(r'Model:\s([\w\_\-\s]+)',a)

brand=re.findall(r'Brand:\s([\w\_\-\s]+)',a)

manufacturer=re.findall(r'Manufacturer:\s([\w\_\-\s]+)',a)

device=re.findall(r'Device:\s([\w\_\-\s]+)',a)

hardware=re.findall(r'Hardware:\s([\w\_\-\s]+)',a)

firmware=re.findall(r'Radio Firmware Version:\s([\w\_\-\s\.]+)',a)

patch=re.findall(r'Security Patch Level:\s([\w\-]+)',a)

match=re.findall(r'<th>Group ID Level1<\/th>\n<\/tr><tr>\n\s+<td>[\w]+<\/td>\n\s+<td>([\w\s]+)</td>\n\s+<td>([\w\s]+)<\/td>\n\s+<td>([\w\s\,]+)<\/td>\n',a)

#CarrierName=match[0][0]
#RoamingState=match[0][1]
#DefaultRoles=match[0][2]

data.append(dtype[0])
data.append(model[0])
data.append(brand[0])
data.append(manufacturer[0])
data.append(hardware[0])
data.append(timezone[0])
data.append(lang[0])
data.append(android_id[0])
data.append(imei[0])
data.append(serialnum[0])
data.append(firmware[0])
data.append(patch[0])
data.append(match[0][0])
data.append(match[0][1])
data.append(match[0][2])
print data

for i in data:
	print i

writecsv0("Android_Device_Config",data)
