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
    ref = db.reference("/Questions/")
    rows = ref.get()
    for key, val in rows.items():
        if(key == "Qn12"):
            count_firebase = val["Q_Count"]
            count = int(count_firebase) + 1
            ref.child(key).update({"Q_Count": count})
            question = val["Name"]
            msgs.append({"text": {"text":[question]}})
            ar = val["Response1"].split(" | ")
            for i in ar:
               msgs.append({"text": {"text":[i]}})

       
    msgs.append({"text": {"text":["Do you need anymore enquires ? 😊 "]}})  
    msgs.append({"text": {"text":["Type Yes or No "]}})     

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
    ref = db.reference("/Questions/")
    rows = ref.get()
    for key, val in rows.items():
        if(key == "Qn13"):
            count_firebase = val["Q_Count"]
            count = int(count_firebase) + 1
            ref.child(key).update({"Q_Count": count})
            question = val["Name"]
            msgs.append({"text": {"text":[question]}})
            ar = val["Response1"].split(" | ")
            for i in ar:
               msgs.append({"text": {"text":[i]}})
       
    msgs.append({"text": {"text":["Do you need anymore enquires ? 😊 "]}})  
    msgs.append({"text": {"text":["Type Yes or No "]}})     

    reply["fulfillmentMessages"] = msgs

    return reply