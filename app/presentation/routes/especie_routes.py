from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash

from app.application.services.especie_service import EspecieService
from app.application.services.planta_service import PlantaService
from app.infrastructure.auth.auth_guard import login_required
from app.infrastructure.auth.supabase_client import supabase


especie_bp = Blueprint(
    "especie",
    __name__ 
)

service = EspecieService()
service_plantas = PlantaService()

@especie_bp.route("/")
@login_required
def listar_especies():

    try:

        user = supabase.auth.get_user()

        search = request.args.get(
            "search"
        )

        difficulty = request.args.get(
            "difficulty"
        )

        growth = request.args.get(
            "growth"
        )

        origin = request.args.get(
            "origin"
        )

        especies = service.listar_todas_especies(
            user_id=user.user.id,
            search=search,
            difficulty=difficulty,
            growth=growth,
            origin=origin
        )

        resumen = service.obtener_resumen(
            user.user.id
        )

        return render_template(
            "especies/listar.html",
            especies=especies,
            **resumen
        )

    except Exception as e:

        print(
            f"Error obteniendo especies: {e}"
        )

        return render_template(
            "errors/500.html"
        ), 500
        
@especie_bp.route(
    "/",
    methods=["POST"]
)
@login_required
def guardar_especie():
    try:
        
        user = supabase.auth.get_user()
        
        photo = request.files.get("photo") 
        
        service.create_especie(
            user_id=user.user.id,
            name=request.form["name"],
            scientific_name=request.form["scientific_name"],
            description=request.form["description"],
            ideal_humidity_min = request.form["ideal_humidity_min"],
            ideal_humidity_max = request.form["ideal_humidity_max"],
            ideal_temperature_min = request.form["ideal_temperature_min"],
            ideal_temperature_max = request.form["ideal_temperature_max"],
            expected_growth_rate = request.form["expected_growth_rate"],
            average_germination_days = request.form["average_germination_days"],
            average_transplant_days = request.form["average_transplant_days"],
            sunlight_requirement = request.form["sunlight_requirement"],
            watering_frequency_days = request.form["watering_frequency_days"],
            difficulty_level = request.form["difficulty_level"],
            photo=photo
        )
        
        flash(
            "Especie creada correctamente",
            "success"
        )

        return redirect(
            url_for("especie.listar_especies")
        )

    except Exception as e:

        if "especies_name_key" in str(e):

            flash(
                "Ya existe una especie con ese nombre.",
                "warning"
            )

            return redirect(
                url_for("especie.listar_especies")
            )

        print(e)

        flash(
            "Ocurrió un error al crear la especie.",
            "danger"
        )

        return redirect(
            url_for("especie.listar_especies")
        )
        
        
@especie_bp.route(
    "/<int:especie_id>"
)
@login_required
def detalle_especie(especie_id):
    
    try:
        print(especie_id)

        user = supabase.auth.get_user()

        especie = service.obtener_por_id(
            especie_id,
            user.user.id
        )
        
        plantas = service_plantas.plantas_especie(
            user.user.id,
            especie_id
        )

        return render_template(
            "especies/detalle_especie.html",
            especie=especie,
            plantas=plantas
        )
    
    except Exception as e:
        print(f"Error obtener especie: {e}")

        return render_template(
            "errors/500.html"
        ), 500
        
@especie_bp.route(
    "/<int:especie_id>",
    methods=["POST"]
)
@login_required
def eliminar_especie(especie_id):
    try:
        user = supabase.auth.get_user()
        
        especie = service.eliminar_especie(
            especie_id,
            user.user.id
        )
        
        flash(
            "Especie eliminada correctamente",
            "success"
        )
        
        return redirect(
                url_for("especie.listar_especies")
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