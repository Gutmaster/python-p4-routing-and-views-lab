#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<parameter>')
def print_route(parameter):
    print(parameter)
    return parameter

@app.route('/count/<parameter>')
def count_route(parameter):
    count = '\n'.join(str(i) for i in range(int(parameter))) + '\n'
    return count

@app.route('/math/<int:num1>/<operator>/<int:num2>')
def math_route(num1, operator, num2):
    if operator == '+':
        return str(num1 + num2)
    elif operator == '-':
        return str(num1 - num2)
    elif operator == '*':
        return str(num1 * num2)
    elif operator == 'div':
        if num2 != 0:
            return str(num1 / num2)
        else:
            return 'Error: Division by zero'
    elif operator == '%':
        return str(num1 % num2)
    else:
        return 'Error: Invalid operator'

if __name__ == '__main__':
    app.run(port=5555, debug=True)