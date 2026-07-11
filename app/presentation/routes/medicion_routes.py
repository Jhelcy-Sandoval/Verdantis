from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash

from app.application.services.medicion_service import MedicionService
from app.infrastructure.auth.auth_guard import login_required
from app.infrastructure.auth.supabase_client import supabase
from app.application.services.locations_service import LocationsService

medicion_bp = Blueprint("mediciones", __name__)

service = MedicionService()
locations_service = LocationsService()

@medicion_bp.route("/")
@login_required
def listar_todas_mediciones():
    
    try:
        user = supabase.auth.get_user()

        mediciones = service.listar_todas(
            user_id=user.user.id
        )

        return render_template(
            "mediciones/listar.html",
            mediciones=mediciones
        )
    
    except Exception as e:
        
        print(
            f"Error obteniendo mediciones: {e}"
        )

        return render_template(
            "errors/500.html"
        )
        
@medicion_bp.route("/locations")
@login_required
def listar_mediciones_ubicaciones():

    try:

        user = supabase.auth.get_user()

        search = request.args.get("search")
        location = request.args.get("location")
        location_id = request.args.get("location_id")
        
        locations = locations_service.listar_todas_locations(
            user.user.id,
        ) 

        mediciones = service.listar_todas(
            user_id=user.user.id,
            search=search,
            location_id=location
        )
        
        ultima_medicion = service.ultima_medicion(
            user_id=user.user.id,
            location_id=location_id
        )
        
        resumen = service.obtener_resumen(
            user.user.id
        )       
                
        return render_template(
            "mediciones/listar_locations.html",
            mediciones=mediciones,
            locations=locations,
            ultima_medicion=ultima_medicion,
            **resumen
        )

    except Exception as e:
        
        print(f"Error al obtener las mediciones.: {e}")

        return render_template(
            "errors/500.html"
        ), 500

@medicion_bp.route("/<int:medicion_id>")
@login_required
def detalle_medicion(medicion_id):
    
    try:
        
        user = supabase.auth.get_user()

        medicion = service.detalle_medicion(
            user.user.id,
            medicion_id
        )
        
        location = locations_service.detalle_location(
            user_id = user.user.id,
            location_id=medicion.location_id
        )

        return render_template(
            "mediciones/detalle_medicion.html",
            medicion=medicion,
            location=location
        )
        
    except Exception as e:
        
        print(
            f"Error obteniendo medicion: {e}"
        )

        return render_template(
            "errors/500.html"
        )

@medicion_bp.route(
    "/",
    methods=["POST"]
)
@login_required
def crear_medicion():

    try:

        user = supabase.auth.get_user()
        
        service.crear_medicion(
            user_id=user.user.id,
            location_id=int(request.form["location_id"]),
            temperatura=float(request.form["temperatura"]),
            humedad=float(request.form["humedad"]),
            desarrollo=float(request.form["desarrollo"]),
            observaciones=request.form.get("observaciones")
        )

        flash(
            "Medición registrada correctamente.",
            "success"
        )

        return redirect(
            url_for("mediciones.listar_mediciones_ubicaciones")
        )

    except Exception as e:

        print(f"Error al crear medición: {e}")

        flash(
            "No fue posible registrar la medición.",
            "danger"
        )

        return redirect(
            url_for("mediciones.listar_mediciones_ubicaciones")
        )
        
@medicion_bp.route(
    "/<int:medicion_id>",
    methods=["POST"]
)
@login_required
def eliminar_medicion(medicion_id):
    try:
        user = supabase.auth.get_user()
        
        medicion = service.eliminar_medicion(
            medicion_id,
            user.user.id
        )
        
        flash(
            "Medicion eliminada correctamente",
            "success"
        )
        
        return redirect(
                url_for("mediciones.listar_mediciones_ubicaciones")
        )
        
    except Exception as e:
            
            flash(
                "Ocurrió un error al eliminar la especie.",
                "danger"
            )
            print(f"Error al eliminar especie: {e}")

            return render_template(
                "errors/500.html"
            ), 500
    