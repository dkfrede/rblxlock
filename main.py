# - Import flask - #
from flask import Flask, render_template,request,session,redirect
from flask_session import Session

# - Make app - #
app = Flask(__name__, template_folder ='html')

# - Api - #
from functions import login
from functions import redirectdis
from functions import upload
import api
from util.logs import log
from user import tokenapi

# - Setup session - #
app.config["SESSION_PERMANENT"] = True
app.config["SESSION_TYPE"] = "filesystem"
# - Final session setup - #
Session(app)

@app.route("/")
@app.route("/home")
def home():
    if session.get("token") and session['token'] != None:
        if session.get("token")+'.json' in tokenapi.getAllFreeTokens('user/tokens/'):
            return render_template("home.html", logged=True, token=session['token'])
    log("Visitor", "User with IP **"+request.remote_addr+"** loaded the home page!",True)
    return render_template("home.html")
@app.route("/login")
def login():
    log("Visitor", "User with IP **"+request.remote_addr+"** loaded the login page!",True)
    return render_template("login.html")
@app.route("/upload")
def upload():
    if session.get("token") and session['token'] != None:
        if session.get("token")+'.json' in tokenapi.getAllFreeTokens('user/tokens/'):
            log("Visitor", "User with IP **"+request.remote_addr+"** loaded the upload page!",True)
            return render_template("upload.html")
    log("Tried", "User with IP **"+request.remote_addr+"** tried loading upload without access!")
    return "no access"
@app.route("/scripts")
def scripts():
    return render_template("scripts.html",scripts=api.getScripts(session['token']),len=len(api.getScripts(session['token'])))
@app.route("/dashboard")
def dashboard():
    if session.get("token") and session['token'] != None:
        if session.get("token")+'.json' in tokenapi.getAllFreeTokens('user/tokens/'):
            return render_template("dashboard.html")
    return redirect("/login")
@app.route("/download")
def download():
    if session.get("token") and session['token'] != None:
        if session.get("token")+'.json' in tokenapi.getAllFreeTokens('user/tokens/'):
            log("Downloader", "User with IP **"+request.remote_addr+"** downloaded our resource!",True)
            return api.download()
    return "No access"
@app.route("/account")
def account():
    return render_template("account.html", token=session['token'], ip=request.remote_addr, admin=tokenapi.isTokenAnAdmin(session['token'],'user/tokens/'))
@app.route("/logout")
def logout():
    if session.get("token"):
        session["token"] = None
    log("Visitor", "User with IP **"+request.remote_addr+"** logged out!",True)
    return redirect("/")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)