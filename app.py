from flask import Flask, jsonify, render_template, request
import time
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('main.html', reload = time.time())
