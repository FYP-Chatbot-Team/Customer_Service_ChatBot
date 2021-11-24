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

    msgs.append({"image":{"imageUri":"https://photos.google.com/u/2/photo/AF1QipMdeY4Qns7fr5nNU7gQb-o0VUKyPxNpErXdEj5Z"}})

    msgs.append({"image":{"imageUri":"https://photos.google.com/u/2/photo/AF1QipPaB2JmxpKcBkw-mQCwyaammYDL5XkwTpIwH8kg"}})

    msgs.append({"image":{"imageUri":"https://photos.google.com/u/2/photo/AF1QipMy_NJ9fVLBH9FuT7WWeMnQ-t35AEghijiZAV_s"}})

    msgs.append({"image":{"imageUri":"https://photos.google.com/u/2/photo/AF1QipNTThKperT8A6huo5wuCYvVB3706zBX_nhKIkEz"}})

    msgs.append({"image":{"imageUri":"https://photos.google.com/u/2/photo/AF1QipPLd_JnZnf-BgH2AoqMydkN3ueGPtkm075sEvvu"}})

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