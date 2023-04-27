from pprint import pprint
import requests
import hmac
import hashlib
import base64

header = { "alg": "HS256", "typ": "JWT"}
payload = {"sub": "390662e6-6297-4b71-a7a2-874a98906458", "iat": 20}
# signature = hmac(base64.encode(header) + "." + base64.encode(payload), "cae84c03f13a4e209c0c6f1cef88ef507e5312c9dcf2485ea02dbb8a8c4b4934")

# const_token = (base64.urlsafe_b64encode(header).base64.urlsafe_b64decode(payload).base64.urlsafe_b64decode(signature))

# res = requests.get('https://ivcs-demo.iva-tech.ru/api/rest/login', headers={'Authorization': f'Bearer {const_token}'}, json=body)

# print(const_token)
#
# for k,v in header.items():
#     k = k.encode()
#     v = v.encode()
#     d = {k:v}
# print(d)
# print(base64.urlsafe_b64encode(d))
header = { "alg": "HS256", "typ": "JWT"}
data_str_en = str(header)
print(base64.urlsafe_b64encode(data_str_en.encode()))

# print(base64.urlsafe_b64encode())