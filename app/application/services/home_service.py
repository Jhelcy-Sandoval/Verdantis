from app.application.services.planta_service import PlantaService
from app.application.services.especie_service import EspecieService
from app.application.services.medicion_service import MedicionService
from app.application.services.locations_service import LocationsService
from app.application.services.medicionplanta_service import MedicionPlantaService

from datetime import datetime

class HomeService:

    def __init__(self):

        self.planta_service = PlantaService()
        self.especie_service = EspecieService()
        self.medicion_service = MedicionService()
        self.location_service = LocationsService()
        self.medicion_planta_service = MedicionPlantaService()

    def obtener_dashboard(
        self,
        user_id
    ):

        return {

            "cards": {

                "plantas": self.planta_service.obtener_resumen(
                    user_id
                ),

                "especies": self.especie_service.obtener_resumen(
                    user_id
                ),

                "ubicaciones": self.location_service.obtener_resumen(
                    user_id
                ),

                "mediciones": self.medicion_service.obtener_resumen(
                    user_id
                ),

                "inspecciones": self.medicion_planta_service.obtener_resumen_home(
                    user_id
                )

            },

            "estado_vivero": self.obtener_estado_vivero(
                user_id
            ),

            "estado_ubicaciones": self.obtener_estado_ubicaciones(
                user_id
            ),

            "condiciones": self.medicion_service.obtener_resumen(
                user_id
            ),

            "distribucion": self.obtener_distribucion_vivero(
                user_id
            ),

            "alertas": self.obtener_alertas(
                user_id
            ),

            "ultimas_inspecciones": self.obtener_ultimas_inspecciones(
                user_id
            ),

            "actividad": self.obtener_actividad_reciente(
                user_id
            )

        }
        
    def obtener_estado_vivero(
        self,
        user_id
    ):

        plantas = self.planta_service.listar_plantas_por_usuario(
            user_id
        )

        optimas = 0
        observacion = 0
        criticas = 0

        for planta in plantas:

            ultima = self.medicion_planta_service.ultima_medicion(
                planta.id
            )

            if not ultima:
                continue

            if ultima.salud == "Óptima":
                optimas += 1

            elif ultima.salud == "Atención":
                observacion += 1

            else:
                criticas += 1

        return {

            "optimas": optimas,

            "observacion": observacion,

            "criticas": criticas,

            "total": optimas + observacion + criticas

        }
        
    def obtener_estado_ubicaciones(
        self,
        user_id
    ):

        locations = self.location_service.listar_todas_locations(
            user_id
        )

        resultado = []

        for location in locations:

            resultado.append({

                "id": location.id,

                "nombre": location.name,

                "estado": location.health_status or "Sin datos",

                "plantas": location.plants_count,

                "especies": location.species_count

            })

        return resultado
    
    def obtener_distribucion_vivero(
        self,
        user_id
    ):

        locations = self.location_service.listar_todas_locations(
            user_id
        )

        return [

            {

                "nombre": location.name,

                "plantas": location.plants_count,

                "especies": location.species_count

            }

            for location in locations

        ]
        
        
    def obtener_alertas(
        self,
        user_id
    ):

        alertas = []

        inspecciones = self.medicion_planta_service.listar_todas(
            user_id
        )

        for inspeccion in inspecciones:

            if inspeccion.salud == "Óptima":
                continue

            if inspeccion.plagas:

                descripcion = "Plagas detectadas"

            elif inspeccion.enfermedad:

                descripcion = "Enfermedad detectada"

            elif inspeccion.humedad_sustrato < 40:

                descripcion = "Humedad del sustrato baja"

            elif inspeccion.humedad_sustrato > 80:

                descripcion = "Exceso de humedad"

            else:

                descripcion = "Inspección requiere revisión"

            alertas.append({

                "tipo": "Planta",

                "titulo": inspeccion.planta.common_name,

                "descripcion": descripcion,

                "estado": inspeccion.salud,

                "fecha": inspeccion.fecha_registro

            })

        return sorted(
            alertas,
            key=lambda x: x["fecha"],
            reverse=True
        )[:6]
        
    def obtener_ultimas_inspecciones(
        self,
        user_id
    ):

        inspecciones = self.medicion_planta_service.listar_todas(
            user_id
        )

        return sorted(
            inspecciones,
            key=lambda x: x.fecha_registro,
            reverse=True
        )[:5]
        

    def obtener_actividad_reciente(
        self,
        user_id
    ):

        actividades = []

        plantas = self.planta_service.listar_plantas_por_usuario(
            user_id
        )

        for planta in plantas:

            actividades.append({

                "tipo": "planta",

                "titulo": f"Planta registrada: {planta.common_name}",

                "descripcion": f"Etiqueta {planta.tag}",

                "fecha": datetime.combine(
                    planta.germination_date,
                    datetime.min.time()
                )

            })

        inspecciones = self.medicion_planta_service.listar_todas(
            user_id
        )

        for inspeccion in inspecciones:

            actividades.append({

                "tipo": "inspeccion",

                "titulo": f"Inspección de {inspeccion.planta.common_name}",

                "descripcion": inspeccion.salud,

                "fecha": inspeccion.fecha_registro

            })

        mediciones = self.medicion_service.listar_todas(
            user_id
        )

        for medicion in mediciones:

            actividades.append({

                "tipo": "medicion",

                "titulo": f"Medición ambiental en {medicion.locations.name}",

                "descripcion": medicion.estado,

                "fecha": medicion.fecha_registro

            })

        actividades = sorted(
            actividades,
            key=lambda actividad: actividad["fecha"],
            reverse=True
        )

        return actividades[:8]