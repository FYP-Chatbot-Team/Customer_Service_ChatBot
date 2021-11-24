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

    msgs.append({"text": {"text":["Do you need anymore enquries ? 😊"]}})

    reply["fulfillmentMessages"] = msgs

    return reply

#Illegal Dumping vs Bulky Waste function
def dumping_vs_waste(data):
    reply = {}
    msgs = []
    conn = database.create_connection()

    msgs.append({"text": {"text":["Illegal Dumping vs Bulky Waste : "]}})
    cur = conn.cursor()
    cur.execute("SELECT response_1,response_2,response_3,response_4,response_5,response_6 FROM question where question_id = 6")
    rows = cur.fetchall()
    for row in rows:
         for response in row:
              msgs.append({"text": {"text":[response]}})

    msgs.append({"text": {"text":["Do you need anymore enquries ? 😊"]}})

    reply["fulfillmentMessages"] = msgs

    return reply

#Team in charge of bulky_waste function
def team_in_charge_of_bulky_waste(data):
    reply = {}
    msgs = []
    conn = database.create_connection()

    msgs.append({"text": {"text":["Which team in charge of Bulky waste ? : "]}})
    cur = conn.cursor()
    cur.execute("SELECT response_1 FROM question where question_id = 7")
    rows = cur.fetchall()
    for row in rows:
         for response in row:
              msgs.append({"text": {"text":[response]}})

    msgs.append({"text": {"text":["Do you need anymore enquries ? 😊"]}})


    reply["fulfillmentMessages"] = msgs

    return reply

#Team in charge of Illegal Dumping function
def team_in_charge_of_illegal_dumping(data):
    reply = {}
    msgs = []
    conn = database.create_connection()

    msgs.append({"text": {"text":["Which team in charge of Illegal Dumping ? : "]}})
    cur = conn.cursor()
    cur.execute("SELECT response_1 FROM question where question_id = 8")
    rows = cur.fetchall()
    for row in rows:
         for response in row:
              msgs.append({"text": {"text":[response]}})

    msgs.append({"image":{"imageuri":"https://www.nea.gov.sg/images/default-source/about-us/nea-logo.png"}})

    msgs.append({"text": {"text":["Do you need anymore enquries ? 😊"]}})

    reply["fulfillmentMessages"] = msgs

    return reply

#Characteristics of illegal dumping function
def Characteristics_of_illegal_dumping(data):
    reply = {}
    msgs = []
    conn = database.create_connection()

    msgs.append({"text": {"text":["What is the characteristic of illegal dumping ? Read below to know more : "]}})
    cur = conn.cursor()
    cur.execute("SELECT response_1,response_2,response_3 FROM question where question_id = 9")
    rows = cur.fetchall()
    for row in rows:
         for response in row:
              msgs.append({"text": {"text":[response]}})

    msgs.append({"text": {"text":["Do you need anymore enquries ? 😊"]}})

    reply["fulfillmentMessages"] = msgs

    return reply