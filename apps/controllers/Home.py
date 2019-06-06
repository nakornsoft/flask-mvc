from apps import app
from flask import render_template

class Home(object):
    @app.route('/', methods=['GET', 'POST'])
    def Home():
        return "Welcome Flask MVC"
