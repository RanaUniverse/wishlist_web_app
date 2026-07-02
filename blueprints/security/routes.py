"""
blueprints/security/routes.py

Here i will make blueprin for security for whole app realted
"""

import secrets


from flask import (
    Blueprint,
    g,
    Response,
)

security_bp = Blueprint(
    name="security_bp",
    import_name=__name__,
)


@security_bp.before_app_request
def attaching_nonce():
    g.nonce = secrets.token_hex(
        nbytes=20,
    )


@security_bp.after_app_request
def modify_headers(response: Response):
    """
    I am using nonce to allow internal css and js
    though i should to use external css and js
    """
    response.headers["Content-Security-Policy"] = (
        f"default-src 'self'; "
        f"script-src 'self' 'nonce-{g.nonce}';"
        f"style-src 'self' 'nonce-{g.nonce}';"
    )

    # This below is for loading correct type of document
    response.headers["X-Content-Type-Options"] = "nosniff"

    response.headers["X-Frame-Options"] = "SAMEORIGIN"

    response.headers["Strict-Transport-Security"] = (
        "max-age=63072000; includeSubDomains; preload"
    )

    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"

    return response
