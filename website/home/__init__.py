from flask import Flask,render_template,redirect


app = Flask(__name__)
app.debug = True
@app.route('/')
def hello_world():
    return render_template("home.html")