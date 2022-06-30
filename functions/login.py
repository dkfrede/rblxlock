from __main__ import app
from flask import Flask, request
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
        else:
            return "False"
    return ""