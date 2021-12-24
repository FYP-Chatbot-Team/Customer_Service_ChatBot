from flask import Flask, request, jsonify, render_template
import datetime
import os
from google.cloud import dialogflow
import requests
import json
import mysql.connector
import firebase_admin
from firebase_admin import db
#Import from other module
import database


#Connect to firebase database
database.create_firebase_connection()

#To test webhook connection
#How to pay fine function
def how_to_pay_fine(data):
    reply = {}
    msgs = []
    conn = database.create_connection()
    ######SQL######
    #msgs.append({"text": {"text":["You can pay using the following option : "]}})
    #cur = conn.cursor()
    #cur.execute("SELECT response_1,response_2,response_3,response_4 FROM question where question_id = 1")
    #rows = cur.fetchall()
    #for row in rows:
    #     for response in row:
    #          msgs.append({"text": {"text":[response]}})

    ######Firebase######
    ref = db.reference("/Questions/Qn1/")

    row = ref.get()
    for row in rows:
          for response in row:
                   msgs.append({"text": {"text":[response]}})
    msgs.append( {
        "quickReplies": {
          "title": "Do you need anymore enquires ? 😊",
          "quickReplies": [
            "Yes",
            "No"
          ]
        }})      
   
    reply["fulfillmentMessages"] = msgs

    return reply

#How to appeal function
def how_to_appeal(data):
    reply = {}
    msgs = []
    conn = database.create_connection()

    cur = conn.cursor()
    msgs.append({"text": {"text":["How to appeal ? Check the following scenario : "]}})
    cur.execute("SELECT response_1 FROM question where question_id = 2")
    rows = cur.fetchall()
    for row in rows:
          for response in row:
                   msgs.append({"text": {"text":[response]}})
       
    msgs.append( {
        "quickReplies": {
          "title": "Do you need anymore enquires ? 😊",
          "quickReplies": [
            "Yes",
            "No"
          ]
        }})    
                          
   
    reply["fulfillmentMessages"] = msgs

    return reply

#Missed Court Date function
def missed_court_date(data):
    reply = {}
    msgs = []
    conn = database.create_connection()

    cur = conn.cursor()
    msgs.append({"text": {"text":["Missed your court date ? Check the following scenario : "]}})
    cur.execute("SELECT response_1,response_2,response_3,response_4,response_5 FROM question where question_id = 3")
    rows = cur.fetchall()
    for row in rows:
          for response in row:
               msgs.append({"text": {"text":[response]}})
                                 
    msgs.append( {
        "quickReplies": {
          "title": "Do you need anymore enquires ? 😊",
          "quickReplies": [
            "Yes",
            "No"
          ]
        }})    

    reply["fulfillmentMessages"] = msgs

    return reply

#court_attendance_status function
def court_attendance_status(data):
    reply = {}
    msgs = []
    conn = database.create_connection()

    cur = conn.cursor()
    msgs.append({"text": {"text":["Court attendance required after fine payment ? Check the following scenario : "]}})
    cur.execute("SELECT response_1,response_2,response_3 FROM question where question_id = 4")
    rows = cur.fetchall()
    for row in rows:
            for response in row:                  
                   msgs.append({"text": {"text":[response]}})
    
       
    msgs.append( {
        "quickReplies": {
          "title": "Do you need anymore enquires ? 😊",
          "quickReplies": [
            "Yes",
            "No"
          ]
        }})    
   
    reply["fulfillmentMessages"] = msgs

    return reply

