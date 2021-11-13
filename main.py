from flask import Flask, request, jsonify, render_template
import datetime
import os
from google.cloud import dialogflow
import requests
import json
import mysql.connector


#Import from other module
import fine_payment
import database


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
 
#setup connection to mySQL database
database.create_connection()
       
def how_to_pay_fine(data):
     reply = fine_payment.how_to_pay_fine(data) #To test webhook connection
     return jsonify(reply)
    

if __name__ == "__main__":
    app.run()
