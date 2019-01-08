from flask import Flask, request as current_request
import os

app = Flask(__name__)

print("hello")

@app.route('/')
def hello_world():
    return f"Hello {os.environ['key']}"
