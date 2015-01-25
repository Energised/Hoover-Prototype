#!/usr/bin/python
#
# quickytable.py
#
# makes my life just a little easier
#

from prettytable import PrettyTable

class QuickyTable(PrettyTable):
	
	def __init__(self, *args):
		self.args = args
		self.table = PrettyTable(['Number','Option'])
		for number, place in enumerate(self.args):
			self.table.add_row([number, place])
		print self.table.get_string()