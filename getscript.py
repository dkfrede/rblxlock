from __main__ import app
from flask import Flask, request, session,redirect
import sys; sys.path.append(".."); from api import getJsonData, getScriptById

@app.route("/api/getscript/<id>", methods=['GET'])
def getscript(id):
    password = request.headers.get('Password')
    placeid = request.headers.get('Roblox-Id')
    ps=False
    place=False
    data = getJsonData(id)
    correctPassword = data['password']
    correctPlaceID = data['placeid']
    # Checks
    data = getJsonData(id)
    if correctPassword != "":
        ps = True
    if correctPlaceID != "":
        place = True
    if ps == True and password != correctPassword:
        return "print('Unathorized')"
    if place == True and placeid != correctPlaceID:
        return "print('Unathorized')"
    return getScriptById(id,True)