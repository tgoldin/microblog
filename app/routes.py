from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Tony'}
    posts = [
        {
            'author': {'username': 'T800'},
            'body': '''I'm not obsolete!'''
        },
        {
            'author': {'username': 'T1000'},
            'body': '''I'll be back!'''
        },
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)