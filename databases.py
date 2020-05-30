"""#grab the data from the json files. If the data 
changes, the json files should have the oppurtunity
to be updated."""
import xml.etree.ElementTree as ET

malts = []
hops = []
styles = []
waters = []
yeasts = []
mashsteps = []

#=====================================================================
#classes for holding the values

class water:
	def __init__(self, name, Ca, Mg, SO4, Na, Cl, HCO3):
		self.name = name
		self.Ca = Ca
		self.Mg = Mg
		self.SO4 = SO4
		self.Na = Na
		self.Cl = Cl
		self.HCO3 = HCO3


class malt:
	def __init__(self, name, maltorigin, color, mashneeded, potential, maxpercent, notes, pH_added):
		self.name = name
		self.maltorigin = maltorigin
		self.color = color
		self.mashneeded = mashneeded
		self.potential = potential
		self.maxpercent = maxpercent
		self.notes = notes
		self.pH_added = pH_added

	def update(WhatPart, newVal):
		if WhatPart == "name":
			self.name = newVal
		elif WhatPart == "origin":
			self.maltorigin = newVal
		elif WhatPart == "color":
			self.color = newVal
		elif WhatPart == "mash":
			self.mashneeded = newVal
		elif WhatPart == "potential":
			self.potential = newVal
		elif WhatPart == "max%":
			self.maxpercent = newVal
		elif WhatPart == "notes":
			self.notes = newVal
		elif WhatPart == "pH":
			self.pH_added = newVal
		else: pass
		return
		
	
class hop:
	def __init__(self, name, AA_AVG, AA_Temp, AA_Min, AA_Max, Subs, Flav):
		self.name = name
		self.AA_AVG = AA_AVG
		self.AA_Temp = AA_Temp
		self.AA_Min = AA_Min
		self.AA_Max = AA_Max
		self.Subs = Subs 
		self.Flav = Flav
	
class mashStep:
	def __init__(self, name, mashtime, mashtemp, decoction):
		self.name = name
		self.mashtime = mashtime
		self.mashtemp = mashtemp
		self.decoction = decoction
	
class adjunct:
	def __init__(self, name, adjamount, adjtime):
		self.name = name
		self.adjamount = adjamount
		self.adjtime = adjtime

class yeast:
	def __init__(self, name, brand, IDcode, beertype, alcmax, flocc, attenuation, mintemp, maxtemp):
		self.name = name
		self.brand = brand
		self.IDcode = IDcode
		self.beertype = beertype
		self.alcmax = alcmax
		self.flocc = flocc
		self.attenuation = attenuation
		self.mintemp = mintemp
		self.maxtemp = maxtemp

class style:
	def __init__(self, name, catnum, catlet, stylenum, cattype, minOG, maxOG, minFG, maxFG, minABV, maxABV, minIBU, maxIBU, minSRM, maxSRM, guide):
		self.name = name 
		self.catnum = catnum 
		self.catlet = catlet 
		self.stylenum = stylenum 
		self.cattype = cattype 
		self.minOG = minOG 
		self.maxOG = maxOG 
		self.minFG = minFG 
		self.maxFG = maxFG 
		self.minABV = minABV 
		self.maxABV = maxABV 
		self.minIBU = minIBU 
		self.maxIBU = maxIBU 
		self.minSRM = minSRM 
		self.maxSRM = maxSRM 
		self.guide = guide

#======================================================================
#functions for loading from xml files

#https://docs.python.org/3/library/xml.etree.elementtree.html#module-xml.etree.ElementTree
def load_water():
	myroot = ET.parse('data/Water.xml').getroot()


load_water()
