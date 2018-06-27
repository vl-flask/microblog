from flask import render_template, flash, redirect, url_for
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Vassily'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', user=user, title="Home", posts=posts)

@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f"Login requested for user {form.username.data}, remember_me={form.remember_me.data}")
        return redirect(url_for('index'))
    return render_template('login.html', form=form, title='Sign In')
