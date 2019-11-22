import requests
import os
import json

class AulaService(object):
    
    def cadastrar_aula(self, disciplina_turma_id, data_aula, horario, cookie):
        print(cookie)
        payload = {'disciplinaTurma': { "id": disciplina_turma_id }, "data": data_aula, "horario":horario}
        headers = {'content-type': "application/json"}
        cookie = cookie
        try:
            session = requests.Session()
            response = requests.post(f"http://{os.environ.get('URL_APPLICATION','localhost:8080')}/api/aula/", 
                data=json.dumps(payload), headers=headers, cookies=cookie)
            print(response.status_code)
            if (response.status_code == 201 or response.status_code == 200):
                return response.json()
            else:
                raise Exception("Aula ja cadastrada")
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