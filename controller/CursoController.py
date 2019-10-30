from flask import Flask, render_template, jsonify, \
    request, Response, redirect, url_for, Blueprint, session
import os
import ast
import requests

from service.CursoService import CursoService

#Atributo
curso_controller = Blueprint('curso_controller', __name__)
cursoService = CursoService()

@curso_controller.route('/cadastrar_curso/', methods=['GET', 'POST'])
def cadastrar_curso():
    if not session.get("cookie"):
        return redirect(url_for('login_controller.login', _external=True))
    if request.method != 'POST':
        return render_template("curso/cadastrar_curso.html")
    
    nome = request.form['nome']
    try:
        cadastro = cursoService.cadastrar_curso(nome, session.get("cookie"))
        return redirect(url_for('login_controller.menu', response=f"Curso {cadastro.get('nome')} cadastrado com sucesso !", _external=True))
    except Exception as e:
        print(f"Minha exception: {e}")
        return redirect(url_for('login_controller.menu', response="Erro: Curso já cadastrado", _external=True))

@curso_controller.route('/listar_cursos/', methods=['GET', 'POST'])
def listar_cursos():
    if not session.get("cookie"):
        return redirect(url_for('login_controller.login', _external=True))
    turmas = request.form.get('turmas')
    if(turmas):
        turmas = ast.literal_eval(turmas)
    cursos = cursoService.listar_cursos(session.get("cookie"))
    return render_template("curso/exibir_cursos.html", cursos = cursos, turmas=turmas)