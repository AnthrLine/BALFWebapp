from modules import sheetoperator

def test():
	print(sheetoperator.eqfteams[0])	

def exec():
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

	rcontents.insert(39, sheetoperator.eqfteams[0])
	rcontents.insert(56, sheetoperator.eqnfteams[0])
	rcontents.insert(73, sheetoperator.indnfnames[0])
	rcontents.insert(89, sheetoperator.indfnames[0])
	rcontents.insert(107, sheetoperator.indpetnames[0])
	rcontents.insert(124, sheetoperator.indgrnames[0])
	

	with open("templates/index.html", "w") as f:
		rcontents = "".join(rcontents)
		f.write(rcontents)