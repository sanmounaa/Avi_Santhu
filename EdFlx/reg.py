from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///edflx.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

app.config['SECRET_KEY'] = 'd5997016ea9265b73abe1f59'
db = SQLAlchemy(app)

class users(db.Model):

    name =  db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False,unique=True,primary_key=True)
