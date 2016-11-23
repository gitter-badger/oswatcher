#!/usr/bin/env python3

from flask import Flask, render_template
from flask_bootstrap import Bootstrap

from db import session, OS

app = Flask(__name__)
app.config.from_object('config')
Bootstrap(app)

@app.route('/view/<os_id>')
def view(os_id):
    return render_template('view.html', os_id=os_id)

@app.route('/')
def main():
    os_list = session.query(OS).all()
    return render_template('welcome.html', os_list=os_list)

if __name__ == '__main__':
    app.run()
