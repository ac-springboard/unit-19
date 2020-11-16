from flask import Flask, request as req
from operations import add, sub, mult, div

app = Flask(__name__)


@app.route('/')
def r_root():
    return """
    <DOCTYPE html>
    <html>
        <head>
            <title>Unit 19.1</title>
        </head>
        <body>
            <h3>Navigator</h3>
            <a href="/add?a=10&b=10">Add: 10 + 10</a><br />
            <a href="/sub?a=10&b=5">Subtract: 10 - 5</a><br />
            <a href="/mult?a=10&b=10">Multiply: 10 * 10</a><br />
            <a href="/div?a=10&b=5">Divide: 10 / 5</a><br />
        </body>
    </html>
    """


@app.route('/add')
def r_add():
    a = int(req.args['a'])
    b = int(req.args['b'])
    return str(add(a, b))


@app.route('/sub')
def r_sub():
    a = int(req.args['a'])
    b = int(req.args['b'])
    return str(sub(a, b))


@app.route('/mult')
def r_mult():
    a = int(req.args['a'])
    b = int(req.args['b'])
    return str(mult(a, b))


@app.route('/div')
def r_div():
    a = int(req.args['a'])
    b = int(req.args['b'])
    return str(div(a, b))



