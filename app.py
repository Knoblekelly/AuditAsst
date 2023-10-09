import os
from flask import Flask, render_template, request, redirect, abort
from werkzeug.utils import secure_filename
from script import db_create
from cs50 import SQL

app = Flask(__name__)
app.config['UPLOAD_EXTENSIONS'] = ['.csv']
app.config['UPLOAD_PATH'] = 'uploads'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_files():
	if request.method == 'POST':
		uploaded_file = request.files['file']
		filename = secure_filename(uploaded_file.filename)
		if filename != '':
			file_ext = os.path.splitext(filename)[1]
			if file_ext not in app.config['UPLOAD_EXTENSIONS']:
				abort(400)
			uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
			db_create(os.path.join(app.config['UPLOAD_PATH'], filename))
			return redirect("/results")
		else:
			return redirect("/upload")
	elif request.method == 'GET':
		return render_template('upload.html')

@app.route('/results')
def results():
	return render_template('results.html')

@app.route('/table', methods=['GET', 'POST'])
def table():
	db = SQL("sqlite:///data.db")
	if request.method == 'POST':
		udas_fin = db.execute(
			"INSERT INTO udas_fin (resident, adm, base, brad, deh, mor, pain, elop) SELECT a.resident, a.adm, b.bas, c.bra, d.deh, e.mor, f.pai, g.elo FROM (SELECT resident, MAX(date) AS adm FROM udas_raw WHERE uda LIKE '%Admit%' GROUP BY resident) AS a JOIN (SELECT resident, MAX(date) AS bas FROM udas_raw WHERE uda LIKE '%Base%' GROUP BY resident) AS b ON a.resident = b.resident JOIN (SELECT resident, MAX(date) AS bra FROM udas_raw WHERE uda LIKE '%Brad%' GROUP BY resident) AS c ON b.resident = c.resident JOIN (SELECT resident, MAX(date) AS deh FROM udas_raw WHERE uda LIKE '%Dehy%' GROUP BY resident) AS d ON c.resident = d.resident JOIN (SELECT resident, MAX(date) AS mor FROM udas_raw WHERE uda LIKE '%MORS%' GROUP BY resident) AS e ON d.resident = e.resident JOIN (SELECT resident, MAX(date) AS pai FROM udas_raw WHERE uda LIKE '%MORS%' GROUP BY resident) AS f ON e.resident = f.resident JOIN (SELECT resident, MAX(date) AS elo FROM udas_raw WHERE uda LIKE '%MORS%' GROUP BY resident) AS g ON f.resident = g.resident")
		udas = db.execute("SELECT * FROM udas_fin")
		return render_template('table.html', placeholder=udas)
	elif request.method == 'GET':
		udas = db.execute("SELECT * FROM udas_fin")
		return render_template('table.html', placeholder=udas)

@app.route('/delete', methods=['GET', 'POST'])
def delete():
	if request.method == 'POST':
		db = SQL("sqlite:///data.db")
		db.execute ("DELETE FROM udas_fin")
		db.execute ("DELETE FROM udas_raw")
		return redirect("/")
	elif request.method == 'GET':
		return render_template('delete.html')


