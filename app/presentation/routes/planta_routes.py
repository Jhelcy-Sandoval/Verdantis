from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash

from app.application.services.planta_service import PlantaService
from app.application.services.especie_service import EspecieService
from app.application.services.locations_service import LocationsService
from app.application.services.medicionplanta_service import MedicionPlantaService
from app.application.services.medicion_service import MedicionService

from app.infrastructure.auth.auth_guard import login_required
from app.infrastructure.auth.supabase_client import supabase

planta_bp = Blueprint(
    "planta",
    __name__
)

service = PlantaService()
service_especies = EspecieService()
service_locations = LocationsService()
service_mediciones = MedicionPlantaService()
service_medicion_ambiental = MedicionService()

@planta_bp.route("/")
@login_required
def listar_plantas():
    try:

        user = supabase.auth.get_user()
        
        
        search = request.args.get("search")
        status = request.args.get("status")
        location = request.args.get("location")

        plantas = service.listar_plantas_por_usuario(
            user.user.id,
            search=search,
            status=status,
            location=location
        )
        
        locations = service_locations.listar_todas_locations(
            user.user.id
        )
        
        resumen = service.obtener_resumen(
            user.user.id
        )
        
        especies = service_especies.listar_todas_especies(
            user.user.id
        )
        
        return render_template(
            "plantas/listar.html",
            especies=especies,
            plantas=plantas,
            locations=locations,
            **resumen
        )
    
    except Exception as e:
        print(f"Error listar plantas: {e}")

        return render_template(
            "errors/500.html"
        ), 500


@planta_bp.route(
    "/",
    methods=["POST"]
)
@login_required
def crear_planta():

    try:

        user = supabase.auth.get_user()
        photo = request.files.get("photo")

        service.crear_planta(
            user_id=user.user.id,
            tag=request.form["tag"],
            common_name=request.form["common_name"],
            especie_id=request.form["especie_id"],
            germination_date=request.form["germination_date"],
            initial_conditions=request.form.get("initial_conditions"),
            variety=request.form.get("variety"),
            location_id=request.form["location_id"],
            photo=photo
        )

        flash(
            "Planta creada correctamente.",
            "success"
        )

        return redirect(
            url_for("planta.listar_plantas")
        )

    except ValueError as e:

        flash(
            str(e),
            "warning"
        )

        return redirect(
            url_for("planta.listar_plantas")
        )

    except Exception as e:

        print(f"Error creando planta: {e}")

        flash(
            "Ocurrió un error al crear la planta.",
            "danger"
        )

        return redirect(
            url_for("planta.listar_plantas")
        )

    except Exception as e:
        
        flash(
            "Ocurrió un error al crear la especie.",
            "danger"
        )

        print(f"Error creando planta: {e}")

        return render_template(
            "errors/500.html"
        ), 500


@planta_bp.route("/<int:planta_id>")
@login_required
def detalle_planta(planta_id):

    try: 

        user = supabase.auth.get_user()

        planta = service.obtener_por_id_y_usuario(
            planta_id,
            user.user.id
        )

        if not planta:

            flash(
                "La planta no existe.",
                "warning"
            )

            return redirect(
                url_for("planta.listar_plantas")
            )
            
        search = request.args.get("search")
        salud = request.args.get("salud")
        plagas = request.args.get("plagas")
        enfermedad = request.args.get("enfermedad")
        
        if plagas == "":
            plagas = None
        elif plagas == "True":
            plagas = True
        elif plagas == "False":
            plagas = False

        if enfermedad == "":
            enfermedad = None
        elif enfermedad == "True":
            enfermedad = True
        elif enfermedad == "False":
            enfermedad = False

        mediciones = service_mediciones.listar_por_planta(
            planta_id,
            search=search,
            salud=salud,
            plagas=plagas,
            enfermedad=enfermedad
        )

        ultima_medicion = service_mediciones.ultima_medicion(
            planta_id
        )
        
        location_id = planta.location_id
        
        medicion_ambiental = service_medicion_ambiental.ultima_medicion(
            user.user.id,
            location_id
        )

        resumen = service_mediciones.obtener_resumen(
            planta_id
        )

        return render_template(
            "plantas/detalle_planta.html",
            planta=planta,
            mediciones=mediciones,
            ultima_medicion=ultima_medicion,
            medicion_ambiental=medicion_ambiental,
            **resumen
        )

    except Exception as e:

        print(f"Error obteniendo planta: {e}")

        return render_template(
            "errors/500.html"
        ), 500


