from emailValidation_app import app
from flask import render_template, redirect, request
#from emailValidation_app.models.emailValidation import EmailValidation

@app.route("/")
def home():
    return render_template("index.html")