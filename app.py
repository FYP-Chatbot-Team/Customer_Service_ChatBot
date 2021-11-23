from flask import Flask, request, jsonify, render_template, g, session, url_for,redirect
import datetime
import os
from google.cloud import dialogflow
import requests
import json
import mysql.connector


#Import from other module
import fine_payment
import illegal_dumping
import letter_of_reminder

#Import from other module for log in system
import user
import database

users = []
users.append(user.User(id=1, username='admin', password='password123'))

app = Flask(__name__)
app.secret_key = 'FYPNEACHATBOTISTHEBEST12345'

#To check if web service is running
@app.route('/')
def index():
    return render_template('index.html')


###########Log In system for rating from users#######
@app.before_request
def before_request():
    g.user = None

    if 'user_id' in session:
        user = [x for x in users if x.id == session['user_id']][0]
        g.user = user

#To check if admin and password is correct 
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop('user_id', None)

        username = request.form['username']
        password = request.form['password']
        
        user = [x for x in users if x.username == username][0]
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('graph'))

        return redirect(url_for('login'))

    return render_template('login.html')



@app.route('/graph')
def graph():
    if not g.user:
        return redirect(url_for('login'))

    data = [
        ("1 star",3),
        ("2 star",1),
        ("3 star",10),
        ("4 star",5),
        ("5 star",12)
        ]

    labels = [row[0] for row in data]
    values = [row[1] for row in data]

    return render_template('graph.html', labels=labels , values=values)

############Dialogflow##################
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json(silent=True)   # get the incoming JSON structure
    action = data['queryResult']['action'] # get the action name associated with the matched intent

     #######Fine payment#########   
    if (action == 'how_to_pay_fine'):
        return how_to_pay_fine(data)

    if (action == 'how_to_appeal'):
        return how_to_appeal(data)

    if (action == 'missed_court_date'):
        return missed_court_date(data)

    if (action == 'court_attendance_status'):
        return court_attendance_status(data)

    
     ###########Illegal Dumping###############
    if (action == 'info_for_illegal_dumping'):
        return info_for_illegal_dumping(data)

    if (action == 'dumping_vs_waste'):
        return dumping_vs_waste(data)

    if (action == 'team_in_charge_of_bulky_waste'):
        return team_in_charge_of_bulky_waste(data)

    if (action == 'team_in_charge_of_illegal_dumping'):
        return team_in_charge_of_illegal_dumping(data)

    if (action == 'Characteristics_of_illegal_dumping'):
        return Characteristics_of_illegal_dumping(data)

     ###########Process for LOR###############
    if (action == 'Advise_for_compoundable_26N_LOR'):
       return Advise_for_compoundable_26N_LOR(data)

    if (action == 'Need_go_to_court_for_settled_C14_fine'):
        return Need_go_to_court_for_settled_C14_fine(data)




 
#######Fine payment#########   
#How to pay fine function
def how_to_pay_fine(data):
     reply = fine_payment.how_to_pay_fine(data) 
     return jsonify(reply)
    
#How to appeal function
def how_to_appeal(data):
     reply = fine_payment.how_to_appeal(data) 
     return jsonify(reply)

#Missed Court Date function
def missed_court_date(data):
     reply = fine_payment.missed_court_date(data) 
     return jsonify(reply)

#court_attendance_status function
def court_attendance_status(data):
     reply = fine_payment.court_attendance_status(data) 
     return jsonify(reply)


###########Illegal Dumping###############
#What information for illegal dumping function
def info_for_illegal_dumping(data):
     reply = illegal_dumping.info_for_illegal_dumping(data)
     return jsonify(reply)

#Illegal Dumping vs Bulky Waste
def dumping_vs_waste(data):
     reply =  illegal_dumping.dumping_vs_waste(data)
     return jsonify(reply)

 
 #Team in charge of bulky waste
def team_in_charge_of_bulky_waste(data):
     reply =  illegal_dumping.team_in_charge_of_bulky_waste(data)
     return jsonify(reply)

#Team in charge of illegal dumping
def team_in_charge_of_illegal_dumping(data):
     reply =  illegal_dumping.team_in_charge_of_illegal_dumping(data)
     return jsonify(reply)

#Characteristics of illegal dumping
def Characteristics_of_illegal_dumping(data):
     reply =  illegal_dumping.Characteristics_of_illegal_dumping(data)
     return jsonify(reply)


 ###########Process for LOR###############
#Need go to court for settled C14 fine
def Need_go_to_court_for_settled_C14_fine(data):
    reply =  letter_of_reminder.Need_go_to_court_for_settled_C14_fine(data)
    return jsonify(reply)

#Advise for compoundable 26N LOR
def Advise_for_compoundable_26N_LOR(data):
    reply =  letter_of_reminder.Advise_for_compoundable_26N_LOR(data)
    return jsonify(reply)


if __name__ == "__main__":
    app.run()

