from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

from app.application.services.alerta_service import AlertaService

from app.infrastructure.auth.auth_guard import login_required

alerta_bp = Blueprint("alerta", __name__)

service = AlertaService()

@alerta_bp.route("/alertas")
@login_required
def listar_alertas():
    return render_template(
        "alertas/listar.html",
        # alertas=service.listar_alertas()
    )