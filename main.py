from flask import Flask, render_template

app = Flask(__name__, template_folder ='html')

import api

@app.route("/")
@app.route("/home")
def home():
    #print(api.getScripts("MINSEJETOKEN"))
    #print(api.getScriptById("7",False))
    #api.upload("""local hey = true \nprint("hey")""","MINSEJETOKEN1")
    return render_template("home.html")
@app.route("/upload")
def upload():
    return render_template("upload.html")
@app.route("/download")
def download():
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
    return render_template("logout.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)