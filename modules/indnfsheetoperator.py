from modules import sheetoperator, nonetodash, lastday
from functools import reduce
import time

def exec():
	header = ''
	podium = []


	# HEADER CONTROL
	with open(r"modules/templates/indnf/headertemplate.html", 'r') as fp:
		header = fp.read() 

	with open('templates/indnf.html', 'w') as f:
		f.write(header)

	# HEADER CONTROL


	# PODIUM CONTROL

	# Read the podium template
	with open(r"modules/templates/indnf/podiumtemplate.html", 'r') as fp:
		podium = fp.readlines()

	# Changing the dummy text
	with open(r"workfile.html", 'w') as fp:
		for number, line in enumerate(podium):
			if number not in [1, 4, 6, 9, 12, 15, 20, 44, 47, 50, 53, 56, 59, 62]: #Lines that the code will delete
				fp.write(line)

	# Edit with a loop
	i = 0
	while i <=2:
		with open("workfile.html", "r") as readingfile:
			rcontents = readingfile.readlines()
		rcontents.insert(1, str(f'"{i+1}"'))
		rcontents.insert(4, f'<img class="badge podiumelement" src="../static/badges/badge{i+1}.png">')
		rcontents.insert(6, str(nonetodash.nonetodash(sheetoperator.tot[i + 1][1])))
		rcontents.insert(9, str(nonetodash.nonetodash(sheetoperator.tot[i + 1][2])))
		rcontents.insert(12, str(nonetodash.nonetodash(sheetoperator.tot[i + 1][8])))
		rcontents.insert(15, str(nonetodash.nonetodash(sheetoperator.tot[i + 1][11])))
		rcontents.insert(20, f'"t{i+1}"')
		rcontents.insert(44, str(nonetodash.nonetodash(sheetoperator.tot[i + 1][3])))
		rcontents.insert(47, str(nonetodash.nonetodash(sheetoperator.tot[i + 1][4])))
		rcontents.insert(50, str(nonetodash.nonetodash(sheetoperator.tot[i + 1][5])))
		rcontents.insert(53, str(nonetodash.nonetodash(sheetoperator.tot[i + 1][6])))
		rcontents.insert(56, str(nonetodash.nonetodash(sheetoperator.tot[i + 1][7])))
		rcontents.insert(59, str(nonetodash.nonetodash(sheetoperator.tot[i + 1][10])))
		rcontents.insert(62, str(nonetodash.nonetodash(sheetoperator.tot[i + 1][9])))
		write(rcontents)
		i += 1
	# PODOIUM CONTROL

	# LIST CONTROL
	with open(r"modules/templates/indnf/listtemplate.html", 'r') as fp:
		list = fp.readlines()

	# Changing the dummy text
	with open(r"workfile.html", 'w') as fp:
		for number, line in enumerate(list):
			if number not in [1, 7, 11, 15, 19, 23, 29, 53, 56, 59, 62, 65, 68, 71]: #Lines that the code will delete
				fp.write(line)

	# Edit with a loop
	i = 3
	while i <= sheetoperator.individualsnf[0]-1:
		with open("workfile.html", "r") as readingfile:
			rcontents = readingfile.readlines()
		rcontents.insert(1, str(f'"{i+1}"'))
		rcontents.insert(7, str(f'{i+1}'))
		rcontents.insert(11, str(nonetodash.nonetodash(sheetoperator.tot[i + 1][1])))
		rcontents.insert(15, str(nonetodash.nonetodash(sheetoperator.tot[i + 1][2])))
		rcontents.insert(19, str(nonetodash.nonetodash(sheetoperator.tot[i + 1][8])))
		rcontents.insert(23, str(nonetodash.nonetodash(sheetoperator.tot[i + 1][11])))
		rcontents.insert(29, f'"t{i+1}"')
		rcontents.insert(53, str(nonetodash.nonetodash(sheetoperator.tot[i + 1][3])))
		rcontents.insert(56, str(nonetodash.nonetodash(sheetoperator.tot[i + 1][4])))
		rcontents.insert(59, str(nonetodash.nonetodash(sheetoperator.tot[i + 1][5])))
		rcontents.insert(62, str(nonetodash.nonetodash(sheetoperator.tot[i + 1][6])))
		rcontents.insert(65, str(nonetodash.nonetodash(sheetoperator.tot[i + 1][7])))
		rcontents.insert(68, str(nonetodash.nonetodash(sheetoperator.tot[i + 1][10])))
		rcontents.insert(71, str(nonetodash.nonetodash(sheetoperator.tot[i + 1][9])))
		write(rcontents)
		print (i)
		i += 1
	# LIST CONTROL

	# FOOTER CONTROL
	with open(r"modules/templates/indnf/footertemplate.html", 'r') as fp:
		footer = fp.read() 

	with open('templates/indnf.html', 'a') as f:
		f.write(footer)
	# FOOTER CONTROL
		
# Final step: save and to the list we go
def write(rcontents):
	with open("templates/indnf.html", "a") as f:
		rcontents = "".join(rcontents)
		f.write(rcontents)