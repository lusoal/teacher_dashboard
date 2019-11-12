from flask import Flask, render_template, jsonify, \
    request, Response, redirect, url_for, Blueprint, session
import os
import requests

from service.ProfessorService import ProfessorService

#Atributo
professor_controller = Blueprint('professor_controller', __name__)
professorService = ProfessorService()

@professor_controller.route('/cadastrar_professor/', methods=['GET', 'POST'])
def cadastrar_professor():
    if not session.get("cookie"):
        return redirect(url_for('login_controller.login', _external=True))
    if request.method != 'POST':
        return render_template("professor/cadastrar_professor.html")
    
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']
    try:
        cadastro = professorService.cadastrar_professor(nome, email, senha, session.get("cookie"))
        return redirect(url_for('login_controller.menu', response=f"Usuario {cadastro.get('nome')} cadastrado com sucesso !", _external=True))
    except Exception as e:
        print(f"Minha exception: {e}")
        return redirect(url_for('login_controller.menu', response="Erro: Usuario ja cadastrado", _external=True))

@professor_controller.route('/professor/disciplinas', methods=['GET', 'POST'])
def listar_professor_disciplinas():
    if not session.get("cookie"):
        return redirect(url_for('login_controller.login', _external=True))
    if request.method != 'POST':
        user_info = session['user_info']
        dicplinas_do_professor = professorService.listar_disciplinas(user_info, session.get("cookie"))
        return render_template("professor/exibir_professor_disciplina.html", dicplinas_do_professor=dicplinas_do_professor)

@professor_controller.route('/professor/aulas/', methods=['GET', 'POST'])
def listar_aulas_professor_disciplinas():
    if not session.get("cookie"):
        return redirect(url_for('login_controller.login', _external=True))

    aulas = eval(request.form['aulas'])
    print(aulas)
    return render_template("professor/aulas_professor_disciplina.html", aulas=aulas)

@professor_controller.route('/aula/criarPresenca/', methods=['GET', 'POST'])
def gerar_aula_qr_code():
    if not session.get("cookie"):
        return redirect(url_for('login_controller.login', _external=True))
    aula = request.form['aula']
    #TODO: Implementar adicionar criacao do endpoint para vincular QRCode ao ID da aula
    qr_code = professorService.gerar_aula_qr_code(aula)
    return render_template("professor/aula_qr_code.html")

