from modules import sheetoperator, nonetodash

def test():
	print(sheetoperator.eqfteams[0])	

def exec(individualsnf=sheetoperator.individualsnf, individualsf=sheetoperator.individualsf, individualspet=sheetoperator.individualspet, individualsgr=sheetoperator.individualsgr, equipsnf=sheetoperator.equipsnf, equipsf=sheetoperator.equipsf):
	lines = []
	with open(r"modules/indextemplate.html", 'r') as fp:
		lines = fp.readlines() 

	with open(r"templates/index.html", 'w') as fp:
		for number, line in enumerate(lines):
			if number not in [39, 56, 73, 89, 107, 124]: #Lines that the code will delete
				fp.write(line)


	#Adding the names
	with open("templates/index.html", "r") as readingfile:
		rcontents = readingfile.readlines()		

	rcontents.insert(39, str(nonetodash.nonetodash(sheetoperator.tot[individualsnf[0] + individualsf[0] + individualspet[0] + individualsgr[0] + equipsnf[0] + 1][1])))
	rcontents.insert(56, str(nonetodash.nonetodash(sheetoperator.tot[individualsnf[0] + individualsf[0] + individualspet[0] + individualsgr[0] + 1][1])))
	rcontents.insert(73, str(nonetodash.nonetodash(sheetoperator.tot[1][1])))
	rcontents.insert(89, str(nonetodash.nonetodash(sheetoperator.tot[individualsnf[0] + 1][1])))
	rcontents.insert(107, str(nonetodash.nonetodash(sheetoperator.tot[individualsnf[0] + individualsf[0] + 1][1])))
	rcontents.insert(124, str(nonetodash.nonetodash(sheetoperator.tot[individualsnf[0] + individualsf[0] + individualspet[0] + 1][1])))
	

	with open("templates/index.html", "w") as f:
		rcontents = "".join(rcontents)
		f.write(rcontents)