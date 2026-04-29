from flask import render_template, request, redirect

from app import app

from email_validator import validate_email, EmailNotValidError
from datetime import datetime


@app.route("/")
def index():
    current_date = datetime.now()
    return render_template("index.html", current_date=current_date)


@app.route("/about")
def about():
    team_members = [
        {'name': 'Jack', 'role': 'cook'},
        {'name': 'Federico', 'role': 'cook'},
        {'name': 'Tomas', 'role': 'waiter'},
        {'name': 'Jessica', 'role': 'waiter'},
        {'name': 'Jakub', 'role': 'waiter'},
        {'name': 'Antonio', 'role': 'hostess'}

    ]
    return render_template("about.html", team_members=team_members)


@app.route("/contact")
def contact():
    responsible_person = {
        'name': 'Alex',
        'position': 'Manager',
        'contact': {
            'phone': '8-123-456-789',
            'email': 'manager@restforrest.com'
        }
    }
    return render_template("contact.html", responsible_person=responsible_person)


@app.route("/submit", methods=["POST", "GET"])
def submit():
    if request.method == "POST":
        email = request.form.get("email")
        name = request.form.get("name")
        message = request.form.get("message")
        is_valid, res = email_validation(email)
        if is_valid:
            return render_template("contact.html", confirmation="Your message has been sent successfully!",
                                   email=email, name=name, message=message, status="success")
        else:
            return render_template("contact.html", confirmation="Incorrect email. Try again", email=email,
                                   name=name, message=message, status="error")
    return redirect("/contact")


def email_validation(email):
    try:
        is_valid = validate_email(email)
        return True, is_valid.email
    except EmailNotValidError:
        return False, None



