from modules import sheetoperator, nonetodash, lastday, adgenerator
from functools import reduce
import time

def exec():
	header = ''
	podium = []


	# HEADER CONTROL
	
	with open(r"modules/templates/eqf/headertemplate.html", 'r') as fp:
		header = fp.read() 

	with open('templates/eqf.html', 'w') as f:
		f.write(header)

	# HEADER CONTROL


	# PODIUM CONTROL

	# Read the podium template
	with open(r"modules/templates/eqf/podiumtemplate.html", 'r') as fp:
		podium = fp.readlines()

	# Changing the dummy text
	with open(r"workfile.html", 'w') as fp:
		for number, line in enumerate(podium):
			if number not in [1, 4, 6, 9, 12, 17, 38, 41, 44, 47, 50, 53]: #Lines that the code will delete
				fp.write(line)

	# Edit with a loop
	lastdayvar = str(nonetodash.nonetodash(lastday.lastday(5)))
	i = 0
	while i <=0:
		lastdaypoints = getattr(sheetoperator, lastdayvar, i)
		with open("workfile.html", "r") as readingfile:
			rcontents = readingfile.readlines()
		rcontents.insert(1, str(f'"{i+1}"'))
		rcontents.insert(4, '<img class="badge podiumelement" src="../static/badges/badge1.png">')
		rcontents.insert(6, str(nonetodash.nonetodash(sheetoperator.eqfteams[int(i)])))
		rcontents.insert(9, str(nonetodash.nonetodash(sheetoperator.eqftotpunts[int(i)])))
		rcontents.insert(12, str(nonetodash.nonetodash(lastdaypoints[i])))
		rcontents.insert(17, f'"t{i+1}"')
		rcontents.insert(38, str(nonetodash.nonetodash(sheetoperator.eqfdilluns[int(i)])))
		rcontents.insert(41, str(nonetodash.nonetodash(sheetoperator.eqfdimarts[int(i)])))
		rcontents.insert(44, str(nonetodash.nonetodash(sheetoperator.eqfdimecres[int(i)])))
		rcontents.insert(47, str(nonetodash.nonetodash(sheetoperator.eqfdijous[int(i)])))
		rcontents.insert(50, str(nonetodash.nonetodash(sheetoperator.eqfdivendres[int(i)])))
		rcontents.insert(53, str(nonetodash.nonetodash(sheetoperator.eqfbitlles[int(i)])))
		write(rcontents)
		i += 1
	# PODOIUM CONTROL

	# LIST CONTROL
	with open(r"modules/templates/eqf/listtemplate.html", 'r') as fp:
		list = fp.readlines()

	# Changing the dummy text
	with open(r"workfile.html", 'w') as fp:
		for number, line in enumerate(list):
			if number not in [1, 7, 11, 15, 19, 25, 46, 49, 52, 55, 58, 61]: #Lines that the code will delete
				fp.write(line)

	# Edit with a loop
	i = 1
	while i <= 6:
		lastdaypoints = getattr(sheetoperator, lastdayvar, i)
		with open("workfile.html", "r") as readingfile:
			rcontents = readingfile.readlines()
		rcontents.insert(1, str(f'"{i+1}"'))
		rcontents.insert(7, str(f'{i+1}'))
		rcontents.insert(11, str(nonetodash.nonetodash(sheetoperator.eqfteams[int(i)])))
		rcontents.insert(15, str(nonetodash.nonetodash(sheetoperator.eqftotpunts[int(i)])))
		rcontents.insert(19, str(lastdaypoints[i]))
		rcontents.insert(25, f'"t{i+1}"')
		rcontents.insert(46, str(nonetodash.nonetodash(sheetoperator.eqfdilluns[int(i)])))
		rcontents.insert(49, str(nonetodash.nonetodash(sheetoperator.eqfdimarts[int(i)])))
		rcontents.insert(52, str(nonetodash.nonetodash(sheetoperator.eqfdimecres[int(i)])))
		rcontents.insert(55, str(nonetodash.nonetodash(sheetoperator.eqfdijous[int(i)])))
		rcontents.insert(58, str(nonetodash.nonetodash(sheetoperator.eqfdivendres[int(i)])))
		rcontents.insert(61, str(nonetodash.nonetodash(sheetoperator.eqfbitlles[int(i)])))
		write(rcontents)
		i += 1
	# LIST CONTROL

	# FOOTER CONTROL
	with open(r"modules/templates/eqf/footertemplate.html", 'r') as fp:
		footer = fp.read() 

	with open('templates/eqf.html', 'a') as f:
		f.write(footer)
	# FOOTER CONTROL
		
# Final step: save and to the list we go
def write(rcontents):
	with open("templates/eqf.html", "a") as f:
		rcontents = "".join(rcontents)
		f.write(rcontents)