@planta_bp.route(
    "/<int:planta_id>/delete",
    methods=["POST"]
)
@login_required
def eliminar_planta(planta_id):
    
    try:

        user = supabase.auth.get_user()

        service.eliminar_planta(
            planta_id,
            user.user.id
        )
        
        flash(
            "Planta eliminada correctamente",
            "success"
        )
        
        return redirect(
            url_for("planta.listar_plantas")
        )  
         
    except Exception as e:
        
        flash(
            "Ocurrió un error al eliminar la planta.",
            "danger"
        )
        print(f"Error eliminando planta: {e}")

        return render_template(
            "errors/500.html"
        ), 500
        
@planta_bp.route(
    "/<int:planta_id>/mediciones",
    methods=["POST"]
)
@login_required
def crear_medicion_planta(planta_id):

    try:

        user = supabase.auth.get_user()

        photo = request.files.get("photo")

        service_mediciones.crear_medicion(

            user_id=user.user.id,

            planta_id=planta_id,

            altura=float(request.form["altura"]),

            numero_hojas=int(
                request.form["numero_hojas"]
            ) if request.form.get("numero_hojas") else None,
            
            diametro_tallo=float(
                request.form["diametro_tallo"]
            ) if request.form.get("diametro_tallo") else None,

            humedad_sustrato=float(
                request.form["humedad_sustrato"]
            ) if request.form.get("humedad_sustrato") else None,

            desarrollo=float(
                request.form["desarrollo"]
            ) if request.form.get("desarrollo") else None,
            
            numero_flores=int(
                request.form["numero_flores"]
            ) if request.form.get("numero_flores") else None,

            numero_frutos=int(
                request.form["numero_frutos"]
            ) if request.form.get("numero_frutos") else None,

            color_hojas=request.form.get(
                "color_hojas"
            ),

            plagas="plagas" in request.form,

            enfermedad="enfermedad" in request.form,

            observaciones=request.form.get(
                "observaciones"
            ),

            photo=photo
        )

        flash(
            "Inspección registrada correctamente.",
            "success"
        )

    except Exception as e:

        print(
            f"Error creando inspección: {e}"
        )

        flash(
            "No fue posible registrar la inspección.",
            "danger"
        )

    return redirect(
        url_for(
            "planta.detalle_planta",
            planta_id=planta_id
        )
    )
    
@planta_bp.route(
    "/mediciones/<int:medicion_id>/delete",
    methods=["POST"]
)
@login_required
def eliminar_medicion_planta(medicion_id):

    try:

        user = supabase.auth.get_user()

        medicion = service_mediciones.detalle_medicion(
            medicion_id,
            user.user.id
        )

        if not medicion:

            flash(
                "La inspección no existe.",
                "warning"
            )

            return redirect(
                url_for("planta.listar_plantas")
            )

        planta_id = medicion.planta_id

        service_mediciones.eliminar_medicion(
            medicion_id,
            user.user.id
        )

        flash(
            "Inspección eliminada correctamente.",
            "success"
        )

        return redirect(
            url_for(
                "planta.detalle_planta",
                planta_id=planta_id
            )
        )

    except Exception as e:

        print(
            f"Error eliminando inspección: {e}"
        )

        flash(
            "Ocurrió un error al eliminar la inspección.",
            "danger"
        )

        return redirect(
            url_for("planta.listar_plantas")
        )