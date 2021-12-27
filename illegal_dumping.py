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
cred_obj = firebase_admin.credentials.Certificate('nea-database-b96f8-firebase-adminsdk-mo1sn-a344a5de3b.json')
default_app = firebase_admin.initialize_app(cred_obj, {
'databaseURL':'https://nea-database-b96f8-default-rtdb.asia-southeast1.firebasedatabase.app/'})


#What information for illegal dumping function
def info_for_illegal_dumping(data):
    reply = {}
    msgs = []

    
    ######SQL######
    #conn = database.create_connection()
    #msgs.append({"text": {"text":["The following details should be obtain for illegal dumping : "]}})
    #cur = conn.cursor()
    #cur.execute("SELECT response_1,response_2,response_3,response_4,response_5,response_6,response_7,response_8 FROM question where question_id = 5")
    #rows = cur.fetchall()
    #for row in rows:
    #    for response in row:
    #          msgs.append({"text": {"text":[response]}})

     ######Firebase######
    ref = db.reference("/Questions/Qn5/")
    rows = ref.get()
    for key, val in rows.items():
             msgs.append({"text": {"text":[val]}}) 

       
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

#Illegal Dumping vs Bulky Waste function
def dumping_vs_waste(data):
    reply = {}
    msgs = []

    ######SQL######
    #conn = database.create_connection()
    #msgs.append({"text": {"text":["Illegal Dumping vs Bulky Waste : "]}})
    #cur = conn.cursor()
    #cur.execute("SELECT response_1,response_2,response_3,response_4,response_5,response_6 FROM question where question_id = 6")
    #rows = cur.fetchall()
    #for row in rows:
    #     for response in row:
    #          msgs.append({"text": {"text":[response]}})

    ######Firebase######
    ref = db.reference("/Questions/Qn6/")
    rows = ref.get()
    for key, val in rows.items():
             msgs.append({"text": {"text":[val]}}) 

       
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

#Team in charge of bulky_waste function
def team_in_charge_of_bulky_waste(data):
    reply = {}
    msgs = []

    ######SQL######
    #conn = database.create_connection()
    #msgs.append({"text": {"text":["Which team in charge of Bulky waste ? : "]}})
    #cur = conn.cursor()
    #cur.execute("SELECT response_1 FROM question where question_id = 7")
    #rows = cur.fetchall()
    #for row in rows:
    #     for response in row:
    #          msgs.append({"text": {"text":[response]}})

      ######Firebase######
    ref = db.reference("/Questions/Qn7/")
    rows = ref.get()
    for key, val in rows.items():
             msgs.append({"text": {"text":[val]}}) 


       
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

#Team in charge of Illegal Dumping function
def team_in_charge_of_illegal_dumping(data):
    reply = {}
    msgs = []

    ######SQL######
    #conn = database.create_connection()
    #msgs.append({"text": {"text":["Which team in charge of Illegal Dumping ? : "]}})
    #cur = conn.cursor()
    #cur.execute("SELECT  response_1,response_2,response_3,response_4,response_5 FROM question where question_id = 8")
    #rows = cur.fetchall()
    #for row in rows:
    #     for response in row:
    #          msgs.append({"image": {"imageUri":[response]}})

      ######Firebase######
    ref = db.reference("/Questions/Qn8/")
    rows = ref.get()
    for key, val in rows.items():
             msgs.append({"image": {"imageUri":[val]}}) 
       
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

#Characteristics of illegal dumping function
def Characteristics_of_illegal_dumping(data):
    reply = {}
    msgs = []

    ######SQL######
    #conn = database.create_connection()
    #msgs.append({"text": {"text":["What is the characteristic of illegal dumping ? Read below to know more : "]}})
    #cur = conn.cursor()
    #cur.execute("SELECT response_1,response_2,response_3 FROM question where question_id = 9")
    #rows = cur.fetchall()
    #for row in rows:
    #     for response in row:
    #          msgs.append({"text": {"text":[response]}})

        ######Firebase######
    ref = db.reference("/Questions/Qn9/")
    rows = ref.get()
    for key, val in rows.items():
             msgs.append({"text": {"text":[val]}})

       
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