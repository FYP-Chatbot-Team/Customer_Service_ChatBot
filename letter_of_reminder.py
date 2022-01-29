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

#Advise for compoundable 26N LOR function
def Advise_for_compoundable_26N_LOR(data):
    reply = {}
    msgs = []

    ######SQL######
    #conn = database.create_connection()
    #msgs.append({"text": {"text":["What to do for compoundable 26N LOR? : "]}})
    #cur = conn.cursor()
    #cur.execute("SELECT response_1,response_2 FROM question where question_id = 10")
    #rows = cur.fetchall()
    #for row in rows:
    #     for response in row:
    #          msgs.append({"text": {"text":[response]}})

     ######Firebase Update Topic Count######
    ref = db.reference("/Topics/")
    rows = ref.get()
    for key, val in rows.items():
        if(key == "Process for LOR"):
            count_firebase = val["Count"]
            count = int(count_firebase) + 1
            ref.child(key).update({"Count": count})


    ######Firebase######
    ref = db.reference("/Questions/")
    rows = ref.get()
    for key, val in rows.items():
        if(key == "Qn10"):
            count_firebase = val["Q_Count"]
            count = int(count_firebase) + 1
            ref.child(key).update({"Q_Count": count})
            question = val["Name"]
            msgs.append({"text": {"text":[question]}})
            ar = val["Response1"].split(" | ")
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

#Must offender go to court for settled C14 fine function
def Need_go_to_court_for_settled_C14_fine(data):
    reply = {}
    msgs = []

    ######SQL######
    #conn = database.create_connection()
    #msgs.append({"text": {"text":["Must offender go to court for settled C14 fine? : "]}})
    #cur = conn.cursor()
    #cur.execute("SELECT response_1 FROM question where question_id = 11")
    #rows = cur.fetchall()
    #for row in rows:
    #     for response in row:
    #          msgs.append({"text": {"text":[response]}})

     ######Firebase Update Topic Count######
    ref = db.reference("/Topics/")
    rows = ref.get()
    for key, val in rows.items():
        if(key == "Process for LOR"):
            count_firebase = val["Count"]
            count = int(count_firebase) + 1
            ref.child(key).update({"Count": count})

     ######Firebase######
    ref = db.reference("/Questions/")
    rows = ref.get()
    for key, val in rows.items():
        if(key == "Qn11"):
            count_firebase = val["Q_Count"]
            count = int(count_firebase) + 1
            ref.child(key).update({"Q_Count": count})
            question = val["Name"]
            msgs.append({"text": {"text":[question]}})
            ar = val["Response1"].split(" | ")
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


