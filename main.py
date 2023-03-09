import os
import sys
import json

pullAllVars = os.environ.get()

try:
    print("Pulling all environment variables")
    print(pullAllVars)
except Exception as e:
    print("Error: ", e)
