'''
HTTP VERBS
    Get-get from back end
    Post-posting
    Put-update
    Delete-delete
    Patch-update
'''
from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("login.html")

@app.route('/welcome')
def welcome():
    return render_template("welcome.html")

if __name__ ==("__main__"):
    app.run(debug=True)