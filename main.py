from flask import Flask, render_template
from api import getScripts

app = Flask(__name__, template_folder ='html')

@app.route("/")
@app.route("/home")
def home():
    print(getScripts("test"))
    return render_template("home.html")
@app.route("/upload")
def upload():
    return render_template("upload.html")
@app.route("/download")
def download():
    return render_template("download.html")
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
    return render_template("logout.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)