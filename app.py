from flask import Flask, request, jsonify, render_template, g, session, url_for,redirect
import datetime
import os
from google.cloud import dialogflow
import requests
import json
import mysql.connector
import firebase_admin
from firebase_admin import db

#Import from other module
import fine_payment
import illegal_dumping
import letter_of_reminder
import letter_of_advice
import work
import Rating


#Connect to firebase database
cred_obj = firebase_admin.credentials.Certificate('nea-database-b96f8-firebase-adminsdk-mo1sn-a344a5de3b.json')
default_app = firebase_admin.initialize_app(cred_obj, {
'databaseURL':'https://nea-database-b96f8-default-rtdb.asia-southeast1.firebasedatabase.app/'})

#Import from other module for log in system
import user
import database

#Set Up for Log In
users = []
ref = db.reference("/Access/")
rows = ref.get()
i = 0
id = 0
for key, val in rows.items():
    i+=1
    if(key == "Password"):
       password = val        
    else:
        username = val    
    if(i == 2):
        id+=1
        users.append(user.User(id=id, username=username, password=password))
         

app = Flask(__name__)
app.secret_key = 'FYPNEACHATBOTISTHEBEST12345'

#To check if web service is running
@app.route('/')
def index():
    return render_template('index.html')


###########Log In system for rating from users#######
@app.before_request
def before_request():
    g.user = None

    if 'user_id' in session:
        user = [x for x in users if x.id == session['user_id']][0]
        g.user = user

#To check if admin and password is correct 
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop('user_id', None)

        username = request.form['username']
        password = request.form['password']
        
        try:
         user = [x for x in users if x.username == username][0]
        except:
           return redirect(url_for('login'))
        else:
            user = [x for x in users if x.username == username][0]
            if user and user.password == password:
                session['user_id'] = user.id
                return redirect(url_for('graph'))

            return redirect(url_for('login'))

       

    return render_template('login.html')


#Logout 
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))



#Graph Page
@app.route('/graph')
def graph():
    if not g.user:
        return redirect(url_for('login'))

    

    #Rating Graph
    star1 = 0
    star2 = 0
    star3 = 0
    star4 = 0
    star5 = 0

    #####SQL###
    #conn = database.create_connection()
    #cur = conn.cursor()
    #cur.execute("SELECT customer_name,comment,rating FROM customer_rating")
    #rows = cur.fetchall()

    #####Firebase for customer rating#######
    ref = db.reference("/Customer_Rating/")
    rows = ref.get()

    for key, val in rows.items():
        for key2, i in val.items():
            if(key2 == "C_Rating"):
              if(i=="1"):
                  star1+=1
              elif(i=="2"):
                  star2+=1
              elif(i=="3"):
                  star3+=1
              elif(i=="4"):
                  star4+=1
              else:
                  star5+=1
             
    data = [
        ("1 star",star1),
        ("2 star",star2),
        ("3 star",star3),
        ("4 star",star4),
        ("5 star",star5)
        ]

    labels = [row[0] for row in data]
    values = [row[1] for row in data]

    #####Firebase for customer rating#######
    data = []
    ref = db.reference("/Topics/")
    rows = ref.get()
    for key, val in rows.items():
        id = key
        for key2, i in val.items():
            if(key2=="Count"):
                count = i
                data.append([id,count])

    labels1 = [row[0] for row in data]
    values1 = [row[1] for row in data]

    #####Firebase for top 5 Question from chatbot#######
    data = []
    ref = db.reference("/Questions/")
    rows = ref.order_by_child("Q_count").limit_to_first(5).get()
    for key, val in rows.items():
        id = val["Name"]
        count = val["Q_Count"]
        data.append([id,count])

    labels2 = [row[0] for row in data]
    values2 = [row[1] for row in data]

    return render_template('graph.html', labels=labels , values=values,labels1=labels1,values1=values1,labels2=labels2,values2=values2)


#Comment Page
@app.route('/comment')
def comment():
    if not g.user:
        return redirect(url_for('login'))
    
    ##SQL##
    #conn = database.create_connection()
    #cur = conn.cursor()
    #cur.execute("SELECT customer_name,comment,rating FROM customer_rating")
    #comment = cur.fetchall()

    ##Firebase##
    ref = db.reference("/Customer_Rating")
    comment = ref.get()

    return render_template('comment.html', comment = comment )


#NEA Webpage for Chatbot
@app.route('/webpage')
def webpage():
    return render_template('webpage.html')


