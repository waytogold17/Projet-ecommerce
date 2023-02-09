
#création de la base de donnée
import sqlite3
import click
from flask import current_app, g
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy
from .config import app,db




class Client(db.Model):
    #nomChamp = db.Column(db.Type , contrainte(optionnel))
        id_et = db.Column(db.Integer,primary_key=True)
        nom = db.Column(db.String(50),nullable=False)
        prenom = db.Column(db.String(80))
        email = db.Column(db.String(80),unique=True,nullable=False)
        
        def __repr__(self):
            return f"Fastbase{self.nom}"
with app.app_context():
    db.create_all()
    