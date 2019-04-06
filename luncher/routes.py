from flask import render_template, url_for, flash, redirect

from luncher import app
from luncher.forms import RegistrationForm, LoginForm


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/about")
def about():
    return render_template('home.html')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.email.data}', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if not form.validate_on_submit():
        return render_template('login.html', title='Login', form=form)
    if form.email.data == 'test@test.com' and form.password.data == 'password':
        flash(f'You have been logged in!', 'success')
        return redirect(url_for('home'))
    else:
        flash('Login Unsuccessful. Pleas check username and password', 'danger')
        return render_template('login.html', title='Login', form=form)
