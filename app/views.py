from app import app
from flask import render_template, request, redirect, send_from_directory, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_heroku import Heroku
import os
from datetime import datetime

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

heroku = Heroku(app)

db = SQLAlchemy(app)

class CustomerDB(db.Model):
    __tablename__ = 'customer_db'
    id = db.Column(db.Integer, primary_key=True)
    customer_email = db.Column(db.String(200), unique=True)
    trial = db.Column(db.Boolean)
    trial_date = db.Column(db.DateTime)
    purchased = db.Column(db.Boolean)
    purchase_date = db.Column(db.DateTime) # if purchase is False, this will be trial_date value
    subscriber = db.Column(db.Boolean)

    def __init__(
        self, customer_email, trial, trial_date,
        purchased, purchase_date, subscriber
    ):
        self.customer_email = customer_email
        self.trial = trial
        self.trial_date = trial_date
        self.purchased = purchased
        self.purchase_date = purchase_date
        self.subscriber = subscriber


@app.route('/')
def home():
    return render_template("public/home.html")

@app.route('/features')
def features():
    return render_template('public/features.html')

@app.route('/downloads')
def about():
    return render_template("public/download.html")

email_list=[]

@app.route('/download_installer', methods=['GET', 'POST'])
def download_installer():

    if request.method == "POST":
        customer_email = request.form["email"]
        
        #TODO redirect to thanks url
        if db.session.query(CustomerDB).filter(CustomerDB.customer_email == customer_email).count() == 0:
            try:
                data = CustomerDB(
                    customer_email, trial=True, trial_date=datetime.now(),
                    purchased=False, purchase_date=db.null(), subscriber=False
                )

                db.session.add(data)
                db.session.commit()

                return send_from_directory(
                    os.path.join(os.path.dirname(__file__) + '/' + 'static/downloads/trial/beta'), 
                    filename="BZMAN_TrialBetaSetup.exe", as_attachment=True)
            
            except Exception as e:
                print(e)
        
        else:
            redirect(url_for('thanks'))

    return render_template('public/download.html')

@app.route('/thankyou')
def thanks():
    return render_template('public/thankyou.html')