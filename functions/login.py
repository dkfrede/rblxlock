from __main__ import app
from re import S
from flask import Flask, request, session
import os
# api
import sys; sys.path.append(".."); from user import tokenapi

@app.route("/api/login", methods=['POST'])
def test():
    tokenapi.generateNewToken('user/tokens/')
    print(os.listdir(".."))
    token = request.form['text']
    if token:
        if token+'.json' in tokenapi.getAllFreeTokens('user/tokens'):
            return "True"

            session['token'] = token

        else:
            return "False"
    return ""