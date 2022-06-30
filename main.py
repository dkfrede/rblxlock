from flask import Flask, render_template,request,session
app = Flask(__name__, template_folder ='html')
from functions import login
import api
from util.logs import log

@app.route("/")
@app.route("/home")
def home():

    if 'token' in session:
        return "login: "+session['username']

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
    log("Visitor", "User with IP **"+request.remote_addr+"** loaded the logout page!",True)
    return render_template("logout.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)