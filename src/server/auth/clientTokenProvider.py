# Random Data function
import random

# Hashing libraries
import base64
import hashlib

# OS commands (Setting Client Name/Token name) 
import os

#random print garbo
separator = "#------------------------------------------------#"

# Token Data
clientID = 'null'

def CreateClientID(clientName, clientOrgID) :
    #Client ID Creator
    print("Client ID Creator")
    print()

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
    print(separator)
    print()

    return(clientID)

#---------------------------------------------------------------------------------#

def CreateOauthToken(oAuthTokenRequestID, oAuthtokenAccountID) :
    #OauthTokenCreator
    print("oAuth Token Creator")
    print()

    #sha256'd RequestID
    oAuthTokenRequestID = hashlib.sha256(oAuthTokenRequestID.encode())
    oAuthTokenRequestID = oAuthTokenRequestID.hexdigest()
    print("oAuth Token Request : " + oAuthTokenRequestID)

    #sha256'd AccID
    oAuthtokenAccountID = hashlib.sha256(oAuthtokenAccountID.encode())
    oAuthtokenAccountID = oAuthtokenAccountID.hexdigest()
    print("oAuth Request AccountID : " + oAuthtokenAccountID)

    completeoAuthStr = hashlib.sha256(oAuthtokenAccountID.encode() + oAuthTokenRequestID.encode())
    completeoAuthStr = completeoAuthStr.hexdigest()
    print("Complete oAuth String : " + completeoAuthStr)
    print(separator)
    print()

    return(completeoAuthStr)
