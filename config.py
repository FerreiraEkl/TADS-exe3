# importações
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
import names
import random

app = Flask(__name__)

path = os.path.dirname(os.path.abspath(__file__))
arquivobd = os.path.join(path, 'carros.db')

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+arquivobd
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app)