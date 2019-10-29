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