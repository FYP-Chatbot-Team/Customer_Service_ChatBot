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

    msgs.append({"image":{"imageUri":"https://lh3.googleusercontent.com/cqs26hUeLR9fffNJuljYbhgjzdpbWMj7nF5yU0YzRbGvBIoLpwp1vgZrrk21Dcm5W0NjTrQkW-lUSDSCOoURRb24Mw4l34CFWIZrsgn3s3haovutIPbBkMXQCqOSpVrxuNgY6SUV87agpPo6hk9yri4cstnhgooSuNCEH20RuY11dHKC1-TZ4DC7d4n-fg0mJEt8PwJm1QwwVCAdWNzz7E2HtPNNJDacfT4Rd2lMidWKj4J3dFq-ZL83qKgYS53PDnKf2_XHXlgWaThJFcR0kieLUm80GOHxeFZMyuyxMRIUIXCEflxnOiaSjm_So_RzwQjey_pCynILYNieyOtbmL5O7FfU4E8breHYDInZIBs2JIBY9Or20nGOGRpe9gXSu2SShWoGEx8yx0DmuyOlGAPhIrHuootyMJxOxyuKiL-9IltaVPa_ZP8c1UXB3R3e2m5YxAQqWaQpLVmgnF3SGhbp9ouf-DrWlT3wGox4pIPQgbBJ_2DGon0M8icn5pGtRiXib-9eowGhuqfJEkWubGmyLOjhAPuz4mvz76MtVWvvKYU9bcT3qBY5iSynXqx_HfXwXBwaGC3iDJ0UHG5DLLq_iJImXz917I0R7zOfhOCFb7ccOdtxMSihqlAnkq15tQNVQbqefbvbC61USFL_yy7BX35H8DpEUTRCibwOJmssEzbiue1_1eGpEtPnTCjAokH-XOfbxTVfB8DkF0n48A=w1355-h559-no?authuser=2"}})

    msgs.append({"image":{"imageUri":"https://lh3.googleusercontent.com/0bYS-cG5t2TTkFg8o04Csfot6dfvBurBzswVpBjPmeHOQztHkoXRGa1rjRgP7fyCJ6R1zn1SmdDhmYO3oXJLCeKGcgbY5acQj1xv1jJk2Ujqh9-iUIiUSSS7aY5aeDXsQnOG-u8BLErdTYFYdrUT7Jr337nx-mzJDlNeIJxCVOXkpxeFWMm40LL5tEGspq8aRpWpXkHuYMbhPD8mkBxYVw08pDJx-7ZuXY2mvKjaD8nim1nrHZxaL4PwSVA8as0ZVUmz8SKsAx5cUDVuFO-GgBGJO8-2UIrTafiyA5myap5oaFR3iHM8ptyHWvD-wSiiwiusOXPqnMC8H6LRZvZsFOPn82wjC8fztBCkLSSQD9FVPFx-x_l2R9-DvenCEXGeujPIXZu5xal6us82yQCq_wmtaz-PxCJATlxoUmRG-qs9VSGVH8jZT3XALL3C9kIHwB5MoGl5ztz-XVvI_H7ghgFOWM3FDsQXD-PWSEIO4hJv2K6x23NNKZUJvV1X4XKDH_fXo6oNEEAxhT0w_v_LVnBjBtmchvC677At1Njb9r9x9m-rQPi9MKvUvGkKrOyILhb9js8Br4R8P8f1FKWNBn6Vg2VDuQESk1mjyvhkCPHPMKwakuN9Pjs8fTwmSHA_ubciNH4hD-_Q4VCjZySD4ORsmkc-r_DEHsLcX6zxgTsr8eY6cS_H_FTZ9A6y2Tf5137hofzmUt2nrqPjE9UKgg=w804-h705-no?authuser=2"}})

    msgs.append({"image":{"imageUri":"https://lh3.googleusercontent.com/ixr5lhxXpwmxpo_aKNijyav8hGHOYH2QrV4gtFn1v7UoYTq8sAMYa2KplEEF7INVGgztyWmN3Qe6VtLS1IJhCZ_XmD_V6XgMp5x1BNpbk71iLDxWa40MNthG6xX7n-YU4Y9QotpwVy0V2j81U0Ej3dc4I6b0pXpVNnjrVVN0sFyXAiSDLlSTeIh91cG-FELPDEY3tB9MRfsJCkVSNJ2oF54CeYXhi8hhC41sZU_CpvhPkjLu1J-WVVKXcCsN2u62cISfeopiG2r1xbJWkgTV_FGc9SS5-zVOox2p3SYeP1-b2hbzMhAF1wGX3GlRTVuN6ZwKeka3qPEWHCOUgGmc5902N_j4dpEiZTPn7BvWiInBjC5HpSMnO8XOGrWv3BSN2UCEZIodijfXT_10YfbYQGUO9-H0VZCPtRTh14dies-_BN8d8byZwNzcirdtd2K-yPbJK4Vl4jzzBK9VlnW2LUPwxMFd_7RgDGR5fNpbdNLmL7tpCIuhw7Sp3TGDVdUVJ2Tar6JKWS7wpJvCZPkrWkONgbMYu-zKTUC1nVhVonoTVu8o22z5B8jWfcu4GMHObgNkdgg1Mlpv2GpS_bGGjH6JQh6pwflecJt24BBSDlQxkyAFUWp7NfPNftMhxauxOJhPKeFI-OkKutMXuvOvNR10hONeZNE05GjLTnpdDT69eIDU-UTGtJ82QtfM7J_3Ilsf8hXNOwpZt-LTst3C7g=w578-h661-no?authuser=2"}})

    msgs.append({"image":{"imageUri":"https://lh3.googleusercontent.com/w_cVf1YWe7GEMtKq2aV8myIc-P7DtJM_J1-46s8IRllvwl3MGQDy43ME0lyB9zBBq23Df3efWuaQHPMIBBHhfgr0d-yGBckWf06-BzDTBUAlfuu037auj4UciILsB1EjAqEGOkxUSSvuM7ZILqmagvo3JET2AH8YSx6KZXoAbo6bVmxE-jx5UvNoWXV3pTtMexjKtheOQU6lHdWIGQi5_cENhq1QXt9GvpRRpxtYnp7jKH6qEpgUMc6u-jGNYuGpDu0TOOjflOYEZZFRMilTN05Icfw7YG8GN6971vUSwo1hA5sZWILfas-8zl36mkmFfPjnFD4boWqFzfuMP78h09JEnVkXufzo2WS7TMUXZrYMd1efPmwZbuKxEkjJ0lsD6DVqGEf8CyBojU4q3kyG8HyEpqV6AXTpD2boT7SU643BwLDDtrTCoxL1SbWF7aZlhkS-5tDY0yhpSNjmIgiOyVe0U7Gfvmn3moqbdfCloJ66OkE_ujMsWC5tfwveVEMXSZDg9-m8EczYqsaa3_LhiAix3FfQFtk765nGgq6OOWEWeXfA1dmnl6GJRqe1OiPiAe4YvPY0QIENq5zw1_Ospf7H7JdM7lYPfcM2oBErLVzPH2lDv_wiCY9UNTko0njIv9orX6bnuQA1qr7M3lHyY0-GMZLsMvY3fpk8me5UiyugKGnoot8nAzVS1lriCm0eT-ZQ9V4d9DcO2SkBtFCRVg=w575-h478-no?authuser=2"}})

    msgs.append({"image":{"imageUri":"https://lh3.googleusercontent.com/JEy6nbtGklrhThq8OubrXouJLc1r9FI-GOISExge4ZZjafCSLf1mck_upBOspeBQTXMXgd_iHE1xfCPyaHA2yV_bOsZZhukS7-44J-nHWKQRbfJRYeSTqw7PljJAL5wJckspccuN-WEDNqAW1ItdFACK_WbpCaaswNVGMJ56pDobrmD5Q8vgE6PJlbwfXBOIw5ugtmTPyTEbuLcnCGAhbAeAKnkmyxk10bft4JgfsDsO-FVjvSoSyWAmr8of9oYXFfdh8freBi82JJAvtKTiWHJeAVXlTlafLiY8FRabOT3BgQHuBnERMFW5Srb_l1zmrYyrU_J9HAclcU1yPjaf7b6LCPBLnZEAFPgDXxuqej-3AJVs_bJVnNk0Y3srK-YT-iMj3d84wsdBJsv3J23b_1GUMm-QEN3n2A-wa1F9-izVVYKbud1osnsJVJDxlNfNGNeKvc6cNX9nfpeEsQfK1fnDVVS9F_jovW3BjIfihNwKZtGzuOWetBbePbZ6sP8HLBzEAlZ-y5usCsoIcy5-UcgMDesZkNoLrTDgFR7eOEBVbJ_tDog2dc4sGFZqTaA_iOJTeNuR1JVFgUOUb_IDcXDI3B-GQ49pdLriTg9sqE7PFnp8Zv3P25W0Ovj7Qi4p7nLAwQ8j3kzhWiDTqluczKHHtC92stgWkEDybLidJqC3QFFkKEUleGIii-LLz2LIvYqTDC7_MUNKG7wRUw7m0g=w581-h356-no?authuser=2"}})

       
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