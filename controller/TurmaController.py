from flask import Flask, render_template, jsonify, \
    request, Response, redirect, url_for, Blueprint, session
import os
import ast
import requests

from service.TurmaService import TurmaService
from service.CursoService import CursoService

#Atributo
turma_controller = Blueprint('turma_controller', __name__)
turmaService = TurmaService()
cursoService = CursoService()

@turma_controller.route('/cadastrar_turma/', methods=['GET', 'POST'])
def cadastrar_turma():
    if not session.get("cookie"):
        return redirect(url_for('login_controller.login', _external=True))
    if request.method != 'POST':
        #TODO: Listar todos os cursos
        cursos = cursoService.listar_cursos(session.get("cookie"))
        return render_template("turma/cadastrar_turma.html", cursos=cursos)
    
    nome = request.form['nome']
    ano_inicio = request.form['ano']
    curso_id= request.form['curso_id']

    try:
        print(nome, ano_inicio, curso_id)
        cadastro = turmaService.cadastrar_turma(nome, curso_id, ano_inicio, session.get("cookie"))
        return redirect(url_for('login_controller.menu', response=f"Truma {cadastro.get('nome')} cadastrada com sucesso !", _external=True))
    except Exception as e:
        print(f"Minha exception: {e}")
        return redirect(url_for('login_controller.menu', response="Erro: Curso já cadastrado", _external=True))

@turma_controller.route('/listar_turmas/', methods=['GET', 'POST'])
def listar_turmas():
    turmas = turmaService.listar_turmas(session.get("cookie"))
    if request.method != 'POST':
        print("AGORA VAI")
        return render_template("turma/exibir_turmas.html", turmas=turmas)

@turma_controller.route('/listar_disciplinas_turma/', methods=['GET', 'POST'])
def listar_disciplinas_turma():
    turma = eval(request.form['turma'])
    disciplinas_turma = turma.get("disciplina_turma")
    print(disciplinas_turma)
    return render_template("turma/listar_disciplinas_turma.html", disciplinas_turma=disciplinas_turma)

@turma_controller.route('/cadastrar_aulas/', methods=['GET', 'POST'])
def cadastrar_aulas():
    disiplina_turma_id = int(request.form['disciplinas_turma_id'])
    print(disiplina_turma_id)
    return render_template("turma/cadastrar_aula.html", disiplina_turma_id=disiplina_turma_id)

@turma_controller.route('/cadastrar_aula/', methods=['GET', 'POST'])
def cadastrar_aula():
    disiplina_turma_id = int(request.form['disciplinas_turma_id'])
    print(disiplina_turma_id)

    return render_template("turma/cadastrar_aula.html", disiplina_turma_id=disiplina_turma_id)

@turma_controller.route('/listar_aulas_disciplina/', methods=['GET', 'POST'])
def listar_aulas_disciplina():
    aulas = eval(request.form['aulas'])
    print(aulas)
    return render_template("turma/listar_aulas.html", aulas=aulas)