from emailValidation_app import app
from flask import render_template, redirect, request
from emailValidation_app.model.emailValidation import Email
from flask import flash


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    print(request.form)
    if not Email.validate_email(request.form):
        return redirect("/")
    new_email = Email.add_email(request.form)
    return redirect("/show_emails")

@app.route("/show_emails")
def show_emails():
    all_emails = Email.all_emails()
    return render_template("emails.html", emails = all_emails)