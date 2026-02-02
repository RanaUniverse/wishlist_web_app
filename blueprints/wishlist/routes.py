"""
blueprints/wishlist/routes.py
in this file all the wishlist realted things will be present
"""

from flask import (
    Blueprint,
    render_template,
    flash,
    abort,
    redirect,
    url_for,
)

from flask_login import (  # type: ignore
    login_required,  # type: ignore
    current_user,
)

from blueprints.wishlist.forms import NewWishItemForm
from db_codes.functions import (
    WishItemNotFound,
    WishItemOwnerNotMatch,
    WishItemUnknownError,
)
from db_codes.functions import (
    add_one_wish_item_for_a_user,
    delete_wish_item,
    get_all_wish_items_for_a_user,
)
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
            flash("Somethings Wrong here with the server")
            abort(
                code=401,
                description="Please report to the admins about the error.",
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
            one_wish=wish_item_obj,
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


@wishlist_bp.route(rule="/edit_wish/<uuid>")
@login_required
def edit_wishitem(uuid: str):
    user_id = current_user.id_

    if not user_id:
        logger.error("When user is login already it should have teh id_ value exists")
        abort(
            code=401,
            desciption="You are not authorized to use this or some server problem",
        )
    flash(
        message="This Features has not impliment yet (Coming Soong...)",
        category="primary",
    )
    return redirect(url_for("general_bp.profile"))


@wishlist_bp.route(rule="/delete_wish/<uuid>")
@login_required
def delete_wishitem(uuid: str):
    user_id = current_user.id_

    # This below should not execute
    if not user_id:
        logger.error("When user is login already it should have teh id_ value exists")
        abort(
            code=401,
            desciption="You are not authorized to use this or some server problem",
        )
    try:
        del_item = delete_wish_item(
            db_engine=engine,
            wish_uuid=uuid,
            user_id=user_id,
        )
        if del_item:
            logger.info(
                msg=f"User with the {user_id} has delete his note of {uuid} now."
            )
            flash(
                message="✅ Wish item deleted successfully!",
                category="danger",
            )
            return redirect(url_for(endpoint="wishlist_bp.all_wishes_items"))
        else:
            logger.info(msg="Wish Item not deleted anyhow?")
            flash(
                message="Wish Item Deleted Failed.",
                category="warning",
            )
            flash(
                message="Please Contact With Admins",
                category="warning",
            )
            return redirect(url_for(endpoint="wishlist_bp.all_wishes_items"))

    except WishItemNotFound:
        flash(
            message=f"`{uuid}`- Does Not Match with Any Wishes",
            category="primary",
        )
        flash(
            message="❌ This wish item was not found. It may have already been removed.",
            category="warning",
        )

    except WishItemOwnerNotMatch:

        flash(
            message=f"`{uuid}`- is Owner By Someone Else",
            category="primary",
        )
        flash(
            message="🚫 You are not allowed to delete this wish item.",
            category="warning",
        )

    except WishItemUnknownError:
        flash(
            message="💥 Something went wrong on our side. Please try again later.",
            category="warning",
        )

    return redirect(url_for(endpoint="wishlist_bp.all_wishes_items"))


@wishlist_bp.route(rule="/all_wishes")
@login_required
def all_wishes_items():
    user_id = current_user.id_
    if not user_id:
        logger.error("When user is login already it should have teh id_ value exists")
        abort(
            code=401,
            description="You are not authorized to use this or some server problem",
        )
    all_wishes = get_all_wish_items_for_a_user(
        db_engine=engine,
        user_id=user_id,
    )

    return render_template(
        "wishlist/all_wish_item.html",
        all_wishes=all_wishes,
    )
