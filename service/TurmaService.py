import requests
import os
import json

class TurmaService(object):
    
    def cadastrar_turma(self, nome, curso, ano, cookie):
        print(cookie)
        payload = {'nome': nome, "ano": ano, "curso": { "id": curso } }
        headers = {'content-type': "application/json"}
        cookie = cookie
        try:
            session = requests.Session()
            response = requests.post(f"http://{os.environ.get('URL_APPLICATION','localhost:8080')}/api/turma/", 
                data=json.dumps(payload), headers=headers, cookies=cookie)
            print(response.status_code)
            if (response.status_code == 201 or response.status_code == 200):
                return response.json()
            else:
                raise Exception("Curso ja cadastrado")
        except Exception as e:
            print(e)
            raise e

    def listar_turmas(self, cookie):
        print(cookie)
        headers = {'content-type': "application/json"}
        cookie = cookie
        try:
            session = requests.Session()
            response = requests.get(f"http://{os.environ.get('URL_APPLICATION','localhost:8080')}/api/turmas/", headers=headers, cookies=cookie)
            print(response.status_code)
            if (response.status_code == 201 or response.status_code == 200):
                return response.json()
            else:
                raise Exception("Curso ja cadastrado")
        except Exception as e:
            print(e)
            raise e