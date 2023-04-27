from pprint import pprint
from IVA_MCU_API import IvaApiIntegration
from Create_JWT import crate_token

token = crate_token('3e0db963-ba9c-41d0-9305-135c5871f36b',
            'e75c8a81f6c14b91a72034ac45f9850f548db662f1cd461bb58889e1f990cff8')
print = token

# res = requests.get('https://ivcs-lab.iva-tech.ru/api/rest/login', headers={'Authorization': 'Bearer'+ token}, json=body)