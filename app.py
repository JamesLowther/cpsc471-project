from flask import Flask, flash, escape, request, render_template, redirect, url_for, session, jsonify
from datetime import timedelta
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)
# api = Api(app)
# basedir = os.path.abspath(os.path.dirname(__file__))
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite3')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.secret_key = "superSecret"
# app.permanent_session_lifetime = timedelta(minutes=1)

# db = SQLAlchemy()
# db.init_app(app)
# #init ma
# ma = Marshmallow(app)

# class PatientModel(db.Model):
# 	pid = db.Column("pid", db.Integer, primary_key=True)
# 	name = db.Column(db.String(100), nullable=False)
# 	email = db.Column(db.String(100), unique=True)
# 	family_doctor = db.Column(db.Integer, db.ForeignKey('Doctor.ssn'))

# 	def __init__(self):
# 		return f"Patient(name = {name}, email = {email}, family_doctor = {family_doctor})"

# class DoctorModel(db.Model):
# 	ssn = db.Column(db.Integer, primary_key=True)
# 	name = db.Column(db.String(50), nullable=False)
# 	specialization = db.Column(db.String(100), nullable=True)

# 	def __repr__(self):
# 		return f"Doctor(name = {name}, specialization = {specialization})"

@app.route('/about')
def about():
	return render_template("about.html")

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/view")
def view():
	return render_template("view.html", values=users.query.all())

@app.route("/newPatient")
def newPatient():
	return render_template("newPatient.html")

@app.route("/login", methods=["POST", "GET"])
def login():
	if request.method == "POST":
		session.permanent = True
		user = request.form["nm"]
		session["user"]= user

		found_user = users.query.filter_by(name=user).first()
		if found_user:
			session["email"] = found_user.email
		else:
			usr = users(user, "")
			db.session.add(usr)
			db.session.commit()

		flash("Login Successful")
		return redirect(url_for("user"))
	else: 
		if "user" in session:
			flash("Already logged in")
			return redirect(url_for("user"))
		return render_template("/login.html")

@app.route("/user", methods=["POST", "GET"])
def user():
	email = None
	if "user" in session:
		user = session["user"]

		if request.method == "POST":
			email = request.form["email"]
			session["email"] = email
			found_user = users.query.filter_by(name=user).first()
			found_user.email = email
			db.session.commit()
			flash("email was saved")
		else:
			if "email" in session:
				email = session["email"]

		return render_template("user.html", email=email)
	else:
		flash("You are not logged in")
		return redirect(url_for("login"))

@app.route("/logout")
def logout():
	session.pop("user", None)
	session.pop("email", None)
	flash(f"{user}, You've been logged out!", "info")
	return redirect(url_for("login"))

# @app.route('/')
# def hello():
#     name = request.args.get("name", "World")
#     return f'Hello, {escape(name)}!'



#db.createall()   #can use this to create the database if not created
#can also run python, then run "from app import db" and "db.create_all()"

# doctor_put_args = reqparse.RequestParser()
# doctor_put_args.add_argument("name", type=str, help="Name for doctor is required", required=True)
# doctor_put_args.add_argument("specialization", type=str, help="Specialization type of the doctor", required=False)

# patient_put_args = reqparse.RequestParser()
# patient_put_args.add_argument("name", type=str, help="Name for patient is required", required=True)
# patient_put_args.add_argument("email", type=str, help="Email for the patient", required=False)
# patient_put_args.add_argument("family_doctor", type=int, help="Family doctor of the patient", required=False)

# doctor_resource_fields = {
# 	'ssn': fields.Integer,
# 	'name': fields.String,
# 	'specialization': fields.String
# }

# patient_resource_fields = {
# 	'pid': fields.Integer,
# 	'name': fields.String,
# 	'email': fields.String,
# 	'family_doctor': fields.Integer
# }

# class Doctor(Resource):
# 	@marshal_with(doctor_resource_fields) #return the result and then serialize into json data base on the resource fields
# 	def get(self, doc_ssn): #override what happens when a get request is sent to this resource
# 		result = DoctorModel.query.filter_by(ssn=doc_ssn).all()
# 		if not result: 
# 			abort(404, message="Counldn't find doctor with this SSN")
# 		return result

# 	@marshal_with(doctor_resource_fields)
# 	def put(self, doc_ssn):
# 		args = doctor_put_args.parse_args()
# 		result = DoctorModel.query.filter_by(ssn=doc_ssn).first()
# 		if result: #if the doctor aleready exists in db
# 			abort(409, message="Doctor with this SSN already exists in the database")

# 		doctor = DoctorModel(ssn=doc_ssn, name=args['name'], specialization=args['specialization'])
# 		db.session.add(doctor)
# 		db.session.commit()
# 		return doctor, 201

# class Patient(Resource):
# 	@marshal_with(patient_resource_fields) #return the result and then serialize into json data base on the resource fields
# 	def get(self, pat_id): #override what happens when a get request is sent to this resource
# 		result = PatientModel.query.filter_by(pid=pat_id).all()
# 		if not result: 
# 			abort(404, message="Counldn't find patient with this PID")
# 		return result

# 	@marshal_with(patient_resource_fields)
# 	def put(self, pat_id):
# 		args = patient_put_args.parse_args()
# 		result = PatientModel.query.filter_by(pid=pat_id).first()
# 		if result: #if the patient aleready exists in db
# 			abort(409, message="Partient with this PID already exists in the database")

# 		patient = PatientModel(pid=pat_id, name=args['name'], email=args['email'], family_doctor=args['family_doctor'])
# 		db.session.add(patient)
# 		db.session.commit()
# 		return patient, 201

# api.add_resource(Doctor, "/doctor/<int:doc_ssn>")
# api.add_resource(Patient, "/patient/<int:pid>")




if __name__ == "__main__":
	# with app.app_context():
		#db.create_all() #Should only do this ONCE!!! otherwise it'll erase previous stored data
	app.run(debug=True)    #Disable debug mode when not in development stage
	app.run(host='0.0.0.0', port=80)
