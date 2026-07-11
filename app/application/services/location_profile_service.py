from datetime import datetime

from app import db
from app.infrastructure.repositories.locations_repository import LocationsRepository


class LocationProfileService:

    def __init__(self):
        self.repository = LocationsRepository()

    def actualizar_perfil(self, location_id, user_id):

        location = self.repository.obtener_por_id(location_id, user_id)

        if not location:
            return None

        rangos = self.calcular_rangos(location)

        location.ideal_temperature_min = rangos["ideal_temperature_min"]
        location.ideal_temperature_max = rangos["ideal_temperature_max"]

        location.ideal_humidity_min = rangos["ideal_humidity_min"]
        location.ideal_humidity_max = rangos["ideal_humidity_max"]

        location.plants_count = len(location.plantas)

        location.species_count = len({
            planta.especie.id
            for planta in location.plantas
        })

        location.profile_updated_at = datetime.utcnow()

        db.session.commit()

        return location

    def calcular_rangos(self, location):
    
        plantas = location.plantas

        if not plantas:

            return {

                "ideal_temperature_min": None,
                "ideal_temperature_max": None,

                "ideal_humidity_min": None,
                "ideal_humidity_max": None

            }

        especies = [
            planta.especie
            for planta in plantas
            if planta.especie
        ]

        cantidad = len(especies)

        return {

            "ideal_temperature_min": round(
                sum(
                    e.ideal_temperature_min
                    for e in especies
                ) / cantidad,
                1
            ),

            "ideal_temperature_max": round(
                sum(
                    e.ideal_temperature_max
                    for e in especies
                ) / cantidad,
                1
            ),

            "ideal_humidity_min": round(
                sum(
                    e.ideal_humidity_min
                    for e in especies
                ) / cantidad,
                1
            ),

            "ideal_humidity_max": round(
                sum(
                    e.ideal_humidity_max
                    for e in especies
                ) / cantidad,
                1
            )

        }

    def calcular_compatibilidad(
        self,
        location,
        especie
    ):

        if (
            location.ideal_temperature_min is None
            or location.ideal_temperature_max is None
        ):

            return {

                "compatible": True,
                "score": 100,
                "mensaje": "La ubicación aún no tiene plantas."

            }

        score = 0


        if (
            especie.ideal_temperature_min
            <= location.ideal_temperature_max
            and especie.ideal_temperature_max
            >= location.ideal_temperature_min
        ):

            score += 50


        if (
            especie.ideal_humidity_min
            <= location.ideal_humidity_max
            and especie.ideal_humidity_max
            >= location.ideal_humidity_min
        ):

            score += 50

        return {

            "compatible": score >= 70,

            "score": score,

            "mensaje": (
                "Compatible"
                if score >= 70
                else "No recomendado"
            )

        }

    def obtener_estado(
        self,
        location,
        temperatura,
        humedad
    ):

        if (
            location.ideal_temperature_min is None
            or location.ideal_temperature_max is None
            or location.ideal_humidity_min is None
            or location.ideal_humidity_max is None
        ):
            return "Sin configurar"

        temperatura_ok = (
            location.ideal_temperature_min
            <= temperatura
            <= location.ideal_temperature_max
        )

        humedad_ok = (
            location.ideal_humidity_min
            <= humedad
            <= location.ideal_humidity_max
        )

        if temperatura_ok and humedad_ok:
            return "Óptimo"

        if temperatura_ok or humedad_ok:
            return "Atención"

        return "Crítico"