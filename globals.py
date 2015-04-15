#!/usr/bin/python
#
# globals.py
#
# using this as a temporary method of holding the global variable
# port along with some exception handling for ease of use
#

from sys import exit # allows program to close
from serial import Serial # required Serial lib
from time import sleep # required module

PORT_NAME = '/dev/ttyACM0' # will only work on OS x, replace with /dev/ttyACM0 for Pi

try:
	print "(~) Accessing Port at " + PORT_NAME # displayed for troubleshooting
	global port # required for access over all files
	port = Serial(PORT_NAME, 115200) # port will only work for OSX
	sleep(1) # lag time caused by connection
	print "(+) Port accessed " # completed message
except OSError as e: # handling exception properly
	with open('log.txt','w') as log: # using log file
		log.write(str(e)) # outputs to log
		print "(-) Connection not available, check log file for more information "
		raw_input() # let used see message and respond
		exit() # will exit the code if no port can be detected
