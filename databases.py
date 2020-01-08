"""#grab the data from the json files. If the data 
changes, the json files should have the oppurtunity
to be updated."""
import json

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
#functions for loading from json files

def load_water():
	mydata = open('Water.json','r').read()
	obj = json.loads(mydata)
	i=0
	while i < len(obj['Water']):
		name = obj['Water'][i]['Name']
		Ca = obj['Water'][i]['Calcium']
		Mg = obj['Water'][i]['Magnesium']
		SO4 = obj['Water'][i]['Sulfate']
		Na = obj['Water'][i]['Sodium']
		Cl = obj['Water'][i]['Chloride']
		HCO3 = obj['Water'][i]['Bicarbonate']
		waters.append(water(name, Ca, Mg, SO4, Na, Cl, HCO3))
		i=i+1

def load_malts():
	mydata = open('fermentables.json','r').read()
	obj = json.loads(mydata)
	i=0
	while i < len(obj['fermentables']):
		name = obj['fermentables'][i]['Grain']
		origin = obj['fermentables'][i]['Origin']
		color = obj['fermentables'][i]['Color']
		potential = obj['fermentables'][i]['Potential']
		maxpercent = obj['fermentables'][i]['Max_x00A0__x0025_']
		notes = obj['fermentables'][i]['Notes']
		pH = obj['fermentables'][i]['PH']
		malts.append(malt(name, origin, color, potential, maxpercent, notes, pH))
		i=i+1
	

def load_hops():
	mydata = open('Hops.json','r').read()
	obj = json.loads(mydata)
	i=0
	while i < len(obj['Hops']):
		name = obj['Hops'][i]['Name']
		AA_AVG = obj['Hops'][i]['Average_x0020_AA_x0025_']
		AA_Min = obj['Hops'][i]['Alpha_x0020_Acid_x0020_Min_x0020__x0025_']
		AA_Max = obj['Hops'][i]['Alpha_x0020_Acid_x0020_Max_x0020__x0025_']
		Subs = obj['Hops'][i]['Possible_x0020_Substitutions']
		Flav = obj['Hops'][i]['Flavor_x0020_Description']
		hops.append(hop(name, AA_AVG, AA_Min, AA_Max, Subs, Flav))
		i=i+1

def load_yeasts():
	mydata = open('Yeast.json','r').read()
	obj = json.loads(mydata)
	i=0
	while i < len(obj['Yeast']):
		name = obj['Yeast'][i]['Yeast'][0]
		brand = obj['Yeast'][i]['Brand']
		IDcode = obj['Yeast'][i]['Code']
		beertype = obj['Yeast'][i]['Type']
		alcmax = obj['Yeast'][i]['Alcohol_x0020_tolerance']
		flocc = obj['Yeast'][i]['Flocculation']
		attenuation = obj['Yeast'][i]['Attenuation']
		mintemp = obj['Yeast'][i]['Min_x0020_Temp']
		maxtemp = obj['Yeast'][i]['Max_x0020_Temp']
		yeasts.append(yeast(name, brand, IDcode, beertype, alcmax, flocc, attenuation, mintemp, maxtemp))
		i=i+1
		

def load_styles():
	mydata = open('Styles.json','r').read()
	obj = json.loads(mydata)
	i=0
	while i < len(obj['Styles']):
		name = obj['Styles'][i]['Beer_x0020_Style']
		catnum = obj['Styles'][i]['Category_x0020_Number']
		catlet = obj['Styles'][i]['"Style_x0020_Letter']
		stylenum = obj['Styles'][i]['Style_x0020__x0023_']
		cattype = obj['Styles'][i]['BJCP_x0020_Category']
		minOG = obj['Styles'][i]['Min_x0020_OG']
		maxOG = obj['Styles'][i]['Max_x0020_OG']
		minFG = obj['Styles'][i]['Min_x0020_FG']
		maxFG = obj['Styles'][i]['Max_x0020_FG']
		minABV = obj['Styles'][i]['Min_x0020_ABV']
		maxABV = obj['Styles'][i]['Max_x0020_ABV']
		minIBU = obj['Styles'][i]['Min_x0020_IBU']
		maxIBU = obj['Styles'][i]['Max_x0020_IBU']
		minSRM = obj['Styles'][i]['Min_x0020_SRM']
		maxSRM = obj['Styles'][i]['Max_x0020_SRM']
		guide = obj['Styles'][i]['Guide']
		styles.append(style(name, catnum, catlet, stylenum, cattype, minOG, maxOG, minFG, maxFG, minABV, maxABV, minIBU, maxIBU, minSRM, maxSRM, guide))
		i=i+1




