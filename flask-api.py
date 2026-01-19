from flask import Flask,jsonify #hey python i want to use flask

app = Flask(__name__) #creating a new flask application

@app.route('/') #when someone vistins the homepage (/)
def greetings():
    return "Login Succesfull!"


@app.route('/about')
def about():
    return "This is the about page of my website"


@app.route('/contact')
def contact():
    return "Contact us at: help@customerservice.com"

@app.route('/greet/<name>')
def greet(name):
    return f"Hello, {name}"

@app.route('/add/<int:num1>/<int:num2>')
def add(num1,num2):
    result = num1 + num2
    return f"{num1} + {num2} = {result}"


#JSON is the language of APIs, its how apps talk to each other

@app.route('/user',methods=['GET'])
def get_user():
    user_data ={
        "name" : "Pavithra",
        "age" : 25,
        "email": "pavithra@gmail.com"
    }
    return jsonify(user_data)

if __name__ == '__main__':
    app.run(debug=True) #start the server and show me errors if something breaks
