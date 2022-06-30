from flask import Flask, render_template,request,session,redirect
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
        return render_template("home.html", logged=True, token=session['token'])
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
@app.route("/dashboard")
def dashboard():
    if session.get("token") and session['token'] != None:
        return render_template("dashboard.html")
    return redirect("/login")
@app.route("/download")
def download():
    log("Downloader", "User with IP **"+request.remote_addr+"** downloaded our resource!",True)
    return api.download()
@app.route("/account")
def account():
    return render_template("account.html", token=session['token'], ip=request.remote_addr, admin=False)
@app.route("/logout")
def logout():
    if session.get("token"):
        session["token"] = None
    log("Visitor", "User with IP **"+request.remote_addr+"** logged out!",True)
    return redirect("/")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)