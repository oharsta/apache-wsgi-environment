from flask import Flask, request as current_request
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    print("hello")
    return f"Hello {os.environ['key']}"
