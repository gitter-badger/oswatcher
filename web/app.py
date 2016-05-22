#!/usr/bin/env python3

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
app = Flask(__name__)
app.config.from_object('config')
Bootstrap(app)

@app.route('/')
def main():
    return render_template('welcome.html')

if __name__ == '__main__':
    app.run()
