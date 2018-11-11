from flask import Flask,render_template,request
from funciones import run_query
import os

app = Flask(__name__)
app.secret_key = 'secret key'
port = os.environ['PORT']

@app.route('/')
def inicio():
    return render_template("login.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method=="GET":
		return render_template("login.html")
	else:
		db_host = request.form['host']
		db_name = request.form['dbname']		
		db_user = request.form['user']
		db_pass = request.form['password']

		#Intenta iniciar sesión con los parámetros introducidos y ejecutar la sentencia establecida.
		query=run_query(db_host,db_name,db_user,db_pass)
		
		if query == None:
			error="No es posible realizar la conexión."
			return render_template("login.html",query=None)
		else:
			return render_template("login.html",query=query)


app.run('0.0.0.0', int(port), debug=False)
