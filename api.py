import requests
import json
import os
from flask import send_file
from util.logs import log
from user.tokenapi import getAllFreeTokens
Rblxwatermark = """--[[
██████╗░██████╗░██╗░░░░░██╗░░██╗██╗░░░░░░█████╗░░█████╗░██╗░░██╗
██╔══██╗██╔══██╗██║░░░░░╚██╗██╔╝██║░░░░░██╔══██╗██╔══██╗██║░██╔╝
██████╔╝██████╦╝██║░░░░░░╚███╔╝░██║░░░░░██║░░██║██║░░╚═╝█████═╝░
██╔══██╗██╔══██╗██║░░░░░░██╔██╗░██║░░░░░██║░░██║██║░░██╗██╔═██╗░
██║░░██║██████╦╝███████╗██╔╝╚██╗███████╗╚█████╔╝╚█████╔╝██║░╚██╗
╚═╝░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝╚══════╝░╚════╝░░╚════╝░╚═╝░░╚═╝
This file is generated by rblxlock.
You do not have access to this file, before our checks.
Trying to reverse-engineer your way to access the file, will give us logs, and will result in a ban.
--]]"""


def upload(data,token):
    data = Rblxwatermark+'\n'+ data
    
    print(getAllFreeTokens())
    if token+'.json' in getAllFreeTokens():

        dataJson = json.load(open("data.json"))
        if dataJson:
            id = dataJson["id"]
            if os.path.exists("files/"+str(id)+".lua"):
                print("File already exists.")
                return False

            dataFile = open("files/"+str(id)+".lua", "x"); dataFile = open("files/"+str(id)+".lua","r+",encoding="utf-8"); dataFile.write(data)
            
            dataJson["id"] += 1

            f = open("data.json","w"); f.close(); f = open("data.json","w"); f.write(json.dumps(dataJson)) # Clears all contents
        
            # Save data of file
            f = open("files/data/"+str(id)+".json","x"); f = f = open("files/data/"+str(id)+".json","r+")

            filedata = {}
            filedata['owner'] = token
            f.write(json.dumps(filedata))

            print("Upload completed")
            log("New file was uploaded!", "An new file was uploaded to rblxlock.\nToken: **"+token+"**\nFile ID: **"+str(id)+"**")
            return True
    else:
        log("A file was unsuccessfully uploaded", "User with the token **"+token+"** was declined uploading because the token was invalid")
def download():
    return send_file('resource.lua', as_attachment=True)
def getJsonData(id):
    return json.load(open("files/data/"+id+".json"))
def getOwnerOfScript(id):
    if id:
        if os.path.exists("files/data/"+id+".json"):
            j = getJsonData(id)
            return j["owner"]
        else:
            print("Cant find data file")
            return False
def getScripts(token):
    if token:
        # token check here (progress)
        files = os.listdir("files/data")
        scripts = []
        for i in files:
            id = i.rsplit(".")[0]
            if getOwnerOfScript(id) == token:
                scripts.append(id)
        return scripts
def getScriptById(id,watermark):
    if id:
        if os.path.exists("files/"+id+".lua"):
            data = open("files/"+id+".lua","r+",encoding="utf-8").read()
            if watermark == False:
                data = data.replace(Rblxwatermark+'\n',"")
            return data