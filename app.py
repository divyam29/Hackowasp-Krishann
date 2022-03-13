from flask import Flask, render_template,request, session, redirect
from logging import FileHandler, WARNING
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

local_server = True

if local_server:
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:@localhost/hackowasp"
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:@localhost/hackowasp"

db = SQLAlchemy(app)

class contact(db.Model):
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    message = db.Column(db.String(255), nullable=False)

@app.route("/")
def home():
    return render_template('Home.html')


@app.route("/About")
def about():
    return render_template('About.html')


@app.route("/Our-App")
def ourapp():
    return render_template('Our-App.html')


@app.route("/Contact")
def contact():
    return render_template('Contact-US.html')


@app.route("/SignIn")
def signin():
    return render_template('Sign-In.html')


if __name__ == "main":
    app.run(debug=True)

file_handler = FileHandler('errorlog.txt')
file_handler.setLevel(WARNING)
