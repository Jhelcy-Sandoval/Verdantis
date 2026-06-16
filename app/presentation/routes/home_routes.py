from flask import Blueprint
from flask import render_template

from app.infrastructure.auth.auth_guard import login_required

home_bp = Blueprint(
    "home",
    __name__
)

@home_bp.route("/")
@login_required
def home():

    return render_template(
        "home/index.html",
        title="Métricas Verdes"
    )