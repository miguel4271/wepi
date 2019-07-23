import json
import socket
import requests

from flask import Flask, request, abort

app = Flask(__name__)

@app.route('/hello/<name>', methods=['GET'])
def webpi(name):
    if request.method == 'GET':

        # Actions to be performed on GET
        # Gets the hostname
        hostname = socket.gethostname()
        # Concatenates the hostname with the name on the endpoint with a message
        message = "Hello, {0}".format(name)+" from "+hostname
        # Builds the json body to be returned
        json_body = {
            'message': message
        }
        # Returns the json response
        return (json_body), 200

    else:
        abort(400)

if __name__ == '__main__':
    app.run()