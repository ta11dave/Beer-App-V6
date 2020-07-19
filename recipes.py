#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import databases as db

recipes = []

"""Make a class that stores all the values of 
a recipe and has methods to add and subtract 
different ingedients and mash steps"""

class recipe:
	def __init__(self, name):
	#recipe name
		self.name = name
	#fermentable and weight in oz
		self.fermentables = []
	#hop, weight in oz, and boil time
		self.hops = []
	#step name, temp, and time
		self.mashsteps = []
	#adjunct, amount, and boil time
		self.adjuncts = []
	#yeast and amount
		self.yeast = "Empty"
	#water
		self.water = [0,0,0,0,0,0]

	def update_name(self, myname):
		self.name = myname

	def add_fermentable(self, myfermentable, amt):
		self.fermentables.append((myfermentable, amt))

	def remove_fermentable(self, myfermentable):
		for ferm in self.fermentables:
			if ferm[0] == myfermentable:
				self.fermentables.remove(ferm)

	def add_hop(self, myhop, amt, minutes):
		self.hops.append((myhop, amt, minutes))

	def remove_hop(self, myhop):
		whichitem = 0
		#input the name of the hop only
		for ahop in self.hops:
			print(ahop[0], myhop)
			if ahop[0] == myhop:
				self.hops.remove(ahop)

	def update_yeast(self, myyeast, amt):
		self.yeast = myyeast

	def add_mashstep(self, mymashsteps, temp, minutes):
		self.mashsteps.append((mymashsteps, temp, minutes))

	def remove_mashstep(self, mymashstep):
		for amashstep in self.mashsteps:
			if amashstep[0] == mymashstep:
				self.mashsteps.remove(amashstep)

	def add_adjunct(self, myadjuncts, amt, minutes):
		self.adjuncts.append((myadjuncts, amt, minutes))

	def remove_adjunct(self, myadjunct):
		for aadjunct in self.adjuncts:
			if aadjunct[0] == myadjunct:
				self.adjuncts.remove(aadjunct)

	def update_water(self, Ca, Mg, SO4, Na, Cl, HCO3):
		self.water = [Ca, Mg, SO4, Na, Cl, HCO3]

	def show(self):
		print('**' + self.name + '**')
		print("Fermentables: ")
		for x in self.fermentables:
			print(x[0], x[1])
		print("Hops: ")
		for x in self.hops:
			print(x[0], x[1], x[2])
		print("Mash Steps: ")
		for x in self.mashsteps:
			print(x[0], x[1], x[2])
		print("Adjuncts: ")
		for x in self.adjuncts:
			print(x)
		print("Yeast: ")
		print(self.yeast)
		print("Water: ")
		print("  Ca: " + str(self.water[0]))
		print("  Mg: " + str(self.water[1]))
		print("  SO4: " + str(self.water[2]))
		print("  Na: " + str(self.water[3]))
		print("  Cl: " + str(self.water[4]))
		print("  HCO3: " + str(self.water[5]))

def default_recipe():
	db.load_all()
	defaultRecipe = recipe("My glorious beer")
	defaultRecipe.add_fermentable("2-row", 3.125)
	defaultRecipe.add_hop("Citra", "5 oz", "whirlpool")
	defaultRecipe.add_mashstep("Saccrification", 67, 16)
	return defaultRecipe



