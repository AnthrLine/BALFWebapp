from modules import sheetoperator, nonetodash, lastday
from functools import reduce
import time

def exec():
	header = ''
	podium = []


	# HEADER CONTROL
	with open(r"modules/templates/indgr/headertemplate.html", 'r') as fp:
		header = fp.read() 

	with open('templates/indgr.html', 'w') as f:
		f.write(header)

	# HEADER CONTROL


	# PODIUM CONTROL

	# Read the podium template
	with open(r"modules/templates/indgr/podiumtemplate.html", 'r') as fp:
		podium = fp.readlines()

	# Changing the dummy text
	with open(r"workfile.html", 'w') as fp:
		for number, line in enumerate(podium):
			if number not in [1, 4, 6, 9, 12, 15, 20, 32, 35, 38]: #Lines that the code will delete
				fp.write(line)

	# Edit with a loop
	i = 0
	while i <=2:
		with open("workfile.html", "r") as readingfile:
			rcontents = readingfile.readlines()
		rcontents.insert(1, str(f'"{i+1}"'))
		rcontents.insert(4, f'<img class="badge podiumelement" src="../static/badges/badge{i+1}.png">')
		rcontents.insert(6, str(nonetodash.nonetodash(sheetoperator.indgrnames[int(i)])))
		rcontents.insert(9, str(nonetodash.nonetodash(sheetoperator.indgrteams[int(i)])))
		rcontents.insert(12, str(nonetodash.nonetodash(sheetoperator.indgrmitjana[int(i)])))
		rcontents.insert(15, str(nonetodash.nonetodash(sheetoperator.indgrtirades[int(i)])))
		rcontents.insert(20, f'"t{i+1}"')
		rcontents.insert(32, str(nonetodash.nonetodash(sheetoperator.indgrmitjana[int(i)])))
		rcontents.insert(35, str(nonetodash.nonetodash(sheetoperator.indgrbitlles[int(i)])))
		rcontents.insert(38, str(nonetodash.nonetodash(sheetoperator.indgrpunts[int(i)])))
		write(rcontents)
		i += 1
	# PODOIUM CONTROL

	# LIST CONTROL
	with open(r"modules/templates/indgr/listtemplate.html", 'r') as fp:
		list = fp.readlines()

	# Changing the dummy text
	with open(r"workfile.html", 'w') as fp:
		for number, line in enumerate(list):
			if number not in [1, 7, 11, 15, 19, 23, 29, 41, 44, 47]: #Lines that the code will delete
				fp.write(line)

	# Edit with a loop
	i = 3
	while i <= sheetoperator.individualsgr[0]-1:
		with open("workfile.html", "r") as readingfile:
			rcontents = readingfile.readlines()
		rcontents.insert(1, str(f'"{i+1}"'))
		rcontents.insert(7, str(f'{i+1}'))
		rcontents.insert(11, str(nonetodash.nonetodash(sheetoperator.indgrnames[int(i)])))
		rcontents.insert(15, str(nonetodash.nonetodash(sheetoperator.indgrteams[int(i)])))
		rcontents.insert(19, str(nonetodash.nonetodash(sheetoperator.indgrmitjana[int(i)])))
		rcontents.insert(23, str(nonetodash.nonetodash(sheetoperator.indgrtirades[int(i)])))
		rcontents.insert(29, f'"t{i+1}"')
		rcontents.insert(41, str(nonetodash.nonetodash(sheetoperator.indgrmitjana[int(i)])))
		rcontents.insert(44, str(nonetodash.nonetodash(sheetoperator.indgrbitlles[int(i)])))
		rcontents.insert(47, str(nonetodash.nonetodash(sheetoperator.indgrpunts[int(i)])))
		write(rcontents)
		print (i)
		i += 1
	# LIST CONTROL

	# FOOTER CONTROL
	with open(r"modules/templates/indgr/footertemplate.html", 'r') as fp:
		footer = fp.read() 

	with open('templates/indgr.html', 'a') as f:
		f.write(footer)
	# FOOTER CONTROL
		
# Final step: save and to the list we go
def write(rcontents):
	with open("templates/indgr.html", "a") as f:
		rcontents = "".join(rcontents)
		f.write(rcontents)