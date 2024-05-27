# Random Data function
import random

# Hashing libraries
import base64
import hashlib

# OS commands (Setting Client Name/Token name) 
import os

# Token Data
clientID = 'null'

def CreateClientID(clientName, clientOrgID) :
    # Hashed Name
    clientHashedname = hashlib.md5(clientName.encode())
    clientHashedname = clientHashedname.hexdigest()
    print("Hash client name : " + clientHashedname)

    # Hashed OrgID
    clientHashedOrgID = hashlib.md5(clientOrgID.encode())
    clientHashedOrgID = clientHashedOrgID.hexdigest()
    print("Hashed OrgID : " + clientHashedOrgID)

    clientCompleteStr = clientHashedname + "-" + clientHashedOrgID
    clientCompleteStr = hashlib.md5(clientCompleteStr.encode())
    clientCompleteStr = clientCompleteStr.hexdigest()
    print("Complete Client String is : " + clientCompleteStr)

    clientID = clientName + "-" + clientOrgID + "-" + clientCompleteStr
    print("Complete Client ID is : " + clientID)

def CreateOauthToken() :
    #OauthTokenCreator
    print("asdasdasd")

CreateClientID("ClientTestName", "ClientTestOrg")
