from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, FloatField, SubmitField
from wtforms.validators import DataRequired, ValidationError

from luncher.models import Supplier, Dish


class AddDishForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    suppliers = Supplier.query.all()
    supplier = SelectField(
        'Supplier', validators=[DataRequired()], coerce=int, choices=[(s.id, s.name) for s in suppliers])
    dish_type = StringField('Dish type', validators=[DataRequired()])
    price = FloatField('Price', validators=[DataRequired()])
    submit = SubmitField('Add')

    def validate_dish(self, name, supplier):
        dish = Dish.query.filter_by(name=name.data, supplier_id=supplier.data)
        if dish:
            raise ValidationError(
                'Something went wrong. There is %s from this supplier in database' % name.data)


class AddSupplierForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Add')

    def validate_name(self, name):
        name = Supplier.query.filter_by(name=name.data).first()
        if name:
            raise ValidationError('Something went wrong. This supplier already exists.')
