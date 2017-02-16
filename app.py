import os
from sqlite3 import dbapi2 as sqlite3
from flask_bcrypt import Bcrypt
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stream')
def stream():

    return render_template('stream.html')

@app.route('/about')
def about():
    User = {}
    User['name'] = 'Bill Grundler'
    User['profession'] = 'Really good singer'

    return render_template('about.html', User=User)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=4000)