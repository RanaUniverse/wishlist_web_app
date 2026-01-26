"""

This is blueprints/general/routes.py
I will write the general informations about the website only
"""

from flask import (
    Blueprint,
    flash,
    render_template,
)


general_bp = Blueprint(
    name="general_bp",
    import_name=__name__,
    template_folder="templates/general",
)


@general_bp.route("/checking")
def checking():
    flash("🟦 Primary Message", "primary")
    flash("⚪ Secondary Message", "secondary")
    flash("✅ Success Message", "success")
    flash("❌ Danger Message", "danger")
    flash("⚠️ Warning Message", "warning")
    flash("ℹ️ Info Message", "info")
    flash("🌤️ Light Message", "light")
    flash("🌑 Dark Message", "dark")

    return render_template(
        template_name_or_list="checking.html",
    )


@general_bp.route("/")
def index():
    return render_template("index.html")


@general_bp.route("/about")
def about():
    return render_template(
        template_name_or_list="about_page.html",
    )


@general_bp.route("/help")
def help():
    return render_template(
        template_name_or_list="help_page.html",
    )
