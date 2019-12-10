from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_required

from luncher import db
from luncher.admin.forms import AddDishForm, AddSupplierForm
from luncher.consts import DishType
from luncher.models import Dish, Supplier

admin = Blueprint('admin', __name__)


@admin.route("/dish", methods=['GET'])
@login_required
def dishes_view():
    dishes = Dish.query.all()
    return render_template('dishes.html', title='Dishes', dishes=dishes, dish_types=DishType.DISH_TYPES)


@admin.route("/dish/add", methods=['GET', 'POST'])
@login_required
def add_dish():
    form = AddDishForm()
    if not form.validate_on_submit():
        return render_template('add_dish.html', title='Add dish', form=form)
    dish = Dish(
        name=form.name.data.upper(), supplier_id=form.supplier.data, dish_type=form.dish_type.data,
        price=form.price.data, calories=form.calories.data, carbohydrates=form.carbohydrates.data, fat=form.fat.data,
        proteins=form.proteins.data)
    db.session.add(dish)
    db.session.commit()
    flash(f'Added {form.name.data}', 'success')
    return redirect(url_for('main.home'))


@admin.route("/dish/<dish_id>/edit", methods=['GET', 'POST'])
@login_required
def edit_dish(dish_id):
    pass


@admin.route("/dish/<dish_id>/delete", methods=['GET', 'POST'])
@login_required
def delete_dish(dish_id):
    Dish.query.filter_by(id=dish_id).delete()
    db.session.commit()
    flash(f'Successfully deleted dish')
    return redirect(url_for('main.home'))


@admin.route("/supplier/add", methods=['GET', 'POST'])
@login_required
def add_supplier():
    form = AddSupplierForm()
    if not form.validate_on_submit():
        return render_template('add_supplier.html', title='Add supplier', form=form)
    supplier = Supplier(name=form.name.data.upper())
    db.session.add(supplier)
    db.session.commit()
    flash(f'Supplier {form.name.data} added', 'success')
    return redirect(url_for('main.home'))


@admin.route("/supplier/delete", methods=['GET', 'POST'])
@login_required
def delete_supplier(supplier_id):
    Supplier.query.filter_by(id=supplier_id).delete()
    db.session.commit()
    flash(f'Successfully deleted supplier')
    return redirect(url_for('main.home'))
