from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import session

from app.application.services.auth_service import AuthService

auth_bp = Blueprint(
    "auth",
    __name__
)

service = AuthService()


@auth_bp.route("/login")
def login():

    return render_template(
        "auth/login.html"
    )

@auth_bp.route(
    "/login",
    methods=["POST"]
)
def login_post():
    
    try:
        email = request.form.get("email")
        password = request.form.get("password")

        response = service.login(
            email=email,
            password=password
        )

        if not response:
            return render_template(
                "auth/login.html",
                error="Correo o contraseña incorrectos"
            )

        session["access_token"] = (
            response.session.access_token
        )

        return redirect(
            url_for("home.home")
        )
    except Exception:
        return redirect(
            url_for("error.error_404")
        )


@auth_bp.route("/signup")
def signup():

    return render_template(
        "auth/register.html"
    )


@auth_bp.route(
    "/signup",
    methods=["POST"]
)
def signup_post():

    try:

        service.register(
            email=request.form.get("email"),
            password=request.form.get("password")
        )

        return redirect(
            url_for("auth.login")
        )

    except Exception:

        return redirect(
            url_for("error.error_404")
        )

@auth_bp.route("/logout")
def logout():

    service.logout()

    return redirect(
        url_for("auth.login")
    )

