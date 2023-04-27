from IVA_MCU_API import IvaApiClient
from pprint import pprint
import configparser


config = configparser.ConfigParser()
config.read('settings.ini')

USER = IvaApiClient(config['ivcs-demo']['Login'], config['ivcs-demo']['Password'])

if __name__=='__main__':

    # print(USER.getSessionId())
    # data = USER.authenticationWithLogin()
    session_id = USER.authenticationWithToken()
    # pprint(data)
    # print(token)
    # conf = USER.get_conference_session('5f9aeaee-0a56-44dd-8436-91dae967743f', sessionId='9e0cde2d-e5c2-4af5-b8e2-0ae75c59ff75')
    # pprint(conf)

    request_user = USER.authenticationWithToken()
    session_id =request_user['sessionId']
    participant = request_user['user']['profileId']
    # print(f"Participant ID = {participant}")
    # print(f'*sessionId - {session}, \n*loginToken - {token}')
    #
    result = USER.conferenceCreate(name='new_conf123', profileId=participant,
                                  description='тестовое мероприятие123', sessionId=session_id)
    # print(result.status_code, result.json())
    # conf_info = DCH.get_conference('4c317779-787e-4c36-85d4-fa8b403c6d49', sessionId=session, token=token)
    # print(conf_info.status_code, conf_info.json())
    # session_info = DCH.set_session_info(sessionId=session, token=token)
    # print(session_info.status_code, session_info.json())

    # print(DCH.set_session_info(sessionId=session).status_code)
