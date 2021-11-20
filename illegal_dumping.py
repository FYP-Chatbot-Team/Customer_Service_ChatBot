from flask import Flask, request, jsonify, render_template
import datetime
import os
from google.cloud import dialogflow
import requests
import json
import mysql.connector

#Import from other module
import database

#What information for illegal dumping function
def info_for_illegal_dumping(data):
    reply = {}
    msgs = []
    conn = database.create_connection()

    msgs.append({"text": {"text":["The following details should be obtain for illegal dumping : "]}})
    cur = conn.cursor()
    cur.execute("SELECT response_1,response_2,response_3,response_4,response_5,response_6,response_7,response_8 FROM question where question_id = 5")
    rows = cur.fetchall()
    for row in rows:
         for response in row:
              msgs.append({"text": {"text":[response]}})

    reply["fulfillmentMessages"] = msgs

    return reply

 # #Illegal Dumping vs Bulky Waste
def dumping_vs_waste(data):
    reply = {}
    msgs = []
    conn = database.create_connection()

    msgs.append({"text": {"text":[" #Illegal Dumping vs Bulky Waste : "]}})
    cur = conn.cursor()
    cur.execute("SELECT response_1,response_2,response_3,response_4,response_5,response_6 FROM question where question_id = 6")
    rows = cur.fetchall()
    for row in rows:
         for response in row:
              msgs.append({"text": {"text":[response]}})

    reply["fulfillmentMessages"] = msgs

    return reply