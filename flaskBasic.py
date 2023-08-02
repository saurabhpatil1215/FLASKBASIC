from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def home_page():
    return render_template('index.html')

@app.route("/math", methods=['POST'])
def calculate():
    print(str(request.form))
    operation= request.form['operation']
    num1=int(request.form['num1'])
    num2=int(request.form['num2'])
   
    if operation=='add':
        result=num1+num2
        addResult=f'sum of {num1}+{num2}is {result}'
    elif operation=='subtract':
        result=num1-num2
        addResult=f'subtraction of {num1}-{num2}is {result}'
    elif operation=='multiply':
        result=num1*num2
        addResult=f'multiplytion of {num1}*{num2}is {result}'
    elif operation=='divide':
        result=num1/num2
        addResult=f'division of {num1}/{num2}is {result}'
    else:
        addResult=f'{operation}is either not arithmatic or its not supported.'

    return render_template('results.html',result=addResult)

@app.route("/")
def hello_world():
    return"<h1>Hello, Saurabh, Its Your first Web!</h1>"


@app.route("/test")
def test():
    data = request.args.get('x')
    return "This is the data input from my url {}".format(data)



if __name__ == '__main__':
    app.run(host="0.0.0.0")