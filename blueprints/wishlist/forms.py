"""
blueprints/wishlist/forms.py
Thsi file here i will keep the forms making for the wishlist items
so that user will feel the details to keep as a note and submit
"""

from flask_wtf import FlaskForm  # type: ignore

from wtforms import StringField, SubmitField, TextAreaField, DecimalField

from wtforms.validators import DataRequired


class NewWishItemForm(FlaskForm):
    name = StringField(
        label="Name of The Item",
        validators=[DataRequired()],
    )
    price = DecimalField(
        label="Price of The item",
    )
    link = TextAreaField(
        label="WEB Link of this item?",
    )
    submit = SubmitField(
        label="Submit This Item",
    )
