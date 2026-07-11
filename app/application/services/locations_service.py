from app.infrastructure.repositories.locations_repository import LocationsRepository
from app.infrastructure.models.locations_model import Location

class LocationsService:

    def __init__(self):
        self.repository = LocationsRepository()

    def listar_todas_locations(
        self,
        user_id,
        search=None):

        locations = self.repository.listar_locations(
            user_id=user_id,
            search=search
        )

        return locations
    
    def eliminar_ubicacion(
        self,
        user_id,
        location_id
    ):
        location = self.repository.obtener_por_id(
            location_id,
            user_id
        )
        
        if location:
            self.repository.eliminar_ubicacion(
                location
            )
            
            return True
        
        return false

    def guardar_ubicacion(
        self,
        user_id,
        name,
        description=None
    ):
        location = Location(
            user_id = user_id,
            name = name, 
            description = description
        )

        return self.repository.guardar_ubicacion(
            location
        )
        
    def detalle_location(
        self,
        user_id,
        location_id
    ):
        
        return self.repository.obtener_por_id(
            location_id,
            user_id
        )
        
    def actualizar_location(
        self,
        user_id,
        location_id,
        location
    ):

        location = self.repository.obtener_por_id(
            location_id,
            user_id
        )

        if not location:
            raise ValueError(
                "La ubicación no existe."
            )

        return self.repository.actualizar_ubicacion(
            location
        )
        
    def obtener_resumen(
        self,
        user_id
    ):

        locations = self.repository.listar_locations(
            user_id=user_id
        )

        total_ubicaciones = len(locations)

        ubicaciones_saludables = len([
            location
            for location in locations
            if location.health_status == "Óptima"
        ])

        ubicaciones_observacion = len([
            location
            for location in locations
            if location.health_status == "Observación"
        ])

        ubicaciones_criticas = len([
            location
            for location in locations
            if location.health_status == "Crítica"
        ])

        total_plantas = sum(
            location.plants_count or 0
            for location in locations
        )

        total_especies = sum(
            location.species_count or 0
            for location in locations
        )

        porcentaje_saludables = (
            round(
                (ubicaciones_saludables / total_ubicaciones) * 100,
                1
            )
            if total_ubicaciones > 0
            else 0
        )

        porcentaje_observacion = (
            round(
                (ubicaciones_observacion / total_ubicaciones) * 100,
                1
            )
            if total_ubicaciones > 0
            else 0
        )

        porcentaje_criticas = (
            round(
                (ubicaciones_criticas / total_ubicaciones) * 100,
                1
            )
            if total_ubicaciones > 0
            else 0
        )

        return {

            "total_ubicaciones": total_ubicaciones,

            "vs_mes_anterior": "+0%",

            "total_plantas": total_plantas,

            "total_especies": total_especies,

            "ubicaciones_saludables": ubicaciones_saludables,
            "porcentaje_saludables": f"{porcentaje_saludables}%",

            "ubicaciones_observacion": ubicaciones_observacion,
            "porcentaje_observacion": f"{porcentaje_observacion}%",

            "ubicaciones_criticas": ubicaciones_criticas,
            "porcentaje_criticas": f"{porcentaje_criticas}%"

        }