from flask import render_template, request, redirect

from app import app

from email_validator import validate_email, EmailNotValidError


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


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



