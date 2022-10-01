from pickle import TRUE
from edapp import app
from flask import Flask
from flask import render_template,redirect,url_for,request,flash
from flask_sqlalchemy import SQLAlchemy
import sqlite3
from edapp.utils import createUser, get_random_string, responseHandler
from reg import db
from reg import users
from forms import registerform
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask import request

def __repr__(self):
        return f'users{self.name,self.email,self.password}'

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/register",methods=['GET','POST'])
def register():
    form = registerform()
    return render_template('auth/register.html',form=form)

@app.route("/reg",methods=['GET','POST'])


def reg():
    if (request.args.get("isItWeb")=="true"):
        if request.method == 'POST' and request.form['password'] == request.form['repeat_password']:
            data=createUser(request.form['user_name'],request.form['email'],request.form['password'])
            if(data.get("status")==True):
                return render_template('auth/login.html')
            else :
                return data
        else : 
            return "password not matched"

    elif (request.args.get("isItWeb")=="false"):
        if request.method == 'POST' and request.form['password'] == request.form['repeat_password']:
           return createUser(request.form['user_name'],request.form['email'],request.form['password'])
            
        else : 
            return "password not matched"
    else :
        return responseHandler(False,{},"Missed param isItWeb.")


@app.route('/login')
def login():
    return render_template('auth/login.html')

@app.route('/profile')
def profile():
    return render_template('profile/profile.html')

@app.route('/admin')
def admin():
    return render_template('admin/admin.html')

@app.route('/referrals')
def referral():
    return render_template('referral/referrals.html')

@app.route('/whatsappconsent')
def consent():
    return render_template('referral/whatsappconsent.html')

@app.route('/getAllUsers')
def get():
     query = db.select(["users"])
    
    
    
    
    