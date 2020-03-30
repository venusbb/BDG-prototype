from app import app
from flask import render_template


@app.route('/')

@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    return render_template('index.html', title='Home', user=user)


@app.route('/about')
def about():
    return render_template('about.html')