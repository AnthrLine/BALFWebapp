from modules import sheetoperator

day = 0
categories = ['indnf', 'indf', 'indpet', 'indgr', 'eqnf', 'eqf']
days = ['dilluns', 'dimarts', 'dimecres', 'dijous', 'divendres']

def fetchlastday(): #Returns the points of the last day
	if sheetoperator.eqfdilluns[0] == None:
		day = 0
		return day
	elif sheetoperator.eqfdimarts[0] == None:
		day = 0
		return day
	elif sheetoperator.eqfdimecres[0] == None:
		day = 1
		return day
	elif sheetoperator.eqfdijous[0] == None:
		day = 2
		return day
	elif sheetoperator.eqfdivendres[0] == None:
		day = 3
		return day
	else:
		day = 4
		return day

def lastday(category):
	variable = f'{categories[category]}{days[fetchlastday()]}'
	return (variable)