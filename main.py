"""
This is my main.py to run my website.
"""

import sys

sys.dont_write_bytecode = True
# This upper 2 line not make the __pycache__ folder


from flask import Flask

from flask_login import LoginManager  # type: ignore

from blueprints.auth.routes import auth_bp
from blueprints.general.routes import general_bp
from blueprints.errors.routes import error_bp

from db_codes.db_make import create_db_and_engine, engine
from db_codes.functions import find_user_obj_from_user_id

from utils.config_settings import (
    FLASK_DEBUG,
    FLASK_HOST,
    FLASK_PORT,
    SECRET_KEY,
)


app = Flask(
    import_name=__name__,
    template_folder="templates",
    static_folder="static",
)


app.config["SECRET_KEY"] = SECRET_KEY

app.register_blueprint(blueprint=auth_bp)
app.register_blueprint(blueprint=error_bp)
app.register_blueprint(blueprint=general_bp)


login_manager = LoginManager()
login_manager.init_app(app)  # type: ignore
login_manager.login_view = "auth_bp.login"  # type: ignore


@login_manager.user_loader  # type: ignore
def load_user_from_session(user_id: str):
    """
    Here the user_id coming from the session
    and flask-login will retrive the user_obj from running this function
    """
    return find_user_obj_from_user_id(
        db_engine=engine,
        user_id=user_id,
    )


if __name__ == "__main__":
    create_db_and_engine()
    app.run(
        host=FLASK_HOST,
        port=FLASK_PORT,
        debug=FLASK_DEBUG,
    )
