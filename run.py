#coding=utf-8
from flask import Flask, request,render_template, redirect, url_for, jsonify
from flask_cors import CORS
from OpenSSL import SSL
import os
import json
# connecting ot service api whatspie
import requests
# from flask_api import FlaskAPI, status, exception


my_awesome_app = Flask(__name__)
my_awesome_app.config.from_json("setting.json")

CORS(my_awesome_app)


@my_awesome_app.route('/', methods=['POST','GET'])
def index():
	
	if request.method == 'GET':
			return "masuk"

	if request.method == 'POST':
            print(request.get_json())
            # Inisialisasi Webservice
            url 	 = my_awesome_app.config['PROVIDER']['CHATAPI']['URL']
            instance = my_awesome_app.config['PROVIDER']['CHATAPI']['INSTANCE']
            token 	 = my_awesome_app.config['PROVIDER']['CHATAPI']['TOKEN']

            wa = url +"/"+ instance +"/sendMessage?token=" +token
            
            #  Hook Target Dan Pesan Yang Dikirim
            # try:
            #     data = request.get_json()['messages'][0]
            # except:
            #     data = request.get_json()
            
            
            # #  Selcet Target Dan Pesan Dengan BotReply
            # target = data["chatId"].split("@")[0]
            # message = getBotReply(str(data["body"]).replace("*",""))

            
            # # SendMessage Ke ChatApi
            # if data['fromMe'] == False:
            #     r = requests.post(wa, data = {"phone": target,"body": message})
            return '{"type": "chat","body": "Mohon tunggu sebentar ya 🤖"}'

if __name__ == '__main__':
    my_awesome_app.run(debug=True)
