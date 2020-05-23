from app import app
from flask import render_template, request, redirect

@app.route('/')
def home():
    return render_template("public/home.html")

@app.route('/features')
def features():
    return render_template('public/features.html')

@app.route('/about')
def about():
    return render_template("public/about.html")


@app.route('/sign-up', methods=["GET", "POST"])
def sign_up():

    if request.method == "POST":

        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        return redirect(request.url)

    return render_template("public/sign_up.html")