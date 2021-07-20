import requests
import pprint
import json

##############################################################################################

init_url = r"https://px-conf.perimeterx.net/api/v1/mobile"
auth_type = r"https://developer.api.walmart.com/api-proxy/service/lmde/app/v4/services/auth/type"
api_login = r"https://developer.api.walmart.com/api-proxy/service/lmde/app/v4/services/auth/login"

login_payload = \
    {
        "payload": {
            "password": "Gm14605954.",
            "loginId": "gustavomogollonr@gmail.com",
            "validity": 1800
        }
    }

auth_payload = \
    {
        "payload": {
            "driverUserId": "gustavomogollonr@gmail.com"
        }
    }

init_payload = \
    {
        "app_id": "PXaY6hlFmo",
        "device_os_name": "Android",
        "device_os_version": "22",
        "sdk_version": "v1.13.1",
        "app_version": "2.22.1"
    }

main_headers = \
    {
        "x-px-authorization": "3",
        "wm_consumer.id": 'a9ca7a88-d09d-4ae6-851b-1bc5585bce2c',
        "user-agent": "Dalvik/2.1.0 (Linux; U; Android 5.1.1; ASUS_I001DA Build/LMY49I)",
        "wm_tenant_id": "0",
    }
##############################################################################################

# init_request = requests.post(init_url, data=init_payload)
# auth_request = requests.post(auth_type, json=auth_payload, headers=header.var)
login_request = requests.post(api_login, json=login_payload, headers=main_headers)

# print codes
# print(init_request)
# print(init_request.json())
# print(auth_request)
# print(auth_request.json())
print(login_request)
pprint.pprint(login_request.json())
