from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

from app.application.services.medicion_service import MedicionService

from app.infrastructure.auth.auth_guard import login_required

medicion_bp = Blueprint("medicion", __name__)

service = MedicionService()

@medicion_bp.route("/mediciones")
@login_required
def listar_todas_mediciones():

    mediciones = service.listar_todas()

    return render_template(
        "mediciones/listar.html",
        mediciones=mediciones
    )

@medicion_bp.route("/mediciones/<int:planta_id>")
@login_required
def listar_mediciones(planta_id):

    mediciones = service.listar_mediciones_por_planta(
        planta_id
    )

    return render_template(
        "mediciones/listar.html",
        mediciones=mediciones,
        planta_id=planta_id
    )


@medicion_bp.route(
    "/mediciones",
    methods=["POST"]
)

def crear_medicion():

    planta_id = int(
        request.form["planta_id"]
    )

    service.crear_medicion(
        planta_id=planta_id,
        temperatura=float(request.form["temperatura"]),
        humedad=float(request.form["humedad"]),
        desarrollo=float(request.form["desarrollo"]),
        observaciones=request.form.get(
            "observaciones"
        )
    )

    return redirect(
        url_for(
            "medicion.listar_mediciones",
            planta_id=planta_id
        )
    )