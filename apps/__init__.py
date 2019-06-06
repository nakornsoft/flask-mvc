# -*- coding: utf-8 -*-
__version__ = '0.1'
from flask import Flask, url_for, render_template, request, Response
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow


app = Flask(__name__, static_folder="static", template_folder="views")
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)
ma = Marshmallow(app)
from apps.controllers import *
