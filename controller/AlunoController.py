from flask import Flask, render_template, jsonify, \
    request, Response, redirect, url_for, Blueprint, session
import os
import requests

from service.AlunoService import AlunoService
from service.TurmaService import TurmaService

#Atributo
aluno_controller = Blueprint('aluno_controller', __name__)

alunoService = AlunoService()
turmaService = TurmaService()

@aluno_controller.route('/cadastrar_aluno/', methods=['GET', 'POST'])
def cadastrar_aluno():
    if not session.get("cookie"):
        return redirect(url_for('login_controller.login', _external=True))
    if request.method != 'POST':
        turmas = turmaService.listar_turmas(session.get("cookie"))
        return render_template("aluno/cadastrar_aluno.html", turmas=turmas)
    
    nome = request.form['nome']
    senha = request.form['senha']
    email = request.form['email']
    turma_id = request.form['turma_id']

    try:
        print(f"TURMA ID {turma_id}")
        
        cadastro = alunoService.cadastrar_aluno(nome, email, senha, turma_id, session.get("cookie"))
        return redirect(url_for('login_controller.menu', response=f"Usuario {cadastro.get('nome')} cadastrado com sucesso !", _external=True))
    except Exception as e:
        print(f"Minha exception: {e}")
        return redirect(url_for('login_controller.menu', response="Erro: Usuario ja cadastrado", _external=True))

@aluno_controller.route('/listar_alunos/', methods=['GET', 'POST'])
def listar_alunos():
    if not session.get("cookie"):
        return redirect(url_for('login_controller.login', _external=True))
    if request.method != 'POST':
        alunos = alunoService.lista_alunos(session.get("cookie"))
        return render_template("aluno/cadastrar_aluno.html", alunos=alunos)