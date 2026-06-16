from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

from app.application.services.planta_service import PlantaService

from app.infrastructure.auth.auth_guard import login_required
from app.infrastructure.auth.supabase_client import supabase

planta_bp = Blueprint(
    "planta",
    __name__
)

service = PlantaService()


@planta_bp.route("/plantas")
@login_required
def listar_plantas():

    user = supabase.auth.get_user()

    plantas = service.listar_plantas_por_usuario(
        user.user.id
    )

    return render_template(
        "plantas/listar.html",
        plantas=plantas
    )


@planta_bp.route(
    "/plantas",
    methods=["POST"]
)
@login_required
def crear_planta():

    user = supabase.auth.get_user()

    service.crear_planta(
        user_id=user.user.id,
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
@login_required
def detalle_planta(planta_id):

    user = supabase.auth.get_user()

    planta = service.obtener_por_id_y_usuario(
        planta_id,
        user.user.id
    )

    return render_template(
        "plantas/detalle_planta.html",
        planta=planta
    )


@planta_bp.route(
    "/plantas/<int:planta_id>/delete",
    methods=["POST"]
)
@login_required
def eliminar_planta(planta_id):

    user = supabase.auth.get_user()

    service.eliminar_planta(
        planta_id,
        user.user.id
    )
    
    return redirect(
        url_for("planta.listar_plantas")
    )