from flask import Flask, render_template
from logging import FileHandler,WARNING
app = Flask(__name__)


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