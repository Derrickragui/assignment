from flask import Flask, render_template, request, redirect, url_for,session
from flask.helpers import make_response
app = Flask(__name__)
app.secret_key="123456"


@app.route('/')
def index():
    return render_template("login.html")

@app.route('/login', methods=['POST'])
def login():

    students = [
        {
            "name": "Fred",
            "email": "fred@gmail.com",
            "password": "123456",
            "age": 24,
            "gender": "Male",
            "score": "29/50"
        },
         {
            "name": "Dossy",
            "email": "dossy@gmail.com",
            "password": "123456",
            "age": 24,
            "gender": "Male",
            "score": "29/50"

        },
         {
            "name": "Derick",
            "email": "derick@gmail.com",
            "password": "123456",
            "age": 20,
            "gender": "Male",
            "score": "29/50"

        },
        {
            "name": "Dominick",
            "email": "dominic@gmail.com",
            "password": "123456",
            "age": 35,
            "gender": "Male",
            "score": "29/50"

        },
          {
            "name": "Bobby",
            "email": "bobby@gmail.com",
            "password": "123456",
            "age": 13,
            "gender": "Male",
            "score": "29/50"

        }
    ]

    for student in students:
        if student['email'] == request.form['email']  and student['password'] == request.form['password'] :
           session["user email"]=request.form['email']
           return redirect(url_for('scores'))

    return "<h1>Wrong credentials</h1>"

@app.route('/scores')
def scores():
    students = [
        {
            "name": "Fred",
            "email": "fred@gmail.com",
            "password": "123456",
            "age": 24,
            "gender": "Male",
            "score": "29/50"
        },
         {
            "name": "Dossy",
            "email": "dossy@gmail.com",
            "password": "123456",
            "age": 24,
            "gender": "Male",
            "score": "29/50"

        },
         {
            "name": "Derick",
            "email": "derick@gmail.com",
            "password": "123456",
            "age": 20,
            "gender": "Male",
            "score": "29/50"

        },
        {
            "name": "Dominick",
            "email": "dominic@gmail.com",
            "password": "123456",
            "age": 35,
            "gender": "Male",
            "score": "29/50"

        },
          {
            "name": "Bobby",
            "email": "bobby@gmail.com",
            "password": "123456",
            "age": 13,
            "gender": "Male",
            "score": "29/50"

        }
    ]
    # res = list(map(itemgetter(email), students))
    email = request.cookies.get("computer pride system")
    if email==None:
        return render_template("login,html")

    return render_template("scores.html", students = students, email = email)

if __name__ == ("__main__"):
    app.run(debug=True)