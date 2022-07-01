from __main__ import app
from flask import Flask, request, session,redirect
import os
# api
import sys; sys.path.append(".."); import api

@app.route("/api/uploadfile", methods=['POST'])
def uploadfile():
    if request.method == 'POST':
        f = request.files['file']
        text = str(request.form['password'])
        text1 = str(request.form['robloxid'])
        api.upload(str(f.read(),'utf-8'),session['token'],'user/tokens/',text,text1)
        return redirect("/dashboard")