from flask import Flask
from flask import request

app = Flask(_name_)

@app.route("/")
def hello_world():
    return"<h1>Hello, Swanand, Its Your first Web!</h1>"

@app.route("/login")
def hello_loging():
    return"<h1>I am loging in</h1>"

@app.route("/About")
def About():
    return"<h1>Hello, About myself!</h1>"


@app.route("/test")
def test():
    data = request.args.get('x')
    return "This is the data input from my url {}".format(data)



if _name_ == '_main_':
    app.run(host="0.0.0.0")