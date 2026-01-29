"""
blueprints/errors/routes.py
This is how i will make the things differnet error messages will handle by this routes
"""

from werkzeug.exceptions import HTTPException, BadRequest


from flask import Blueprint, render_template


error_bp = Blueprint(
    name="error_bp",
    import_name=__name__,
    template_folder="templates",
)


# Here the error.description has a default value
# from the flask it will shows if i will not shows
@error_bp.app_errorhandler(400)
def handle_bad_request(error: HTTPException):

    if error.description != BadRequest.description:
        show_msg = error.description
    else:
        show_msg = None

    return (
        render_template(
            template_name_or_list="error/400.html",
            show_msg=show_msg,
        ),
        400,
    )
