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

@app.route('/',methods=['POST'])
def index():
    return render_template("login.html")

@app.route('/login')
def login(email,password):
    email=str("derrickragui@gmail.com")
    password="derrick2021"

    if request.method==['POST']:
        email=request.form["derrickragui@gmail.com"]
        password=request.form["derrick2021"]
        return render_template("Welcome")
    else:
        return("wrong credentials")
if __name__ ==("__main__"):
    app.run(debug=True)