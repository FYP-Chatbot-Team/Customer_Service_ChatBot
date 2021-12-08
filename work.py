from flask import Flask, request, jsonify, render_template
import datetime
import os
from google.cloud import dialogflow
import requests
import json
import mysql.connector

#Import from other module
import database

#Non-urgent SFA cases function
def Nonurgent_SFA_cases(data):
    reply = {}
    msgs = []
    conn = database.create_connection()

    msgs.append({"text": {"text":["How to handle non-urgent SFA cases? : "]}})
    cur = conn.cursor()
    cur.execute("SELECT response_1 FROM question where question_id = 14")
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


#How to stop SFA rejecting my cases
def How_to_stop_SFA_rejecting_my_cases(data):
    reply = {}
    msgs = []
    conn = database.create_connection()

    msgs.append({"text": {"text":["How to ensure SFA accepts my case? : "]}})
    cur = conn.cursor()
    cur.execute("SELECT response_1,response_2,response_3 FROM question where question_id = 15")
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


#SFA in charge of
def SFA_in_charge_of(data):
    reply = {}
    msgs = []
    conn = database.create_connection()

    msgs.append({"text": {"text":["What is SFA in charge of? : "]}})
    cur = conn.cursor()
    cur.execute("SELECT response_1,response_2,response_3,response_4,response_5,response_6 FROM question where question_id = 16")
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