from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

error_bp = Blueprint("error", __name__)

@error_bp.route("/404")
def error_404():
    return render_template("errors/404.html"), 404