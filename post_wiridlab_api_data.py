import requests
import json
import random

#Please Complete te next information for API connection
TOKEN_API_WIRIDLAB='<YOUR_AUTHENTICATION_WIRIDLAB_TOKEN>'
NODE_NAME_WIRIDLAB= '<NODE_NAME_WIRIDLAB_PLATFORM>'

#This is an example of how to build a package to send information in json format 
sensor = 'prueba_post'
node = 121
temperature = random.randrange(12, 30)
humidity = random.randrange(35, 50)

print("Enviando datos a la API.....")
jsonData = [{}]
jsonData[0]["SensorName"] = sensor
jsonData[0]["NodeNo"] = node
jsonData[0]["Variables"] = {}
jsonData[0]["Variables"]["HumidityMeasure"] = humidity
jsonData[0]["Variables"]["TemperatureMeasure"] = temperature
print (jsonData)

jsonData = json.dumps(jsonData, indent=4)    
headers = {"WIRID-LAB-AUTH-TOKEN": TOKEN_API_WIRIDLAB, "Content-Type": "application/json"}
info = requests.post("https://api.wiridlab.site/api/iot/devices/"+ NODE_NAME_WIRIDLAB.lower() , headers=headers, data=jsonData, timeout=None)
dataAPI = info.json()

if (info.status_code == 200):
    print ("  Request API")
    print(json.dumps(dataAPI, indent=4, sort_keys=True))
else:
    print ("Error sending information")
    print(json.dumps(dataAPI, indent=4, sort_keys=True))

