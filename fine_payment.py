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
database.create_connection()

#To test webhook connection
def how_to_pay_fine(data):
    reply = {}
    msgs = []

    msgs.append({"text": {"text":["You can pay using the following option : "]}})
    msgs.append({"text": {"text":["1. AXS Stations, E-Station, M-Station g"]}})
    msgs.append({"text": {"text":["2. All Post Officers (over the counter)"]}})
    msgs.append({"text": {"text":["3. SAM Kiosks, Mobile App, Web "]}})
    msgs.append({"text": {"text":["4. CSC Counter (Last Resort)"]}})
    reply["fulfillmentMessages"] = msgs

    return reply
