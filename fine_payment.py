from flask import Flask, request, jsonify, render_template
import datetime
import os
from google.cloud import dialogflow
import requests
import json
import mysql.connector
from firebase_admin import db
#Import from other module
import database


#To test webhook connection
#How to pay fine function
def how_to_pay_fine(data):
    reply = {}
    msgs = []
    ######SQL######
    #conn = database.create_connection()
    #msgs.append({"text": {"text":["You can pay using the following option : "]}})
    #cur = conn.cursor()
    #cur.execute("SELECT response_1,response_2,response_3,response_4 FROM question where question_id = 1")
    #rows = cur.fetchall()
    #for row in rows:
    #     for response in row:
    #          msgs.append({"text": {"text":[response]}})

    ######Firebase Update Topic Count######
    ref = db.reference("/Topics/Fine Payment/")
    rows = ref.get()
    for key, val in rows.items():
        if(key == "Count"):
            count = int(val) + 1
            ref.child("Fine Payment").update({"Count":count})

    ######Firebase######
    ref = db.reference("/Questions/Qn1/")
    rows = ref.get()
    for key, val in rows.items():
        ar = val.split(" | ")
        for i in ar:
            msgs.append({"text": {"text":[i]}})
            
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
    ######SQL######
    #conn = database.create_connection()
    #cur = conn.cursor()
    #msgs.append({"text": {"text":["How to appeal ? Check the following scenario : "]}})
    #cur.execute("SELECT response_1 FROM question where question_id = 2")
    #rows = cur.fetchall()
    #for row in rows:
    #      for response in row:
    #               msgs.append({"text": {"text":[response]}})

     ######Firebase Update Topic Count######
    ref = db.reference("/Topics/Fine Payment/")
    rows = ref.get()
    for key, val in rows.items():
        if(key == "Count"):
            count = int(val) + 1
            ref.child("Fine Payment").update({"Count":count})

    ######Firebase######
    ref = db.reference("/Questions/Qn2/")
    rows = ref.get()
    for key, val in rows.items():
        ar = val.split(" | ")
        for i in ar:
            msgs.append({"text": {"text":[i]}})
       
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

    ######SQL######
    #conn = database.create_connection()
    #cur = conn.cursor()
    #msgs.append({"text": {"text":["Missed your court date ? Check the following scenario : "]}})
    #cur.execute("SELECT response_1,response_2,response_3,response_4,response_5 FROM question where question_id = 3")
    #rows = cur.fetchall()
    #for row in rows:
    #      for response in row:
    #           msgs.append({"text": {"text":[response]}})

     ######Firebase Update Topic Count######
    ref = db.reference("/Topics/Fine Payment/")
    rows = ref.get()
    for key, val in rows.items():
        if(key == "Count"):
            count = int(val) + 1
            ref.child("Fine Payment").update({"Count":count})

    ######Firebase######
    ref = db.reference("/Questions/Qn3/")
    rows = ref.get()
    for key, val in rows.items():
        ar = val.split(" | ")
        for i in ar:
            msgs.append({"text": {"text":[i]}})
       
                                 
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

    ######SQL######
    #conn = database.create_connection()
    #cur = conn.cursor()
    #msgs.append({"text": {"text":["Court attendance required after fine payment ? Check the following scenario : "]}})
    #cur.execute("SELECT response_1,response_2,response_3 FROM question where question_id = 4")
    #rows = cur.fetchall()
    #for row in rows:
    #        for response in row:                  
    #               msgs.append({"text": {"text":[response]}})

     ######Firebase Update Topic Count######
    ref = db.reference("/Topics/Fine Payment/")
    rows = ref.get()
    for key, val in rows.items():
        if(key == "Count"):
            count = int(val) + 1
            ref.child("Fine Payment").update({"Count":count})
    
     ######Firebase######
    ref = db.reference("/Questions/Qn4/")
    rows = ref.get()
    for key, val in rows.items():
        ar = val.split(" | ")
        for i in ar:
            msgs.append({"text": {"text":[i]}})
    
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

