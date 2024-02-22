from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os
import boto
from config import *
from pymysql import connections

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employee.db'  # SQLite database file
db = SQLAlchemy(app)


bucket = custombucket
region = customregion
db_conn = connections.Connection(
    host = customhost,
    port=3306,
    user = customuser,
    password = custompass,
    db = customdb
)
class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    deparment = db.Column(db.Float, nullable=False)
    manager = db.Column(db.Integer, nullable=False)
   
    
# class FormData(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     email = db.Column(db.String(100), nullable=False)
#     id = db.Column(db.String(20), nullable=False)
#     deparment = db.Column(db.Float, nullable=False)
#     manager = db.Column(db.Integer, nullable=False)

@app.route("/", methods = ['GET', 'POST'])   
def index():
    return render_template('index.html')
    

# @app.route("/")   
# def index():
#     return render_template('login.html')
    
@app.route('/AddEmp', methods=['POST'])
def AddEmp():
    id=request.form['id'],
    name = request.form['name']
    email= request.form['email'],
    department=request.form['department'],
    manager=request.form['manager']
    
    inser_sql = " INSERT INTO employee values (%s %s %s %s %s)"
    curser = db_conn.cursor()
    
    curser.execute(inser_sql, (id, name, email, department , manager))
    db_conn.commit()
    
    


#     # Check if email is already registered
#     if Employee.query.filter_by(email=data['email']).first():
#         return jsonify({'error': 'Email already exists'}), 400


#     # Add user to the database
#     new_employee = Employee(email=data['email'], password=data['password'])
#     db.session.add(new_employee)
#     db.session.commit()


#     return jsonify({'message': 'Signup successful', 'user': {'email': new_employee.email}}), 201


# @app.route('/login', methods=['POST'])
# def login():
#     data = request.get_json()


#     # Find employee by email
#     employee = Employee.query.filter_by(email=data['email']).first()


#     if not employee or employee.password != data['password']:
#         return jsonify({'error': 'Invalid email or password'}), 401


#     return jsonify({'message': 'Login successful', 'user': {'email': employee.email}}), 200
# @app.route('/users', methods=['GET'])
# def get_users():
#     users = Employee.query.all()
#     user_data = [{'id': user.id, 'email': user.email} for user in users]
#     return jsonify(user_data)


# @app.route('/submit_form', methods=['POST'])
# def submit_form():
#     # Get form data from the request
#     form_data = request.json


#     # Create a new FormData object and save it to the database
#     new_form = FormData(fullname=form_data['fullname'],
#                         email=form_data['email'],
#                         phone=form_data['phone'],
#                         amount=form_data['amount'],
#                         terms=form_data['terms'])
#     db.session.add(new_form)
#     db.session.commit()


#     # Return a response
#     return jsonify({"message": "Form submitted successfully!"})


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug= True)



