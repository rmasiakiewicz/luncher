from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_required

from luncher import db
from luncher.admin.forms import AddDishForm, AddSupplierForm
from luncher.models import Dish, Supplier

admin = Blueprint('admin', __name__)


@admin.route("/dish/add", methods=['GET', 'POST'])
@login_required
def add_dish():
    form = AddDishForm()
    if not form.validate_on_submit():
        return render_template('add_dish.html', title='Add dish', form=form)
    dish = Dish(
        name=form.name.data, supplier_id=form.supplier.data, dish_type=form.dish_type.data, price=form.price.data)
    db.session.add(dish)
    db.session.commit()
    flash(f'Added {form.name.data}', 'success')
    return redirect(url_for('main.home'))


@admin.route("/supplier/add", methods=['GET', 'POST'])
@login_required
def add_supplier():
    form = AddSupplierForm()
    if not form.validate_on_submit():
        return render_template('add_supplier.html', title='Add supplier', form=form)
    supplier = Supplier(name=form.name.data)
    db.session.add(supplier)
    db.session.commit()
    flash(f'Supplier {form.name.data} added', 'success')
    return redirect(url_for('main.home'))
