from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, FloatField, SubmitField
from wtforms.validators import DataRequired, ValidationError

from luncher.consts import DishType
from luncher.models import Supplier, Dish


class AddDishForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    suppliers = Supplier.query.all()
    supplier = SelectField(
        'Supplier', validators=[DataRequired()], coerce=int, choices=[(s.id, s.name) for s in suppliers])
    dish_type = SelectField(
        'Dish type', validators=[DataRequired()], coerce=int, choices=[(k, v) for k, v in DishType.DISH_TYPES.items()])
    price = FloatField('Price', validators=[DataRequired()])
    calories = FloatField('Calories ( Optional )')
    carbohydrates = FloatField('Carbohydrates ( Optional )')
    fat = FloatField('Fat ( Optional )')
    proteins = FloatField('Proteins ( Optional )')
    submit = SubmitField('Add')

    def validate_dish(self, name, supplier):
        dish = Dish.query.filter_by(name=name.data.upper(), supplier_id=supplier.data)
        if dish:
            raise ValidationError(
                'Something went wrong. There is %s from this supplier in database' % name.data)


class AddSupplierForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Add')

    def validate_name(self, name):
        name = Supplier.query.filter_by(name=name.data.upper()).first()
        if name:
            raise ValidationError('Something went wrong. This supplier already exists.')
