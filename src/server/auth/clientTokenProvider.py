# Random Data function
import random

# Hashing libraries
import base64
import hashlib

# OS commands (Setting Client Name/Token name) 
import os

# Token Data
token = 'null'
tokenRandomData = 'null'

# Client Name Data
clientName = 'null'

def ClientTokenGenerator() : 
    
    print(random.randint(0, 999999999999999999)) #from 0 to 999999999999999999 (18 times the number 9)

ClientTokenGenerator()