from flask import Flask, render_template,request,session
from flask_session import Session

app = Flask(__name__, template_folder ='html')

# - Api - #
from functions import login
from functions import redirectdis
import api
from util.logs import log
app.config["SESSION_PERMANENT"] = True
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
@app.route("/")
@app.route("/home")
def home():
    if session.get("token") and session['token'] != None:
        return "login: "+session['token']
    log("Visitor", "User with IP **"+request.remote_addr+"** loaded the home page!",True)
    return render_template("home.html")
@app.route("/login")
def login():
    log("Visitor", "User with IP **"+request.remote_addr+"** loaded the login page!",True)
    return render_template("login.html")
@app.route("/upload")
def upload():
    log("Visitor", "User with IP **"+request.remote_addr+"** loaded the upload page!",True)
    return render_template("upload.html")
@app.route("/download")
def download():
    log("Downloader", "User with IP **"+request.remote_addr+"** downloaded our resource!",True)
    return api.download()
@app.route("/scripts")
def scripts():

    return render_template("scripts.html")
@app.route("/whitelist")
def whitelist():
    return render_template("whitelist.html")
@app.route("/account")
def account():
    return render_template("account.html")
@app.route("/logout")
def logout():
    if session.get("token"):
        session["token"] = None
    log("Visitor", "User with IP **"+request.remote_addr+"** loaded the logout page!",True)
    return "logged out"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)