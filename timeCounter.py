
'''The following script has been designed to do a certain task every 1 hour, you can change it according to your need. '''
from datetime import datetime
import math

#This runs at the start of the script
before = datetime.strptime(datetime.strftime(datetime.now(),'%H:%M:%S'),'%H:%M:%S')
while True:
	after = datetime.strptime(datetime.strftime(datetime.now(),'%H:%M:%S'),'%H:%M:%S')
	if (((after - before).seconds)/3600) ==1:
		before = datetime.strptime(datetime.strftime(datetime.now(),'%H:%M:%S'),'%H:%M:%S')
        	print "1 hour tweet",(((after - before).seconds))
		#You can call any function here
