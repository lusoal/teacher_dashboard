from flask import Flask, render_template, jsonify, \
    request, Response, redirect, url_for, session

from controller.FilterController import filter_controller
from controller.CursoController import curso_controller
from controller.TurmaController import turma_controller
from controller.ProfessorController import professor_controller
from controller.LoginController import login_controller


#Flask Configurations
class FlaskConfs(object):
        
    #Atributos
    app = Flask(__name__)
    app.secret_key = 'eipohgoo4rai0uf5ie1oshahmaeF'

    def __call__(self):
        self.register_blue_prints()
        self.run_app()
    
    def register_blue_prints(self):
        self.app.register_blueprint(curso_controller)
        self.app.register_blueprint(turma_controller)
        self.app.register_blueprint(filter_controller)
        self.app.register_blueprint(professor_controller)
        self.app.register_blueprint(login_controller)

    def run_app(self):
        self.app.run(debug=True, host='0.0.0.0')