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

 #What to do for non-compoundable 26N LOA function
def What_to_do_for_noncompoundable_26N_LOA(data):
    reply = {}
    msgs = []

    ######SQL######
    #conn = database.create_connection()
    #msgs.append({"text": {"text":["What to do for non-compoundable 26N LOA? : "]}})
    #cur = conn.cursor()
    #cur.execute("SELECT response_1,response_2 FROM question where question_id = 12")
    #rows = cur.fetchall()
    #for row in rows:
    #     for response in row:
    #          msgs.append({"text": {"text":[response]}})

    ######Firebase Update Topic Count######
    ref = db.reference("/Topics/")
    rows = ref.get()
    for key, val in rows.items():
        if(key == "Process for LOA"):
            count_firebase = val["Count"]
            count = int(count_firebase) + 1
            ref.child(key).update({"Count": count})

     ######Firebase######
    ref = db.reference("/Questions/Qn12/")
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


#What to bring for WOA execution function
def What_to_bring_for_WOA_execution(data):
    reply = {}
    msgs = []

    ######SQL######
    #conn = database.create_connection()
    #msgs.append({"text": {"text":["What to bring for WOA execution ? : "]}})
    #cur = conn.cursor()
    #cur.execute("SELECT response_1 FROM question where question_id = 13")
    #rows = cur.fetchall()
    #for row in rows:
    #     for response in row:
    #          msgs.append({"text": {"text":[response]}})

     ######Firebase Update Topic Count######
    ref = db.reference("/Topics/")
    rows = ref.get()
    for key, val in rows.items():
        if(key == "Process for LOA"):
            count_firebase = val["Count"]
            count = int(count_firebase) + 1
            ref.child(key).update({"Count": count})

     ######Firebase######
    ref = db.reference("/Questions/Qn13/")
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