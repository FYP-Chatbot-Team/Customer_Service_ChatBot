from flask import Flask, request, jsonify, render_template
import datetime
import os
from google.cloud import dialogflow
import requests
import json
import mysql.connector

#Import from other module
import database

#setup connection to mySQL database
#function for DB connection
def create_connection():
    """ create a database connection to the mySQL database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = mydb = mysql.connector.connect(
    host="us-cdbr-east-04.cleardb.com",
    user="b33cdae453531f",
    password = "6a5d5f6d",
    database="heroku_edda316505ad5d8"
    )
        return conn
    except Error as e:
        print(e)
    return None


#How to pay fine function
def how_to_pay_fine(data):
    reply = {}
    msgs = []
    conn = create_connection()
    with conn:
          msgs.append({"text": {"text":["You can pay using the following option : "]}})
          cur = conn.cursor()
          cur.execute("SELECT response_1,response_2,response_3,response_4 FROM question where question_id = 1")
          rows = cur.fetchall()
          for row in rows:
                for response in row:
                   msgs.append({"text": {"text":[response]}})
                          
   
    reply["fulfillmentMessages"] = msgs

    return reply

#How to appeal function
def how_to_appeal(data):
    reply = {}
    msgs = []
    conn = create_connection()
    with conn:
          cur = conn.cursor()
          msgs.append({"text": {"text":["How to appeal ? Check the following scenario : "]}})
          cur.execute("SELECT response_1 FROM question where question_id = 2")
          rows = cur.fetchall()
          for row in rows:
                for response in row:
                   msgs.append({"text": {"text":[response]}})
                          
   
    reply["fulfillmentMessages"] = msgs

    return reply

#Missed Court Date function
def missed_court_date(data):
    reply = {}
    msgs = []
    conn = create_connection()
    with conn:
          cur = conn.cursor()
          msgs.append({"text": {"text":["Missed your court date ? Check the following scenario : "]}})
          cur.execute("SELECT response_1,response_2,response_3,response_4,response_5 FROM question where question_id = 3")
          rows = cur.fetchall()
          for row in rows:
                for response in row:
                   msgs.append({"text": {"text":[response]}})
                          
   
    reply["fulfillmentMessages"] = msgs

    return reply

#court_attendance_status function
def court_attendance_status(data):
    reply = {}
    msgs = []
    conn = create_connection()
    with conn:
          cur = conn.cursor()
          msgs.append({"text": {"text":["Court attendance required after fine payment ? Check the following scenario : "]}})
          cur.execute("SELECT response_1,response_2,response_3 FROM question where question_id = 4")
          rows = cur.fetchall()
          for row in rows:
                for response in row:                  
                   msgs.append({"text": {"text":[response]}})
                          
   
    reply["fulfillmentMessages"] = msgs

    return reply

