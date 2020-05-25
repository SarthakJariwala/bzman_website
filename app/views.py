from app import app
from flask import render_template, request, redirect, send_from_directory, url_for
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

@app.route('/download_installer', methods=['GET', 'POST'])
def download_installer():

    if request.method == "POST":
        email = request.form["email"]
        # print(email)
        #TODO redirect to thanks url
        return send_from_directory(
            os.path.join(os.path.dirname(__file__) + '/' + 'static/downloads/trial/beta'), 
            filename="BZMAN_TrialBetaSetup.exe", as_attachment=True)

    return render_template('public/download.html')

@app.route('/thankyou')
def thanks():
    return render_template('public/thankyou.html')