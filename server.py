from flask import Flask, escape, request, render_template, send_from_directory
from os import path

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<username>')
def hello_user(username=None):
    return render_template('index.html', username=username)

@app.route('/<username>/<int:post_id>')
def hello_user_id(username=None, post_id=1):
    return render_template('index.html', username=username, post_id=post_id)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
# @app.route('/main.css')
# def blog():
#     return render_template('main.css')

# @app.route('/main.js')
# def blog():
#     return render_template('main.js')

@app.route('/about.html')
def blog2():
    
    return render_template('about.html')