############Dialogflow##################
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json(silent=True)   # get the incoming JSON structure
    action = data['queryResult']['action'] # get the action name associated with the matched intent

     #######Fine payment#########   
    if (action == 'how_to_pay_fine'):
        return how_to_pay_fine(data)

    if (action == 'how_to_appeal'):
        return how_to_appeal(data)

    if (action == 'missed_court_date'):
        return missed_court_date(data)

    if (action == 'court_attendance_status'):
        return court_attendance_status(data)

    
     ###########Illegal Dumping###############
    if (action == 'info_for_illegal_dumping'):
        return info_for_illegal_dumping(data)

    if (action == 'dumping_vs_waste'):
        return dumping_vs_waste(data)

    if (action == 'team_in_charge_of_bulky_waste'):
        return team_in_charge_of_bulky_waste(data)

    if (action == 'team_in_charge_of_illegal_dumping'):
        return team_in_charge_of_illegal_dumping(data)

    if (action == 'Characteristics_of_illegal_dumping'):
        return Characteristics_of_illegal_dumping(data)

     ###########Process for LOR###############
    if (action == 'Advise_for_compoundable_26N_LOR'):
       return Advise_for_compoundable_26N_LOR(data)

    if (action == 'Need_go_to_court_for_settled_C14_fine'):
        return Need_go_to_court_for_settled_C14_fine(data)


    ###########Process for LOA###############
    if (action == 'What_to_do_for_non-compoundable_26N_LOA'):
        return What_to_do_for_noncompoundable_26N_LOA(data)

    if (action == 'What_to_bring_for_WOA_execution'):
        return What_to_bring_for_WOA_execution(data)

    ###########Work Instruction for SFA###############   
    if (action == 'Non-urgent_SFA_cases'):
        return Nonurgent_SFA_cases(data)

    if (action == 'How_to_stop_SFA_rejecting_my_cases'):
        return How_to_stop_SFA_rejecting_my_cases(data)

    if (action == 'SFA_in_charge_of'):
        return SFA_in_charge_of(data)

    ###########Rating Function############### 
    if (action == 'rating_function'):
        return rating_function(data)

 
#######Fine payment#########   
#How to pay fine function
def how_to_pay_fine(data):
     reply = fine_payment.how_to_pay_fine(data) 
     return jsonify(reply)
    
#How to appeal function
def how_to_appeal(data):
     reply = fine_payment.how_to_appeal(data) 
     return jsonify(reply)

#Missed Court Date function
def missed_court_date(data):
     reply = fine_payment.missed_court_date(data) 
     return jsonify(reply)

#court_attendance_status function
def court_attendance_status(data):
     reply = fine_payment.court_attendance_status(data) 
     return jsonify(reply)


###########Illegal Dumping###############
#What information for illegal dumping function
def info_for_illegal_dumping(data):
     reply = illegal_dumping.info_for_illegal_dumping(data)
     return jsonify(reply)

#Illegal Dumping vs Bulky Waste
def dumping_vs_waste(data):
     reply =  illegal_dumping.dumping_vs_waste(data)
     return jsonify(reply)

 
 #Team in charge of bulky waste
def team_in_charge_of_bulky_waste(data):
     reply =  illegal_dumping.team_in_charge_of_bulky_waste(data)
     return jsonify(reply)

#Team in charge of illegal dumping
def team_in_charge_of_illegal_dumping(data):
     reply =  illegal_dumping.team_in_charge_of_illegal_dumping(data)
     return jsonify(reply)

#Characteristics of illegal dumping
def Characteristics_of_illegal_dumping(data):
     reply =  illegal_dumping.Characteristics_of_illegal_dumping(data)
     return jsonify(reply)


###########Process for LOR###############
#Need go to court for settled C14 fine
def Need_go_to_court_for_settled_C14_fine(data):
    reply =  letter_of_reminder.Need_go_to_court_for_settled_C14_fine(data)
    return jsonify(reply)

#Advise for compoundable 26N LOR
def Advise_for_compoundable_26N_LOR(data):
    reply =  letter_of_reminder.Advise_for_compoundable_26N_LOR(data)
    return jsonify(reply)

###########Process for LOA###############
 #What to do for non-compoundable 26N LOA
def What_to_do_for_noncompoundable_26N_LOA(data):
    reply =  letter_of_advice.What_to_do_for_noncompoundable_26N_LOA(data)
    return jsonify(reply)

#What to bring for WOA execution
def What_to_bring_for_WOA_execution(data):
    reply =  letter_of_advice.What_to_bring_for_WOA_execution(data)
    return jsonify(reply)

###########Work Instruction for SFA###############   
#Non-urgent SFA cases
def Nonurgent_SFA_cases(data):
    reply =  work.Nonurgent_SFA_cases(data)
    return jsonify(reply)

#How to stop SFA rejecting my cases
def How_to_stop_SFA_rejecting_my_cases(data):
    reply =  work.How_to_stop_SFA_rejecting_my_cases(data)
    return jsonify(reply)

#SFA in charge of
def SFA_in_charge_of(data):
    reply =  work.SFA_in_charge_of(data)
    return jsonify(reply)


###########Rating Function###############   
def rating_function(data):
    reply =  Rating.rating_function(data)
    return jsonify(reply)




if __name__ == "__main__":
    app.run()

