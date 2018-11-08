import os
from flask import render_template, flash, request, send_from_directory, redirect
from app import app
from app import filter
from app.forms import LoginForm

UPLOAD_FOLDER = os.path.basename('uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/")
def main():
    return render_template('index.html')

@app.route("/filter")
def filter():
    return render_template("main.html")

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['image']
    choice = request.form['filter']
    f = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(f)
    new_file = filter.filter_image(file.filename, choice)
    return render_template('main.html', filename = "/uploads/" + new_file)


@app.route('/uploads/<path:filename>', methods=['GET'])
def send_file(filename):
    print(os.getcwd() + "uploads")
    return send_from_directory(os.path.join(os.getcwd() + r"\uploads"), filename)

@app.after_request
def add_header(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    print(response.headers.get('Cache-Control'))
    return response

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/')
    return render_template('login.html', title='Sign In', form=form)