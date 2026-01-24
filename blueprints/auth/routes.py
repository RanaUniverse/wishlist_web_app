"""
This is the
blueprints/auth/routes.py
here i will write the register related informations
"""

from flask import (
    Blueprint,
    render_template,
)


from blueprints.auth.forms import RegisterForm


auth_bp = Blueprint(
    name="auth_bp",
    import_name=__name__,
    template_folder="templates/auth",
)


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    """
    This fun is for the showing the register page to a new user
    """
    form = RegisterForm()
    if form.validate_on_submit():  # type: ignore
        return render_template(
            "show_data.html",
            data={
                "first_name": form.first_name.data,
                "last_name": form.last_name.data,
                "phone_no": form.phone_no.data,
                "email_id": form.email_id.data,
                "username": form.username.data,
            },
        )
    else:
        print(form.errors)
        return render_template(
            template_name_or_list="register_page.html",
            form=form,
        )


@auth_bp.route("/login")
def login():
    """
    This fun will shows the login page to user
    where user will write the username and password
    """
    return render_template(
        template_name_or_list="login_page.html",
    )
