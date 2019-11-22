import requests
import os
import json

#TODO: Alterar para disciplina turma pois disciplina e uma coisa diferente
class DisciplinaService(object):
    
    def cadastrar_disciplina(self, professor_id, turma_id, disciplina_id, dias_da_semana, cookie):
        print(cookie)
        payload = {'turma': turma_id, "disciplina": disciplina_id, "professor": professor_id, "diasDaSemana" : dias_da_semana}
        headers = {'content-type': "application/json"}
        cookie = cookie
        try:
            session = requests.Session()
            response = requests.post(f"http://{os.environ.get('URL_APPLICATION','localhost:8080')}/api/disciplinaTurma/", 
                data=json.dumps(payload), headers=headers, cookies=cookie)
            print(response.status_code)
            if (response.status_code == 201 or response.status_code == 200):
                return response.json()
            else:
                raise Exception("Disciplina ja cadastrada nessa turma")
        except Exception as e:
            print(e)
            raise e

    def listar_disciplinas(self, cookie):
        headers = {'content-type': "application/json"}
        cookie = cookie
        try:
            session = requests.Session()
            response = requests.get(f"http://{os.environ.get('URL_APPLICATION','localhost:8080')}/api/disciplinas/", headers=headers, cookies=cookie)
            print(response.status_code)
            if (response.status_code == 200):
                return response.json()
            else:
                raise Exception("Error")
        except Exception as e:
            print(e)
            raise e