import os
from flask import render_template, request, send_from_directory, redirect, url_for
from app import app

UPLOAD_FOLDER = os.path.basename('uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/")
def main():
    return render_template('main.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['image']
    f = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(f)
    return render_template('main.html', filename= "/uploads/" + file.filename)


@app.route('/uploads/<path:filename>', methods=['GET'])
def send_file(filename):
    return send_from_directory(os.path.join(os.getcwd() + "uploads", filename))