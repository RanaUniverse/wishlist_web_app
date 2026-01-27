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
)


class RegisterForm(FlaskForm):
    first_name = StringField(
        label="First Name",
        validators=[DataRequired()],
        render_kw={"placeholder": "You Must need to enter"},
    )
    last_name = StringField(
        label="Last Name",
        validators=[Optional()],
    )
    phone_no = StringField(
        label="Phone Number",
        validators=[Optional(), Length(min=10, max=15)],
        render_kw={"placeholder": "Example: +91 9876598765"},
    )
    username = StringField(
        label="Unique Username",
        validators=[DataRequired(), Length(min=3, max=20)],
        render_kw={"placeholder": "Must Need (Minimum 3 Characters)"},
    )
    password = PasswordField(
        label="Password",
        validators=[
            DataRequired(),
            Length(
                min=3,
                message="Password must be at least 3 characters long",
            ),
        ],
        render_kw={"placeholder": "Must Need (Minimum 3 Characters)"},
    )
    submit = SubmitField(
        label="Register Here",
    )


class LoginForm(FlaskForm):
    username = StringField(
        label="Your Username",
        validators=[DataRequired(), Length(min=3, max=20)],
        render_kw={"placeholder": "What was your Username"},
    )
    password = PasswordField(
        label="Password Here",
        validators=[
            DataRequired(),
        ],
        render_kw={"placeholder": "What is Your Password"},
    )
    submit = SubmitField(label="Login Now")
