from flask import Flask, render_template, jsonify, \
    request, Response, redirect, url_for, Blueprint, session
import os
import json

from service.LoginService import LoginService
import requests

#Atributo
login_controller = Blueprint('login_controller', __name__)
loginService = LoginService()

@login_controller.route('/', methods=['GET'])
def index():
    #TODO: Remover pop da sessao para utilizar o Logout, criar Logout no Java API
    try:
        session.pop('cookie')
        session.pop('user_info')
    except:
        pass
    return redirect(url_for('login_controller.login', _external=True))

@login_controller.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        try:
            login_response = loginService.realizar_login(username, password)
            if (login_response):    
                session['cookie'] = login_response[0].cookies.get_dict()
                session['user_info'] = login_response[0].json()
                session['user_type'] = login_response[1]
                return redirect(url_for('login_controller.menu', _external=True))
            else:
                return redirect(url_for('login_controller.login', _external=True))
        except Exception as e:
            print(e)
            return redirect(url_for('login_controller.login', _external=True))
    else:
        return render_template("login.html")

@login_controller.route('/menu/', methods=['GET', 'POST'])
def menu():
    if not session.get("cookie"):
        return redirect(url_for('login_controller.login',  _external=True))
    print(session.get("cookie"))
    return render_template("menu.html", response = request.args.get('response'))