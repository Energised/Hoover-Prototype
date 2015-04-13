#!/usr/bin/python
#
# quickytable.py
#
# makes my life just a little easier
#

from prettytable import PrettyTable # uses the PrettyTable lib

class QuickyTable(PrettyTable): # class inheriting from PrettyTable
	
	def __init__(self, *args): # unpacks a user defined list
		self.args = args # defines list
		self.table = PrettyTable(['Number','Option']) # creates a PrettyTable instance
		for number, place in enumerate(self.args): # 
			self.table.add_row([number, place])
		print self.table.get_string()
