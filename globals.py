#!/usr/bin/python
#
# globals.py
#
# using this as a temporary method of holding the global variable
# port along with some exception handling for ease of use
#

from sys import exit
from serial import Serial
from time import sleep

PORT_NAME = '/dev/ttyACM0'

try:
	print "(~) Accessing Port at " + PORT_NAME
	global port
	port = Serial(PORT_NAME, 115200) # port will only work for OSX
	sleep(1) # lag time
	print "(+) Port accessed "
except OSError as e:
	with open('log.txt','w') as log:
		log.write(str(e))
		print "(-) Connection not available, check log file for more information "
		raw_input()
		exit() # will exit the code if no port can be detected
