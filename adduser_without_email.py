from http.server import BaseHTTPRequestHandler,HTTPServer
import requests
import base64
import json
import hmac
import hashlib
import time
from datetime import datetime
import jwt

hostName = "localhost"
serverPort = 4444
url_api = "https://saas.vkurse.ru/api/rest/integration"
app_secret='513b4083ca494a22a9667916948139b3e8e4dee5f083437cbbd48011cbb77eb2'.encode()
app_id="33ba097d-7d29-472f-96b7-9641100415ee"


def current_time():
  curr_dt = datetime.now()
  timestamp = int(round(curr_dt.timestamp()))
  return timestamp

header_data = {
    "alg": "HS256",
    "typ": "JWT"
}
payload_data = {
    "sub": app_id,
    "iat": current_time()
}

def get_token():
  token = jwt.encode(
    headers=header_data,
    payload=payload_data,
    key=app_secret,
    algorithm='HS256'
  )
  auth = "Bearer "+token
  return auth

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        auth2 = str(get_token())
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.send_header("Authorization",auth2)
        self.send_header("user-agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)""Chrome/89.0.4389.72 Safari/537.36")
        self.end_headers()
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)''Chrome/89.0.4389.72 Safari/537.36','Content-type' : 'application/json; charset=utf-8','Authorization': auth2}
        params = {'limit': 0}
        r = requests.get(url_api+'/users',headers=headers,params=params)
        r_dict = r.json()
        data = r_dict['data']
        self.wfile.write(bytes("<html><head><title>https://pythonpool.com</title></head>", "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<ul>", "utf-8"))
        count = r_dict['totalCount']
        self.wfile.write(bytes("<p>Total users: "+ str(count)+" </p>", "utf-8"))
        number = 0
        for user in data:
          number += 1
          self.wfile.write(bytes("<li>", "utf-8"))
          self.wfile.write(bytes(str(number)+" "+user['name']+" "+user['profileId'], "utf-8"))
          self.wfile.write(bytes("</li>", "utf-8"))
        self.wfile.write(bytes("</ul>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))
 
if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print(f"Server started http://{hostName}:{serverPort}")
 
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
 
    webServer.server_close()
    print("Http server stopped.")
