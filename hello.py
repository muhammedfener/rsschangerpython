import requests
from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def index():
    query_byte = request.query_string
    query_String = query_byte.decode("utf-8")
    content = requests.get('https://turktorrent.us/?'+query_String)
    return content.text


@app.after_request
def add_header(response):
    response.headers['Content-type'] = 'text/xml; charset=utf-8'
    return response