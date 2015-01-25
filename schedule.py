#!/usr/bin/python
#
# schedule.py
# 
# setting schedule info, checking real time against schedule time and displaying
# information on the LCD screen
#
# USAGE:
#	>> new_time = Schedule()
#	>> __user inputs values__
#	>> new_time.show()
#	>> new_time.save()

import time
import pickle
from globals import *
from hardware import lcd

class Schedule:

	def __init__(self):
		self.date = int(input('Date: (dd)  '))
		self.month = int(input('Month: (MM)  '))
		self.hour = int(input('Hour: (hh)  '))
		self.minute = int(input('Minute: (mm)  '))
		self.name = raw_input('Name: ')
		self.info = (str(self.date) + '/' + str(self.month) + '/' + str(self.hour) + '/' + str(self.minute))

	def check(self):
		test = time.localtime()
		now = (test.tm_mday, test.tm_mon, test.tm_hour, test.tm_min)
		if now == self.info:
			return True
		else:
			return False
	
	def save(self):
		with open('schedule_data.dat','w') as data:
			pickle.dump(self.info,data)
			print "(+) DATA SAVED "
			print "(+) Press any key to continue "
			raw_input()

	def show(self):
		try:
			lcd(self.info)
		except OSError as e:
			print "Port not found"
			print "Handled exceptions send to log.txt"
			with open('log.txt','r') as log:
				log.append((e))
