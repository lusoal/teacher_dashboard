import requests
import os
import json

class CursoService(object):
    
    def cadastrar_curso(self, nome, cookie):
        print(cookie)
        payload = {'nome': nome}
        headers = {'content-type': "application/json"}
        cookie = cookie
        try:
            session = requests.Session()
            response = requests.post(f"http://{os.environ.get('URL_APPLICATION','localhost:8080')}/api/curso/", 
                data=json.dumps(payload), headers=headers, cookies=cookie)
            print(response.status_code)
            if (response.status_code == 201 or response.status_code == 200):
                return response.json()
            else:
                raise Exception("Curso ja cadastrado")
        except Exception as e:
            print(e)
            raise e

    def listar_cursos(self, cookie):
        headers = {'content-type': "application/json"}
        cookie = cookie
        try:
            session = requests.Session()
            response = requests.get(f"http://{os.environ.get('URL_APPLICATION','localhost:8080')}/api/cursos/", headers=headers, cookies=cookie)
            if (response.status_code == 200):
                return response.json()
            else:
                raise Exception("Erro ao listar cursos")
        except Exception as e:
            print(e)
            raise e