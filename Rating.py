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



###########Rating Function###############   
def rating_function(data):
    reply = {}
    msgs = []

    conn = database.create_connection()
    cur = conn.cursor()

    name = data['queryResult']['parameters']['name']
    comment = data['queryResult']['parameters']['comment']
    rating = data['queryResult']['parameters']['rating']

    #####SQL######
    #sql = "INSERT INTO customer_rating (customer_name, comment, rating) VALUES (%s, %s, %s)"
    #val = (name, comment, rating)
    #cur.execute(sql,val)
    #conn.commit()


    ######Firebase######
    ref = db.reference("/Customer Rating")
    ref.push().set({
        "Comment": comment,
        "Name": name,
        "Rating": rating
        }      
        )

    message = "Thank you " + name + " for giving us a rating."

    msgs.append({"text": {"text":[message]}})

    msgs.append({"image":{"imageUri":"https://www.prescience.com.au/wp-content/uploads/2018/01/Thank-You-Robot-04-e1515991584548.png"}})


    reply["fulfillmentMessages"] = msgs

    return reply