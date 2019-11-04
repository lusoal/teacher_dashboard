import requests
import os
import json

class AlunoService(object):
    
    def cadastrar_aluno(self, nome, email, senha, turma_id, cookie):
        print(cookie)
        payload = {'nome': nome, 'email': email, 'senha': senha, "turma" : { "id" : turma_id } }
        print(payload)
        
        headers = {'content-type': "application/json"}
        cookie = cookie
        try:
            session = requests.Session()
            response = requests.post(f"http://{os.environ.get('URL_APPLICATION','localhost:8080')}/api/aluno/", 
                data=json.dumps(payload), headers=headers, cookies=cookie)
            print(response.text)
            if (response.status_code == 201):
                return response.json()
            else:
                raise Exception("Usuario ja cadastrado")
        except Exception as e:
            print(e)
            raise e