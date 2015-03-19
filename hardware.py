#!/usr/bin/python
#
# hardware.py
#
# A list of functions to be called by the cleaning algorithm in order to interact with the specified hardware
#
# Any hardware additions to the project should be added in their simplest form here with their serial interaction
#
# a) ULTRASOUND SENSORS:
#	
#	HARDWARE INFO:
#
#		>> VCC
#			- Green
#			- 5v
#
#		>> TRIG
#			- Grey
#			- GPIO 23
#
#		>> ECHO 
#			- Purple
#			- GPIO 24
#
#		>> GND
#			- Orange
#			- RPi GND
#
#	USAGE:
#
#		>> *var* = sensor() - Returns value to var of distance in cm rounded to 2 sf
#
# b) LCD:
#
#	HARDWARE INFO:
#
#		>> Vss
#			- GND (via potentiometer)
#
#		>> Vcc
#			- 5v (via potentiometer)
#
#		>> Vo
#			- Middle Pin of potentiometer
#
#		>> RS
#			- Pin 40
#
#		>> R/W
#			- GND (via potentiometer)
#
#		>> E
#			- Pin 41
#
#		>> D4
#			- Pin 42
#		
#		>> D5
#			- Pin 43
#
#		>> D6
#			- Pin 44
#
#		>> D7
#			- Pin 45
#
#		>> Backlight Anode
#			- 5v
#
#		>> Backlight Cathode
#			- GND
#
#	USAGE:
#
#		>> lcd(*string*) - Sends *string* as a tuple to be read as a stream via the Arduino
#
#
# c) MOTORS:
#	
#	HARDWARE INFO:
#
#		>> L293D IC Motor Stepper - Pin diagrams available
#
#		>> Left Motor
#			Clockwise - Arduino Pin 7
#			Anticlockwise - Arduino Pin 8
#
#		>> Right Motor
#			Clockwise - Arduino Pin 9
#			Anticlockwise - Arduino Pin 10
#	
#	USAGE:
#
#		Call the movement functions written below with a time to wait (t) - the duration of this call
#		will always be (t + 1)
#
#		>> forwards(t)
#		>> backwards(t)
#		>> left(t)
#		>> right(t)
#
#	TIMING:
#
#		For movement at a 90 degree angle, I have found that a time of roughly 2 seconds seems to give a good approximate value
#		Other angles can be calculated as time in the domain (t >= 1)
#		
#		Moving forwards for t=1 seconds gives a distance of 17cm
#

import time
from serial import Serial
#import RPi.GPIO as GPIO

from globals import *
#port = Serial('/dev/tty.usbmodem411',115200)
#time.sleep(1) # required as a waiting period for the port to be initialised

TRIG = 23
ECHO = 24
SPEED_OF_SOUND = 34300 # cm/s

def forwards(t):
	port.write('b')
	port.write(str(t))
	time.sleep(t + 1)

def backwards(t):
	port.write('c')
	port.write(str(t))
	time.sleep(t + 1)

def left(t):
	port.write('e')
	port.write(str(t))
	time.sleep(t + 1)

def right(t):
	port.write('d')
	port.write(str(t))
	time.sleep(t + 1)

def lcd(t):
	port.write('a')
	time.sleep(1)
	port.write(str(t))
	time.sleep(2)

def sensor():
	try:
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
	except:
		distance = 0
	return distance

def servo():
	port.write('f')
	time.sleep(3)

def test():
	left(4)

#test()
