from __main__ import app
from flask import Flask, request, session,redirect
import os
# api
import sys; sys.path.append(".."); from user import tokenapi

@app.route("/api/login", methods=['POST'])
def test():
    tokenapi.generateNewToken('user/tokens/')
    token = request.form['text']
    if token:
        if token+'.json' in tokenapi.getAllFreeTokens('user/tokens'):
            session['token'] = token
            return redirect("/")
        else:
            return "False"
    return " "