"""
This is the
blueprints/auth/routes.py
here i will write the register related informations
"""

from flask import (
    abort,
    Blueprint,
    flash,
    render_template,
    redirect,
    url_for,
)

from flask_login import (  # type: ignore
    login_user,  # type: ignore
    login_required,  # type: ignore
    logout_user,
)


from blueprints.auth.forms import RegisterForm, LoginForm

from db_codes.functions import (
    add_new_user,
    find_user_obj_from_username,
    verify_login_credentials,
)
from db_codes.db_make import engine

from utils.custom_logger import logger


auth_bp = Blueprint(
    name="auth_bp",
    import_name=__name__,
    template_folder="templates",
)


@auth_bp.route(
    rule="/register",
    methods=["GET", "POST"],
)
def register():
    """
    This fun is for the showing the register page to a new user
    When i will get the data form user i will try to check
    if the username is already there in the db,if already say user this
    else start register this...
    """
    form = RegisterForm()
    if form.validate_on_submit():  # type: ignore

        first_name = form.first_name.data
        username = form.username.data
        password = form.username.data

        # I make this below part just for adding one extra validation which i though
        # can be problem i need to think about this what is the problme or solution later

        # if not all([first_name, username, password]):
        if first_name is None or username is None or password is None:
            logger.error(
                "Form validation passed, but one or more required fields are None "
                "(first_name, username, password)"
            )
            flash(message="Something went wrong. Please try again.", category="danger")

            return render_template(
                template_name_or_list="auth/register_page.html",
                form=form,
            )

        existing_user = find_user_obj_from_username(
            db_engine=engine,
            username=username,
        )
        if existing_user:
            flash(
                message=f"The username **{username}** is already taken by another one "
                "Please Choose any other username",
                category="danger",
            )
            return render_template(
                template_name_or_list="auth/register_page.html",
                form=form,
            )

        new_user = add_new_user(
            db_engine=engine,
            first_name=first_name,
            last_name=form.last_name.data,
            phone_no=form.phone_no.data,
            username=username,
            password=password,
        )
        if not new_user:
            flash(
                message="Something wrong when try to register you in our Database"
                "Make a complain to the Admin in the /help section",
                category="warning",
            )
            return render_template(
                template_name_or_list="auth/register_page.html",
                form=form,
            )
        else:
            # means the new_user has been successfully insert in the db
            # i am now showing the data later i will need to use the db below
            flash(
                message="You Have Been Registerd Successfully Now...",
                category="info",
            )
            flash(
                message="After You fill the register page here should be a validate or otp verifiction like thigns, for now the verification process has not been made yet. It asumes that you have successfully register so please try to register here belwo with the passowrd you have entered.",
                category="success",
            )
            flash(
                message=f"Current Account's Usernaem:- `{username}`",
                category="info",
            )
            return redirect(url_for("auth_bp.login"))

    # This else part is when i get a /register Get from user
    else:
        flash(
            message="Let's Create Your Account",
            category="primary",
        )
        return render_template(
            template_name_or_list="auth/register_page.html",
            form=form,
        )


@auth_bp.route(
    rule="/login",
    methods=["GET", "POST"],
)
def login():
    """
    This fun will shows the login page to user
    where user will write the username and password
    """
    form = LoginForm()

    if form.validate_on_submit():  # type: ignore
        username = form.username.data
        password = form.password.data
        if username is None or password is None:
            logger.error("Username and password is none even after the validation.")
            abort(400)

        user_obj = verify_login_credentials(
            db_engine=engine,
            username=username,
            password=password,
        )

        if user_obj is None:
            flash("Invalid username or password ❌", "danger")
            flash("Please Retry Again Once More...", "secondary")
            return render_template(
                template_name_or_list="auth/login_page.html",
                form=form,
            )

        else:
            # means the user_obj is present
            login_user(
                user=user_obj,
                remember=True,
            )
            flash(
                message="Login Successful 🎉🎉🎉",
                category="success",
            )
            return redirect(url_for("general_bp.profile"))

    # This is when i will get Get Response
    return render_template(
        template_name_or_list="auth/login_page.html",
        form=form,
    )


@auth_bp.route(rule="/logout")
@login_required
def logout():
    logout_user()
    flash("You Have Just logged out 👋", "warning")
    return render_template(
        template_name_or_list="general/index.html",
    )
