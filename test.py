#!/usr/bin/python
#
# test.py
#
# Every component should run and output a value, tests to see if a value is output and if not then return an error
# but continue with the test on all components to check every bit of the system - can be exited if necessary
#
# USAGE:
#	new_test = Test('/dev/tty.usbmodem411',115200)
#	print new_test.errors (PrettyTable integration would be nice...)
#

import time
import sys

from serial import Serial

class Test:

        """ A system-wide test of hardware, software, serial interaction etc (doesn't use the global port name) """
        
	def __init__(self, port, baud, errors=[]):
		self.port = port
		self.baud = baud
		self.errors = errors
		try:
			print "\r(~) ACCESSING PORT {}".format(self.port) + " " * 40
			self.connection = Serial(self.port, self.baud)
			time.sleep(1)
			sys.stdout.flush()
			print '\r(+) SUCCESS'
		except Exception as e:
			self.errors.append((e))
			print '(-) ERROR OCCURED ON CONNECTION\n'
			print '(-) EXCEPTIONS APPENDED TO LOG\n'

	def motor(self):
		try:
			print "(~) Powering Motors Forwards "
			self.connection.write('b')
			self.connection.write('4')
			time.sleep(1) #lag time 
			time.sleep(4)
			print "(~) Powering Motors Backwards "
			self.connection.write('c')
			self.connection.write('4')
			time.sleep(1) #lag time 
			time.sleep(4)
			print "(~) Powering Motors Left "
			self.connection.write('d')
			self.connection.write('4')
			time.sleep(1) #lag time 
			time.sleep(4)
			print "(~) Powering Motors Right"
			self.connection.write('e')
			self.connection.write('4')
			time.sleep(1) #lag time 
			time.sleep(4)
			print "(+) SUCCESSFUL"
		except Exception as e:
			self.errors.append((e))
			print "(-) MOTOR CONNECTION FAILED"

	def lcd(self):
		try:
			print "(~) INITIALISING LCD"
			self.connection.write("a")
			self.connection.write("test post")
			time.sleep(4)
			print "(+) LCD WORKING"
		except Exception as e:
			self.errors.append((e))
			print "(-) LCD CONNECTION FAILED"

	def sensor(self):
		try:
			#import RPi.GPIO as GPIO
			GPIO.setmode(GPIO.BCM)
			GPIO.setup(TRIG, GPIO.OUT)
			GPIO.setup(ECHO, GPIO.IN)
			GPIO.output(TRIG, False)
			time.sleep(2)
			GPIO.output(TRIG, True)
			time.sleep(0.00001)
			GPIO.output(TRIG, False)
			while GPIO.input(ECHO) == 0:
				pulse_start = time.time()
			while GPIO.input(ECHO) == 1:
				pulse_end = time.time()
			pulse_duration = pulse_end - pulse_start
			distance = pulse_duration * (SPEED_OF_SOUND/2)
			distance = round(distance, 2)
			print distance
		except Exception as e:
			self.errors.append(e)
			print "(-) SENSOR TEST FAILED"

	def servo(self):
		try:
			print "(~) MOVING BRUSH SERVO"
			self.connection.write('f')
			time.sleep(3)
			print "(+) BRUSH SERVO WORKING"
		except Exception as e:
			self.errors.append(e)
			print "(-) BRUSH SERVO TEST FAILED"

	def full_check(self):
		self.motor()
		self.lcd()
		#for _ in range(5):
		#	self.sensor()

	def log(self):
		with open('errors.txt','w') as err:
			err.write(str(self.errors))
