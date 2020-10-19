import requests
import json

#Please Complete te next information for API connection
TOKEN_API_WIRIDLAB='<YOUR_AUTHENTICATION_WIRIDLAB_TOKEN>'
NODE_NAME_WIRIDLAB= '<NODE_NAME_WIRIDLAB_PLATFORM>'

headers = {"WIRID-LAB-AUTH-TOKEN": TOKEN_API_WIRIDLAB, "Content-Type": "application/json"}
response = requests.get("https://api.wiridlab.site/api/iot/devices/"+ NODE_NAME_WIRIDLAB.lower() , headers=headers)
dataAPI = response.json()

print (json.dumps(dataAPI))