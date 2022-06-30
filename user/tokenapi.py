import os
import json
import random
words=list('abcdefghijklmnopqrstuvwxyz---1234567890')

def getAllTokens():
    return os.listdir("tokens")
def getAllUsedTokens():
    tokens=[]
    for i in getAllTokens():
        with open("tokens/"+i,'r') as f:
            j = json.loads(f.read())
            if j['used'] == True:
                tokens.append(i)
    return tokens
def getAllFreeTokens():
    tokens=getAllTokens()
    for i in getAllUsedTokens():
        tokens.remove(i)
    return tokens
def generateNewToken():
    found = False
    finalCode=''
    while found == False:
        code=''
        for i in range(20):
            code=code+random.choice(words)
        if code+'.json' not in getAllTokens():
            found = True
            finalCode=code
    # - Make file
    f=open("tokens/"+finalCode+".json","x"); f.close(); f=open("tokens/"+finalCode+".json","r+")
    j = {}
    j["used"] = False
    j["lastip"] = "127.0.0.1"
    f.write(json.dumps(j))
    return finalCode
def removeToken(token):
    if token:
        if token+'.json' in getAllTokens():
            os.remove("tokens/"+token+".json")
            return True
    return False
print(getAllUsedTokens())
print(getAllFreeTokens())
print(generateNewToken())
print(removeToken("oxps26tt8n5t-rz4axsy"))