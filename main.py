"""
This is my main.py to run my website.
"""

import sys

sys.dont_write_bytecode = True
# This upper 2 line not make the __pycache__ folder


from flask import Flask


from blueprints.auth.routes import auth_bp
from blueprints.general.routes import general_bp

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
app.register_blueprint(blueprint=general_bp)


if __name__ == "__main__":
    app.run(
        host=FLASK_HOST,
        port=FLASK_PORT,
        debug=FLASK_DEBUG,
    )
