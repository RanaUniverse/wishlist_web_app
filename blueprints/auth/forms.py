"""
This is the file here i will write the logic of the
auth related forms making with flask-wtf
blueprints/auth/forms.py
"""

from flask_wtf import FlaskForm  # type: ignore

from wtforms import (
    StringField,
    PasswordField,
    SubmitField,
)

from wtforms.validators import (
    DataRequired,
    Optional,
    Length,
    Email,
)


class RegisterForm(FlaskForm):
    first_name = StringField(
        label="First Name",
        render_kw={"placeholder": "You Must need to enter"},
        validators=[DataRequired()],
    )
    last_name = StringField(
        label="Last Name",
        validators=[Optional()],
    )
    phone_no = StringField(
        label="Phone Number",
        validators=[Optional(), Length(min=10, max=15)],
    )
    email_id = StringField(
        label="Email Address",
        validators=[Optional(), Email()],
    )
    username = StringField(
        label="Unique Username",
        validators=[DataRequired(), Length(min=1, max=10)],
        render_kw={"placeholder": "You Must need to enter"},
    )
    password = PasswordField(
        label="Password",
        render_kw={"placeholder": "You Must need to enter"},
        validators=[
            DataRequired(),
            Length(
                min=3,
                message="Password must be at least 3 characters long",
            ),
        ],
    )
    submit = SubmitField(
        label="Register Here",
    )
