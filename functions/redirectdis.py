from __main__ import app
from flask import Flask, request, session,redirect
@app.route("/redirectdis", methods=['POST','GET'])
def redirectdis():
    return redirect("https://discord.gg/zntkqNwe")