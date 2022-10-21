from flask import Flask, render_template, request, make_response, jsonify
import requests

app = Flask(__name__, instance_relative_config=True)

@app.route('/add')
def add():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a and b:
        return make_response(jsonify(s=a+b), 200) # HTTP 200 OK
    else:
        return make_response('Invalid input\n', 400) # HTTP 400 BAD REQUEST

@app.route('/sub')
def sub():
    #TODO: complete this function

@app.route('/mul')
def mul():
    #TODO: complete this function

@app.route('/div')
def div():
    #TODO: complete this function. 

@app.route('/mod')
def mod():
    #TODO: complete this function. 


def create_app():
    return app
