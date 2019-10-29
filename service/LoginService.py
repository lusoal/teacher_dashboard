import requests
import os
import json

class LoginService(object):
    
    def realizar_login(self, user, password, userType):
        payload = {'usuario': user, 'senha': password}
        headers = {'content-type': "application/json"}
        try:
            session = requests.Session()
            response = session.post(f"http://{os.environ.get('URL_APPLICATION','localhost:8080')}/api/login/?userType={userType}", 
                data=json.dumps(payload), headers=headers)
            if (response.status_code == 200):
                print(response.cookies.get_dict())
                return response
            else:
                return False
        except Exception as e:
            print(e)
            raise e