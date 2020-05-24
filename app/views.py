from app import app
from flask import render_template, request, redirect, send_from_directory
import os

@app.route('/')
def home():
    return render_template("public/home.html")

@app.route('/features')
def features():
    return render_template('public/features.html')

@app.route('/downloads')
def about():
    return render_template("public/download.html")

MYDIR = os.path.dirname(__file__)

@app.route('/download_installer')
def download_installer():
    return send_from_directory(
        os.path.join(MYDIR + '/' + 'static/downloads/trial/beta'), 
        filename="BZMAN_BetaV2TrialSetup.exe",
        as_attachment=True
        )


# @app.route('/sign-up', methods=["GET", "POST"])
# def sign_up():

#     if request.method == "POST":

#         username = request.form["username"]
#         email = request.form["email"]
#         password = request.form["password"]

#         return redirect(request.url)

#     return render_template("public/sign_up.html")