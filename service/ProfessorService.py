import requests
import os
import qrcode
import json

class ProfessorService(object):
    
    def cadastrar_professor(self, nome, email, senha, cookie):
        print(cookie)
        payload = {'nome': nome, 'email': email,'senha': senha}
        headers = {'content-type': "application/json"}
        cookie = cookie
        try:
            session = requests.Session()
            response = requests.post(f"http://{os.environ.get('URL_APPLICATION','localhost:8080')}/api/professor/", 
                data=json.dumps(payload), headers=headers, cookies=cookie)
            print(response.text)
            if (response.status_code == 201):
                return response.json()
            else:
                raise Exception("Usuario ja cadastrado")
        except Exception as e:
            print(e)
            raise e
    
    def listar_disciplinas(self, user_info, cookie):
        print(user_info)
        headers = {'content-type': "application/json"}
        cookie = cookie
        try:
            session = requests.Session()
            response = requests.get(f"http://{os.environ.get('URL_APPLICATION','localhost:8080')}/api/disciplinasProfessor/{user_info.get('id')}", 
                headers=headers, cookies=cookie)
            
            print(response.text)
            
            if (response.status_code == 200):
                return response.json()
            else:
                raise Exception("Usuario ja cadastrado")
        except Exception as e:
            print(e)
            raise e
    
    def listar_aulas(self, user_info, cookie):
        print(user_info)
        headers = {'content-type': "application/json"}
        cookie = cookie
        try:
            session = requests.Session()
            response = requests.get(f"http://{os.environ.get('URL_APPLICATION','localhost:8080')}/api/disciplinasProfessor/{user_info.get('id')}", 
                headers=headers, cookies=cookie)
            
            print(response.text)
            
            if (response.status_code == 200):
                return response.json()
            else:
                raise Exception("Usuario ja cadastrado")
        except Exception as e:
            print(e)
            raise e
    
    def gerar_aula_qr_code(self, data, path_to_save = "static"):
    
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(f'{path_to_save}/qrcode_test.png')
        return True
    
    def listar_professores(self, cookie):
        headers = {'content-type': "application/json"}
        try:
            session = requests.Session()
            response = requests.get(f"http://{os.environ.get('URL_APPLICATION','localhost:8080')}/api/professores/", 
                headers=headers, cookies=cookie)
            
            print(response.text)
            
            if (response.status_code == 200):
                return response.json()
            else:
                raise Exception("Usuario ja cadastrado")
        except Exception as e:
            print(e)
            raise e

        