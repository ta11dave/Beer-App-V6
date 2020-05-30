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

	def add_fermentable(self, myfermentable):
		x = input("What how many oz? ")
		self.fermentables.append((myfermentable, x))

	def remove_fermentable(self, myfermentable):
		for ferm in self.fermentables:
			if ferm[0] == myfermentable:
				self.fermentables.remove(myfermentable)

	def add_hop(self, myhop):
		x = input("What how many oz? ")
		y = input("What long in the boil? ")
		self.hops.append((myhop, x, y))

	def remove_hop(self, myhop):
		for ahop in self.hops:
			if ahop[0] == myhop:
				self.hops.remove(myhop)

	def update_yeast(self, myyeast):
		self.yeast = myyeast

	def add_mashstep(self, mymashsteps):
		self.mashsteps.append(mymashsteps)

	def remove_mashstep(self, mymashstep):
		for amashstep in self.mashsteps:
			if amashstep[0] == mymashstep:
				self.mashsteps.remove(mymashstep)

	def add_adjunct(self, myadjuncts):
		self.adjuncts.append(myadjuncts)

	def remove_adjunct(self, myadjunct):
		for aadjunct in self.adjuncts:
			if aadjunct[0] == myadjunct:
				self.adjuncts.remove(myadjunct)

	def update_water(self, Ca, Mg, SO4, Na, Cl, HCO3):
		self.water = [Ca, Mg, SO4, Na, Cl, HCO3]

	def show(self):
		print('**' + self.name + '**')
		print("Fermentables: ")
		for x in self.fermentables:
			print(x[0].name, x[1])
		print("Hops: ")
		for x in self.hops:
			print(x[0].name, x[1], x[2])
		print("Mash Steps: ")
		for x in self.mashsteps:
			print(x)
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

#tests
db.load_all()
testrecipe = recipe("My beer")
testrecipe.show()
#print("X")
#testrecipe.add_hop(db.hops[0])
#testrecipe.show()
