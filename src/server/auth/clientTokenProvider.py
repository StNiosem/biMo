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

    # Hashed

CreateClientID("ClientTestName", "ClientTestOrg")
