from flask import Blueprint, redirect, url_for, flash, render_template, request
from flask_login import current_user, login_user, logout_user, login_required

from luncher import bcrypt, db
from luncher.models import User
from luncher.users.forms import RegistrationForm, LoginForm

users = Blueprint('users', __name__)


@users.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(name=form.name.data, surname=form.surname.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.email.data}', 'success')
        return redirect(url_for('users.login'))
    return render_template('register.html', title='Register', form=form)


@users.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if not form.validate_on_submit():
        return render_template('login.html', title='Login', form=form)
    user = User.query.filter_by(email=form.email.data).first()
    if user and bcrypt.check_password_hash(user.password, form.password.data):
        login_user(user, remember=form.remember.data)
        next_page = request.args.get('next')
        flash(f'You have been logged in!', 'success')
        return redirect(next_page) if next_page else redirect(url_for('main.home'))
    else:
        flash('Login Unsuccessful. Pleas check username and password', 'danger')
        return render_template('login.html', title='Login', form=form)


@users.route("/logout", methods=['GET', 'POST'])
def logout():
    logout_user()
    flash(f'You have been logged out!', 'success')
    return redirect(url_for('main.home'))


@users.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')
