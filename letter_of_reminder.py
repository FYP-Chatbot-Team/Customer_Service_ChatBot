from flask import Flask, request, jsonify, render_template
import datetime
import os
from google.cloud import dialogflow
import requests
import json
import mysql.connector

#Import from other module
import database

#Advise for compoundable 26N LOR function
def Advise_for_compoundable_26N_LOR(data):
    reply = {}
    msgs = []
    conn = database.create_connection()

    msgs.append({"text": {"text":["What to do for compoundable 26N LOR? : "]}})
    cur = conn.cursor()
    cur.execute("SELECT response_1,response_2 FROM question where question_id = 10")
    rows = cur.fetchall()
    for row in rows:
         for response in row:
              msgs.append({"text": {"text":[response]}})

       
    msgs.append( {
        "quickReplies": {
          "title": "Do you need anymore enquries ? 😊",
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
    conn = database.create_connection()

    msgs.append({"text": {"text":["Must offender go to court for settled C14 fine? : "]}})
    cur = conn.cursor()
    cur.execute("SELECT response_1 FROM question where question_id = 11")
    rows = cur.fetchall()
    for row in rows:
         for response in row:
              msgs.append({"text": {"text":[response]}})

       
    msgs.append( {
        "quickReplies": {
          "title": "Do you need anymore enquries ? 😊",
          "quickReplies": [
            "Yes",
            "No"
          ]
        }})    

    reply["fulfillmentMessages"] = msgs

    return reply


