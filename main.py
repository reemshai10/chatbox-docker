 #!/usr/bin/env python3
import json
from datetime import datetime
from flask import Flask
from flask import render_template,redirect,jsonify
from flask import request
import os
#import mysql.connector as conn
app = Flask(__name__)
dic1={}
CHAT_ROOM_DATA_PATH = 'rooms_data'
DATE_FORMAT = '[%Y-%m-%d %H:%M:%S]' 

#ef conn_db():
#return conn.connect(user=root,
#                    password=,
#                    host='**********',
#                    database=DATABASE
#                    )

#mycursor.execute("CREATE TABLE msg (username VARCHAR(255), msg VARCHAR(255))")


#help fun
def add_msg(room,username,msg):
    time=datetime.now().strftime(DATE_FORMAT)
    formatted_msg=f"{time} {username}: {msg}\n"
    with open(f"{CHAT_ROOM_DATA_PATH}/{room}","a")as f:
            f.write(formatted_msg)

    return True

def get_chat_msg(room):
    file_path=f"{CHAT_ROOM_DATA_PATH}/{room}"
    if not os.path.exists(file_path):
        return ""
    try:
        with open(file_path)as f:
            return f.read()        
    except:
        print ("something goes bad!")


@app.route("/",methods=['GET'])
@app.route("/<room>",methods=['GET'])
def room(room=1):
    return render_template("index.html")



@app.route("/api/chat/<room>",methods=['POST','GET'])
def add_data(room):
        if request.method == 'POST':
            if request.form["username"].strip() == "" and request.form["msg"].strip() == "" :
                return "status 200"
            if add_msg(room,request.form["username"],request.form["msg"]):

                return "OK"
        if request.method == 'GET':
            return get_chat_msg(room)
    

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)