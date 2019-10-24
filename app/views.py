from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm


@app.route('/')
@app.route('/dash')
def index():
	title = 'Home'
	user = {'name': 'Hitesh Yadav'}
	posts = [  # fake array of posts
        { 
            'author': {'nickname': 'Jackie'}, 
            'body': 'Beautiful day in Portland!' 
        },
        { 
            'author': {'nickname': 'Chan'}, 
            'body': 'The Avengers movie was so cool!' 
        }
    ]
	return render_template('index.html',
							title=title,
							user=user,
							posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
	title = 'Sign In'
	form = LoginForm()

	if form.validate_on_submit():
		flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))

		return redirect('/dash')

	return render_template('login.html', title=title, form=form, providers=app.config['OPENID_PROVIDERS'])