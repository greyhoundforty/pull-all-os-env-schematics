import os
import sys
import json

pullCeServicesVars = os.environ.get('CE_SERVICES')
pullCosVars = os.environ.get('CLOUD_OBJECT_STORAGE')
ceVarsType = type(pullCeServicesVars)

try:
    print("CE Vars Type: ", + str(ceVarsType))
    print(pullCeServicesVars)
    print
except Exception as e:
    print("Error: ", e)
