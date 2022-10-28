import json
from flask import Flask, request
app = Flask(__name__)


@app.route('/')
def index():
    return json.dumps({'name': 'alice',
                       'email': 'alice@outlook.com'})


# GET requests will be blocked
@app.route('/json-example', methods=['POST'])
def json_example():
    print("HEADERS:")
    print(request.headers)
    print("DATA")

    print(request.headers)


    print(request.cookies)
    print("DATA2")
    print(request.data)
    print(request.args)
    print(request.form)
    print(request.endpoint)
    print(request.method)
    print(request.remote_addr)
    data = request.data

    print(type(request.data))
    # request_data = request.get_json()
    # print("HOOOLA")
    # print(request_data)

    return "Received OK"
app.run()
