#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import databases

recipes = []

"""Make a class that stores all the values of 
a recipe and has methods to add and subtract 
different ingedients and mash steps"""

class recipe:
	def __init__(self, name):
		self.name = name
		self.fermentables = []
		self.hops = []
		self.mashsteps = []
		self.adjuncts = []
		self.yeast = []
		self.water = []
