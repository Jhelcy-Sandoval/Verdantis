from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash

from app.application.services.locations_service import LocationsService
from app.infrastructure.auth.auth_guard import login_required
from app.infrastructure.auth.supabase_client import supabase

locations_bp = Blueprint(
    "locations",
    __name__ 
)

service = LocationsService()

@locations_bp.route("/")
@login_required
def listar_locations():
    try:
        user = supabase.auth.get_user()
        
        search = request.args.get(
            "search"
        )
        
        locations = service.listar_todas_locations(
            user.user.id,
            search=search
        )
        
        print(f"locations", locations)

        return render_template(
            "locations/listar.html",
            locations=locations
        )
        
    except Exception as e:
        print(f"Error obteniendo ubicaciones: {e}")

        return render_template(
            "errors/500.html"
        ), 500

@locations_bp.route(
    "/",
    methods=["POST"]
)
@login_required
def guardar_ubicacion():
    try:
        
        user = supabase.auth.get_user()
        
        service.guardar_ubicacion(
            user_id = user.user.id,
            name = request.form["name"],
            description = request.form["description"]
        )
        
        flash(
            "Ubicacion creada correctamente",
            "success"
        )

        return redirect(
            url_for("locations.listar_locations")
        )

    except Exception as e:

        if "location_name_key" in str(e):

            flash(
                "Ya existe una ubicacion con ese nombre.",
                "warning"
            )

            return redirect(
                url_for("locations.listar_locations")
            )

        print(e)

        flash(
            "Ocurrió un error al crear la ubicacion.",
            "danger"
        )

        return redirect(
            url_for("locations.listar_locations")
        )
        
@locations_bp.route(
    "/<int:location_id>",
    methods=["POST"]
)
@login_required
def detalle_location(location_id):
    try:
        user = supabase.auth.get_user()
        
        location = service.obtener_por_id(
            location_id,
            user.user.id
        )
        
        return render_template(
            location=location
        )

    except Exception as e:
        print(f"Error obtener ubicación: {e}")

        return render_template(
            "errors/500.html"
        ), 500


@locations_bp.route(
    "/<int:location_id>",
    methods=["POST"]
)
@login_required
def eliminar_location(location_id):
    try:
        user = supabase.auth.get_user()
        
        location = service.eliminar_ubicacion(
            user.user.id,
            location_id
        )
        
        flash(
            "Ubicacion eliminada correctamente",
            "success"
        )
        
        return redirect(
                url_for("locations.listar_locations")
        )

    except Exception as e:
            
            flash(
                "Ocurrió un error al eliminar la ubicacion.",
                "danger"
            )
            print(f"Error al eliminar ubicacion: {e}")

            return render_template(
                "errors/500.html"
            ), 500