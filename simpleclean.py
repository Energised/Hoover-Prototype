#!/usr/bin/python
#
# simpleclean.py 
#
# Most simplistic algorithm for cleaning a room
#
# SYSTEM OVERVIEW:
#
# a) move within range of wall
# b) turns in passed direction for 90 degrees
# c) moves until object in way
# d) repeat b and c 4 times
# e) turn 90 degrees
# f) recursive call - move within (distance + 20) of other sides wall, change direction 
# g) repeat a -> f until (distance = CURRENT_Y - 40)
#

from globals import *
from hardware import *

from clean import *

def clean_a(verticle, direction, CURRENT_X, CURRENT_Y): # direction must be called as 'l' or 'r'
	found_wall = False
	while not found_wall:
		forwards(2)
		distance = sensor()
		if distance <= 20:
			found_wall = True # end of a)
	
	found_block = False
	if direction == 'l': 
		left(2)
	else:
		right(2)
	while not found_block:
		distance = sensor()
		if distance >= 30:
			found_block = True
		else:
			if direction == 'l':
				left(2)
			else:
				right(2)
			forwards(1)
			if direction == 'l':
				right(2)
			else:
				left(2) # end of b)
	
	for _ in range(4):
		found_object = False
		while not found_object:
			forwards(2) # end of c)
			distance = sensor()
			if distance <= 20:
				found_object = True
			forwards(1)
			stuck_check = sensor()
			if stuck_check == distance:
				backwards(1)
				found_object = True # end of d)
		if direction == 'l':
			left(2)
		else:
			right(2) # end of e)
	move = (CURRENT_X / 2)/17
	move = round(move, 2)
	forwards(move)
	passes += 1
	CURRENT_Y -= 25
	if direction == 'l':
		left(2)
		clean_a(CURRENT_Y,'r')
	else:
		right(2)
		clean_a(CURRENT_Y,'l')
