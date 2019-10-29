from flask import Flask, render_template, jsonify, \
    request, Response, redirect, url_for, Blueprint, session

import requests

#Atributo
filter_controller = Blueprint('filter_controller', __name__)

@filter_controller.route('/', defaults={'u_path': ''})
@filter_controller.route('/<path:u_path>')
def catch_all(u_path):
    return render_template("errors/404.html")