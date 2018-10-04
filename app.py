from flask import Flask, jsonify, render_template, request
import time
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"
