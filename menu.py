#!/usr/bin/python
#
# menu.py
#
# main function for main menu
#
# arduino/computer serial interaction menu
#
# REQUIRED MODULES:
#   - schedule.py - Schedule addition
#   - clean.py - Main Program
#   - test.py - Test both Arduino and RPi
#   - check.py - Checks for the .dat file
#   - globals.py - Contains the port information to be called straight away (not called in test.py)
#   - quickytable.py - Bespoke solution to make life easy
#

import time

from serial import Serial # externalities

from quickytable import QuickyTable # homemade modules
from schedule import Schedule
from test import Test
from clean import Clean

from hardware import * # also homemade
from globals import *

class Menu():

	""" Menu structure and base level of the program, displayed with a lightweight solution to PrettyTable """

	def __init__(self):
		QuickyTable('Begin Cleaning','Add To Schedule','Run Test Protocol')
		self.decide()

	def decide(self):
		self.choice = int(input("(~) "))
		if self.choice == 0:
			self.cleaning()
		elif self.choice == 1:
			self.add_schedule()
		elif self.choice == 2:
			self.test_func()

	def cleaning(self):
		self.__clear__()
		new_clean = Clean()
		new = Menu()

	def add_schedule(self):
		self.__clear__()
		set_clean = Schedule() # calls an instance of schedule to be made and checked
		if self_clean.check():
			new_clean = Clean()
		set_clean.save()
		set_clean.show()
		new = Menu()

	def test_func(self):
		self.__clear__()
		check = Test('/dev/ttyACM0',115200) # initialises a test protocol
		done = False
		while not done:
			QuickyTable("Motors", "LCD", "Both")
			test_check = int(input("(~) What do you want to test?: "))
			done = True
			if test_check == 0:
				check.motor()
			elif test_check == 1:
				check.lcd()
			elif test_check == 2:
				check.full_check()
			else:
				done = False
				print "(-) Invalid input "
		check.log()
		new = Menu()


	def __clear__(self):
		try:
			from subprocess import call
			call(['clear'])
		except ImportError:
			print "The module subprocess isn't included in your library."
		except OSError:
			print "Your bash doesn't have the function clear available."


if __name__ == '__main__':
	new = Menu()
