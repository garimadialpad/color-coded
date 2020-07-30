# importing the requests library 


import json
import requests 
  
# api-endpoint 
URL1 = "http://localhost:8086/_ah/login?email=test%40example.com&admin=True&action=Login&continue=http%3A%2F%2Flocalhost%3A8086%2F"
session = requests.Session()
response = session.get(URL1)
URL = "http://localhost:8086/api/querymachines"
  
# sending get request and saving the response as response object 
r = requests.get(url = URL, cookies = session.cookies.get_dict())
print r.text

  

  
