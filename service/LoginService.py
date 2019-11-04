import requests
import os
import json

class LoginService(object):
    
    def realizar_login(self, user, password):
        payload = {'usuario': user, 'senha': password}
        headers = {'content-type': "application/json"}
        userType = ["professor", "admin"]
        try:
            session = requests.Session()
            for types in userType:
                print(types)
                response = session.post(f"http://{os.environ.get('URL_APPLICATION','localhost:8080')}/api/login/?userType={types}", 
                    data=json.dumps(payload), headers=headers)
                if (response.status_code == 200):
                    print(f"[INFO] Logged as user type {types} ")
                    print(response.cookies.get_dict())
                    return response, types
                else:
                    continue
            return False
        except Exception as e:
            print(e)
            raise e