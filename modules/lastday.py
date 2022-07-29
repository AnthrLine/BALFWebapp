from modules import sheetoperator

def fetchlastday(individualsnf=sheetoperator.individualsnf, individualsf=sheetoperator.individualsf, individualspet=sheetoperator.individualspet, individualsgr=sheetoperator.individualsgr, equipsnf=sheetoperator.equipsnf, equipsf=sheetoperator.equipsf):
	if sheetoperator.tot[1][3] == '':
		day = 2
		return day
	elif sheetoperator.tot[1][4] == '':
		day = 2
		return day
	elif sheetoperator.tot[1][5] == '':
		day = 3
		return day
	elif sheetoperator.tot[1][6] == '':
		day = 4
		return day
	elif sheetoperator.tot[1][7] == '':
		day = 5
		return day 
	else:
		day = 6
		return day