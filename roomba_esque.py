#!/usr/bin/python
#
# roomba_esque_clean.py 
#
# copies the style of the roombas clean, spiralling inside to the outside
# requires the user to begin the clean in the middle of the room

from globals import *
from serial import serial


def spiral():
	found = False
	while not found:
		jump = CURRENT_Y/17
		for time in range(2,CURRENT_Y,jump):
			check = sensor()
			if check <= 10:
				found = True
				break
			else:
				forwards(time)
				left(time)

