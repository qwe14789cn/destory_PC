#--------------------------------------------------------------------
#	set up start time
#--------------------------------------------------------------------
import time
year    = time.localtime()[0]
month   = time.localtime()[1]
day     = time.localtime()[2]
flag    = 2017*365 + 1*30 + 1 
print str(year)+'-'+str(month)+'-'+str(day)

#---------------------------------------------------------------------
#	auto del part
#---------------------------------------------------------------------
if year*365 + month*30 + day >=flag:
	print "import success"
	import auto_del
