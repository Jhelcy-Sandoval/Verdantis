from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

from app.application.services.planta_service import PlantaService

planta_bp = Blueprint(
    "planta",
    __name__
)

service = PlantaService()


@planta_bp.route("/plantas")
def listar_plantas():

    plantas = service.listar_plantas()

    return render_template(
        "plantas/listar.html",
        plantas=plantas
    )


@planta_bp.route(
    "/plantas",
    methods=["POST"]
)
def crear_planta():

    service.crear_planta(
        tag=request.form["tag"],
        species=request.form["species"],
        germination_date=request.form["germination_date"],
        initial_conditions=request.form.get(
            "initial_conditions"
        )
    )

    return redirect(
        url_for("planta.listar_plantas")
    )


@planta_bp.route(
    "/plantas/<int:planta_id>"
)
def detalle_planta(planta_id):

    planta = service.obtener_por_id(
        planta_id
    )

    return render_template(
        "plantas/detalle_planta.html",
        planta=planta
    )


@planta_bp.route(
    "/plantas/<int:planta_id>/delete",
    methods=["POST"]
)
def eliminar_planta(planta_id):

    service.eliminar_planta(planta_id)

    return redirect(
        url_for("planta.listar_plantas")
    )