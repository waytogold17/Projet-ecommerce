from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Fastbase.db'
app.secret_key=["SECRET_KEY"]
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
SQLALCHEMY_TRACK_MODIFICATIONS = False
db = SQLAlchemy(app)
