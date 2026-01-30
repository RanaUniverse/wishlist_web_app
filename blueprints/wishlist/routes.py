"""
blueprints/wishlist/routes.py
in this file all the wishlist realted things will be present
"""

from flask import Blueprint, render_template, flash, abort

from flask_login import (  # type: ignore
    login_required,  # type: ignore
    current_user,
)

from blueprints.wishlist.forms import NewWishItemForm

from db_codes.functions import add_one_wish_item_for_a_user
from db_codes.db_make import engine

from utils.custom_logger import logger

wishlist_bp = Blueprint(
    name="wishlist_bp",
    import_name=__name__,
    template_folder="templates",
)


@wishlist_bp.route("/add_wishitem", methods=["GET", "POST"])
@login_required
def add_wishitem():
    form = NewWishItemForm()

    if form.validate_on_submit():  # type: ignore
        wish_name = form.name.data
        wish_price = form.price.data
        wish_link = form.link.data

        if wish_name is None or wish_price is None or wish_link is None:
            logger.error(
                "Even after validaion the values comes as None it should not be"
            )
            abort(
                code=401,
                description="Somethings wrong happens in the server pls report",
            )

        username = current_user.username
        if not username:
            logger.error(
                "in a login required fun the current_user should has the "
                " userame else somehtign wrong"
            )

    wish_item_obj = add_one_wish_item_for_a_user(
            db_engine=engine,
            username=username,
            wish_name=wish_name,
            wish_price=float(wish_price),
            wish_link=wish_link,
        )

        return render_template(
            template_name_or_list="wishlist/one_wish_item.html",
            wish_obj=wish_item_obj,
        )

    # i need to change this below to in html formatting
    if form.errors:
        flash(
            message=f"{form.errors}",
            category="warning",
        )

    return render_template(
        template_name_or_list="wishlist/new_wish_item.html",
        form=form,
    )
