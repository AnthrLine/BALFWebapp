from modules import sheetoperator, nonetodash

def test():
	print(sheetoperator.eqfteams[0])	

def exec(individualsnf=sheetoperator.individualsnf, individualsf=sheetoperator.individualsf, individualspet=sheetoperator.individualspet, individualsgr=sheetoperator.individualsgr, equipsnf=sheetoperator.equipsnf, equipsf=sheetoperator.equipsf):
	lines = []
	with open(r"modules/indextemplate.html", 'r') as fp:
		lines = fp.readlines() 

	with open(r"templates/index.html", 'w') as fp:
		for number, line in enumerate(lines):
			if number not in [44, 63, 82, 100, 120, 139]: #Lines that the code will delete
				fp.write(line)


	#Adding the names
	with open("templates/index.html", "r") as readingfile:
		rcontents = readingfile.readlines()		

	rcontents.insert(44, str(nonetodash.nonetodash(sheetoperator.tot[individualsnf[0] + individualsf[0] + individualspet[0] + individualsgr[0] + equipsnf[0] + 1][1])))
	rcontents.insert(63, str(nonetodash.nonetodash(sheetoperator.tot[individualsnf[0] + individualsf[0] + individualspet[0] + individualsgr[0] + 1][1])))
	rcontents.insert(82, str(nonetodash.nonetodash(sheetoperator.tot[1][1])))
	rcontents.insert(100, str(nonetodash.nonetodash(sheetoperator.tot[individualsnf[0] + 1][1])))
	rcontents.insert(120, str(nonetodash.nonetodash(sheetoperator.tot[individualsnf[0] + individualsf[0] + 1][1])))
	rcontents.insert(139, str(nonetodash.nonetodash(sheetoperator.tot[individualsnf[0] + individualsf[0] + individualspet[0] + 1][1])))
	

	with open("templates/index.html", "w") as f:
		rcontents = "".join(rcontents)
		f.write(rcontents)