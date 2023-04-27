from IVA_MCU_API import changeProfile
import hmac
import hashlib
import base64
import timestamp
from datetime import datetime as datetime


# header = {"alg": "HS256", "typ": "JWT"}
# payload = {"sub": "390662e6-6297-4b71-a7a2-874a98906458", "iat": 20}
# appSecret = "cae84c03f13a4e209c0c6f1cef88ef507e5312c9dcf2485ea02dbb8a8c4b4934"
# header_b = changeProfile.data_encoder(header).encode()
# payload_b = changeProfile.data_encoder(payload).encode()
# # print(str(header))
# # print(base64.urlsafe_b64encode((header_b)))
# # print(base64.urlsafe_b64encode((payload_b)))
#
# b_app_secret = str(appSecret).encode('utf-8')
# print(str(base64.urlsafe_b64encode(header_b)) + "." + str(base64.urlsafe_b64encode(payload_b)))
# sign_b = hmac.HMAC(b_app_secret, (str(base64.urlsafe_b64encode(header_b)) + "." + str(base64.urlsafe_b64encode(payload_b))).encode(), digestmod='sha256').hexdigest()
# print(sign_b)


ts = int(round(datetime.now().timestamp()))
def crate_token(app_id, app_secret):
    header = {"alg": "HS256", "typ": "JWT"}
    payload = {"sub": app_id, "iat": ts}
    header_b = changeProfile.data_encoder(header).encode()
    payload_b = changeProfile.data_encoder(payload).encode()
    # print(str(header))
    # print(base64.urlsafe_b64encode((header_b)))
    # print(base64.urlsafe_b64encode((payload_b)))
    # sig = hmac.HMAC(str(DISQUS_SECRET_KEY).encode('utf-8'),  message + ' ' + timestamp, hashlib.sha1).hexdigest()
    b_app_secret = app_secret.encode('utf-8')
    # print(bytes(appSecret, 'utf-8'))
    # b_head_pay = (base64.urlsafe_b64encode(header_b) + "." + base64.urlsafe_b64encode(payload))
    # print(str(base64.urlsafe_b64encode(header_b)))
    # print(str(base64.urlsafe_b64encode(header_b)) + "." + str(base64.urlsafe_b64encode(payload_b)))
    sign_b = hmac.HMAC(b_app_secret, (str(base64.urlsafe_b64encode(header_b)) + "." + str(base64.urlsafe_b64encode(payload_b))).encode(), digestmod='sha256').hexdigest()
    # print(sign_b)
    # token = jwt.encode(
    #     headers=header,
    #     payload=payload,
    #     key=sign_b,
    #     algorithm="HS256")
    token = (base64.urlsafe_b64encode(header).base64.urlsafe_b64decode(payload).base64.urlsafe_b64decode(sign_b))

    return token


