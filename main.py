from flask import Flask, render_template, send_file, request, make_response
import requests
import time
import uuid
import schedule
import os
from threading import Thread
from modules import sheetoperator, mainhtmloperator, eqfsheetoperator, eqnfsheetoperator, indfsheetoperator, indnfsheetoperator, indpetsheetoperator, indgrsheetoperator, adgenerator, schedulef


app = Flask('app')

ads = []

def generateads():
	global ads
	ads = adgenerator.generate()
		

@app.route('/')
def main():
	schedule.run_pending()
	return render_template("index.html")

@app.route('/sw.js')
def sw():
	return send_file("sw.js")

@app.route('/index')
def index():
	schedule.run_pending()
	return render_template("index.html")

#@app.route('/testeqf')
def testeqf():
	eqfsheetoperator.exec()
	return ("Que sigui el que déu vulgui")

@app.route('/patrocinadors')
def patrocinadors():
	schedule.run_pending()
	return render_template("patrocinadors.html")

@app.route('/equipsfederats')
def equipsfederats():
	generateads()
	return render_template('eqf.html', ad1=ads[0], ad2=ads[1])

@app.route('/equipsnofederats')
def equipsnofederats():
	return render_template('eqnf.html', ad3=ads[2], ad4=ads[3])

@app.route('/individualnofederats')
def individualnofederats():
	return render_template('indnf.html', ad1=ads[4], ad2=ads[5])

@app.route('/individualfederats')
def individualfederats():
	return render_template('indf.html', ad1=ads[6], ad2=ads[7])

@app.route('/individual20102014')
def individual20102014():
	return render_template('indpet.html', ad1=ads[8], ad2=ads[9])

@app.route('/individual20062009')
def individual20062009():
	return render_template('indgr.html', ad1=ads[10], ad2=ads[11])

#@app.route('/csvexec')
def csvexec():
	sheetoperator.csvexec()
	mainhtmloperator.exec()
	eqfsheetoperator.exec()
	eqnfsheetoperator.exec()
	indfsheetoperator.exec()
	indnfsheetoperator.exec()
	indpetsheetoperator.exec()
	indgrsheetoperator.exec()
	generateads()
	return('Que sigui el que déu vulgui :)')

@app.route('/admin')
def admin():
	if request.cookies.get('uuid') == str(getuuid()):
		return render_template('admin.html')
	else:
		return loginform()

def getuuid():
	with open('uuid.txt', 'r') as uuidfile:
			uuidv = uuidfile.readlines()
			return(uuidv[0])

@app.route('/loginform')
def loginform():
	return render_template('loginform.html')
	
@app.route('/login', methods = ['POST', 'GET'])
def login():
	password = '-4959667821176916462'

	pwd = str(hash(request.form.get('pwd')))

	if password == pwd:
		uuidv = str(uuid.uuid4())

		with open('uuid.txt', 'w') as uuidfile:
			uuidfile.write(str(uuidv))

		resp = make_response(render_template('admin.html'))
		resp.set_cookie('uuid', uuidv)
		return resp 
	else:
		return loginform()
		

@app.route('/file', methods = ['POST', 'GET'])
def file():
	if os.path.exists('Web.xlsx'):
		os.remove('Web.xlsx')
	if request.cookies.get('uuid') == str(getuuid()):
		if request.method == 'POST':
			f = request.files['xlsx']
			f.save(f.filename)
			csvexec()
			return admin()	

	else:
		return("You don't have permission to do that")

if __name__ == '__main__':
	schedule.every(10).seconds.do(generateads)
	schedule.run_pending()
	t = Thread(target=schedulef.run)
	t.start()
	app.config['TESTING'] = True
	app.config['UPLOAD_FOLDER'] = '/'
	app.config['TEMPLATES_AUTO_RELOAD'] = True
	app.run(host='0.0.0.0', port=5000)
	