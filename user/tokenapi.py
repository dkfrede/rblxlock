import os
import json
import random
import sys; sys.path.append(".."); from util.logs import log
words=list('abcdefghijklmnopqrstuvwxyz---1234567890')
def getAllTokens(path):
    return os.listdir(path)
def getAllUsedTokens(path):
    tokens=[]
    for i in getAllTokens(path):
        with open("user/tokens/"+i,'r') as f:
            j = json.loads(f.read())
            if j['used'] == True:
                tokens.append(i)
    return tokens
def getAllFreeTokens(path):
    tokens=getAllTokens(path)
    for i in getAllUsedTokens(path):
        tokens.remove(i)
    return tokens
def generateNewToken(path,*log1):
    found = False
    finalCode=''
    while found == False:
        code=''
        for i in range(20):
            code=code+random.choice(words)
        if code+'.json' not in getAllTokens(path):
            found = True
            finalCode=code
    # - Make file
    f=open(path+finalCode+".json","x"); f.close(); f=open(path+finalCode+".json","r+")
    j = {}
    j["used"] = False
    j["lastip"] = "127.0.0.1"
    f.write(json.dumps(j))
    if log1 == None:
        log("Token created!", "A new token was generated.\nToken: **"+finalCode+"**")
    return finalCode
def generateMultiTokens(path,amount):
    tokens1=''
    for i in range(amount):
        token = generateNewToken(path,True)
        if tokens1 != '':
            tokens1=tokens1+'\n'+token
        else:
            tokens1=token
    log("Tokens created!","**"+str(amount)+"** tokens where created!\n"+tokens1)
    return tokens1
def removeToken(token):
    if token:
        if token+'.json' in getAllTokens(path):
            log("Token removed", "The token **"+token+"** was removed!")
            os.remove("user/tokens/"+token+".json")
            return True
    return False