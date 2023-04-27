import requests
from pprint import pprint
import configparser
import json



config = configparser.ConfigParser()
config.read('settings.ini')


class IvaApiClient:

    url = config['ivcs-demo']['url']
    headers = {
        "Content-Type": 'application/json'
    }

    def __init__(self, user_login, user_pass):
        self.user_login = user_login
        self.user_pass = user_pass

    def getSessionId(self):
        try:
            with open("temp_token.txt") as data_file:
                json_data = json.load(data_file)
                print("read session at file")
            # проводим проверку на актуальность сессии
            check_session = self.set_session_info(sessionId=json_data['sessionId'])
            if check_session.status_code == 200:
                print("Session is active")
                return json_data['sessionId']
            elif check_session.status_code == 401:
                print('SessionId is not active')
                response = self.authenticationWithToken(token=json_data['loginToken'])
                # if response
                # with open('temp_token.txt', mode='w') as data_file:
                #     json.dump(response.json(), data_file)
                return response.json()['sessionId']
        # на случай если файл нет
        except FileNotFoundError:
            print('Get sessionId and tokenLogin')
            response = self.authenticationWithLogin().json()
            with open('temp_token.txt', mode='w') as data_file:
                json.dump(response, data_file)
            return response['SessionId']

    def authenticationWithLogin(self):
        print('Get sessionId and tokenLogin')
        body = {
            "login": self.user_login,
            "password": self.user_pass,
            "rememberMe": True
        }
        response = requests.post(f'{self.url}/login', headers=self.headers, json=body).json()
        with open('temp_token.txt', mode='w') as data_file:
            json.dump(response, data_file)
        return response

    def authenticationWithToken(self, token):
        print('Get the current session using token')
        header = {'token': token}
        body = {'token': token}
        response = requests.post(f'{self.url}/login-with-token', headers={**self.headers}, json=body)
        print(response.json())
        print(response.status_code)
        if response.status_code == 200:
            return response.json()
        else:
            print('Get the current session using login')
            response = self.authenticationWithLogin()
            with open('temp_token.txt', mode='w') as data_file:
                json.dump(response, data_file)
            return response.json()

    def conferenceCreate(self, sessionId, name, profileId, description='', runType="AUTO", features=[],
                         joinRestriction="ANYONE", attendeePermissions=[], attendeeMediaState="NONE",
                         startDate=0, duration=3600000):
        header = {'sessionId': sessionId}
        body = {
        "description": description,
        "settings": {
        "runType": runType,
        "features": features,
        "joinRestriction": joinRestriction,
        "attendeePermissions": attendeePermissions,
        "attendeeMediaState": attendeeMediaState,
        },
        "participants": [
        {'interlocutor':
             {'profileId': profileId}
        }
        ],
        "name": name,
        "startDate": startDate,
        "duration": duration,
        # "schedule": {
        # "periodicityType": periodicityType,
        # "daysOfWeek": daysOfWeek,
        # "dayNumber": dayNumber,
        # "weekNumber": weekNumber,
        # "monthNumber": monthNumber
        # }
        }

        res = requests.post(f'{self.url}/conferences', headers={**self.headers, **header}, json=body)
        # return res.json()['loginToken']
        return res

    def get_conference(self, conferenceId, sessionId):
        header = {'Session': sessionId}
        body = {}
        response = requests.get(f'{self.url}/conferences/{conferenceId}', headers={**self.headers, **header}, json=body)
        return response

    def get_conference_session(self, conferenceSessionId, sessionId):
        header = {'Session': sessionId}
        body = {}
        response = requests.get(f'{self.url}/conferences-session/{conferenceSessionId}', headers={**self.headers, **header}, json=body)
        return response

    def set_session_info(self, sessionId):
        header = {'session': sessionId}
        body = {}
        response = requests.get(f'{self.url}/session/info', headers={**self.headers, **header}, json=body)
        return response




