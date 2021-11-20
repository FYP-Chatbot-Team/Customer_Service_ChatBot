from flask import Flask, request, jsonify, render_template
import datetime
import os
from google.cloud import dialogflow
import requests
import json
import mysql.connector


#Import from other module
import fine_payment
import illegal_dumping


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json(silent=True)   # get the incoming JSON structure
    action = data['queryResult']['action'] # get the action name associated with the matched intent

    if (action == 'how_to_pay_fine'):
        return how_to_pay_fine(data)

    if (action == 'how_to_appeal'):
        return how_to_appeal(data)

    if (action == 'missed_court_date'):
        return missed_court_date(data)

    if (action == 'court_attendance_status'):
        return court_attendance_status(data)

    if (action == 'info_for_illegal_dumping'):
        return info_for_illegal_dumping(data)

    if (action == 'dumping_vs_waste'):
        return dumping_vs_waste(data)
 
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

if __name__ == "__main__":
    app.run()
