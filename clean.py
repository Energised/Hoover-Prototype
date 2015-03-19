#!/usr/bin/python
#
# clean.py
#
# main algorithm and cleaning system required
#
#
# USAGE:
#	When adding a room, the dictionary will save the room name as '{*name*_x:*num*,*name*_y:*num*}'
#
# ALGORITHM INSTRUCTIONS:
#	
#		a) Simple Clean - Takes the size of the room and moves from the middle outwards moving around objects and 
#						  working its way back into the middle of the room.
#
#		b) Roomba Style - Starts in the middle of the room, spirals outwards from the centre until it hits an object, 
#						  then moves around the outside to clean at each corner
#
#		c) Spanning Tree - Randomly generates a tree from the middle of one width to the other width and made up of vertices at each 100 pixel
#						   gap, cleaning down each edge from one side to another, then doing the same thing from the other side
#
#

from serial import Serial
from hardware import *
from quickytable import QuickyTable
from simpleclean import *
from roomba_esque import *

import pickle

CURRENT_X = 0
CURRENT_Y = 0

rooms = {}

class Clean:

	""" Specification for cleaning system - user algorithm choice and calls """

	def __init__(self):
		print "(~) Commencing clean "
		print "(~) Choosing Room "
		print "(~) List of current rooms "
		with open('rooms.dat','rb') as data:
			self.info = pickle.load(data)
		for section in self.info.items():
			for part in section:
				print part
		choice = raw_input("(~) Enter room name (if name doesn't exist one will be made) ")
		choice_x, choice_y = choice + '_x', choice + '_y'
		if choice_x in self.info:
			CURRENT_X = self.info[choice_x]
			CURRENT_Y = self.info[choice_y]
		else:
			val_x = int(input("(~) Input " + choice + "'s length (longest side): "))
			val_y = int(input("(~) Input " + choice + "'s width (shortest side): "))
			self.info[choice_x], self.info[choice_y] = val_x, val_y
			CURRENT_X, CURRENT_Y = val_x, val_y
		self.__clear__()
		rooms = self.info
		print "(+) Using the Room Size (in cm): " + str(CURRENT_X) + ',' + str(CURRENT_Y)
		self.__save__()
		print "(~) User algorithm decision "
		QuickyTable('Simple Clean', 'Roomba-esque', 'Spanning Tree') # 3 simple options for now
		done = False
		while not done:
			done = True
			alg_choice = int(input("(~) Awaiting User Input "))
			if alg_choice == 0:
				self.simple_clean()
			elif alg_choice == 1:
				self.roomba_style()
			elif alg_choice == 2:
				self.spanning_tree()
			else:
				print "(-) Invalid User Input "
				done = False

	def simple_clean(self):
		passes = 0
		CURRENT_X, CURRENT_Y, passes = clean_a(CURRENT_Y,'l', CURRENT_X, CURRENT_Y)

	def roomba_esque(self):
		CURRENT_X, CURRENT_Y = clean_b()

	def spanning_tree(self):
		pass

	def __save__(self):
		with open('rooms.dat','a') as size:
			pickle.dump(rooms, size)
			print "(+) Data Saved "

	def __clear__(self):
		try:
			from subprocess import call
			call(['clear'])
		except ImportError:
			print "The module subprocess isn't included in your library "
		except OSError:
			print "Please add the alias clear to your .bashrc or .bashprofile "
