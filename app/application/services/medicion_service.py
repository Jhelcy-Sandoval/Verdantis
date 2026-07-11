from app.infrastructure.models.medicion_model import Medicion
from app.infrastructure.repositories.medicion_repository import MedicionRepository
from app.application.services.location_profile_service import LocationProfileService
from app.application.services.locations_service import LocationsService

class MedicionService:

    def __init__(self):
        self.repository = MedicionRepository()
        self.location_service = LocationsService()
        self.location_profile_service = LocationProfileService()

    def listar_todas(
        self,
        user_id,
        search=None,
        location_id=None
    ):

        mediciones = self.repository.listar_todas(
            user_id=user_id,
            search=search,
            location_id=location_id
        )

        return mediciones
    
    def obtener_resumen(self, user_id):

        mediciones = self.repository.listar_todas(
            user_id=user_id
        )

        total_mediciones = len(mediciones)

        if total_mediciones == 0:

            return {

                "total_mediciones": 0,

                "vs_mes_anterior": "+0%",

                "humedad_promedio": 0,
                "variacion_humedad": "0%",

                "temperatura_promedio": 0,
                "variacion_temperatura": "0%",

                "mediciones_alerta": 0,
                "porcentaje_alerta": "0%"
            }

        humedad_promedio = round(
            sum(
                medicion.humedad
                for medicion in mediciones
            ) / total_mediciones,
            1
        )

        temperatura_promedio = round(
            sum(
                medicion.temperatura
                for medicion in mediciones
            ) / total_mediciones,
            1
        )

        mediciones_alerta = len([
            medicion
            for medicion in mediciones
            if medicion.estado in [
                "Atención",
                "Crítico"
            ]
        ])
        porcentaje_alerta = round(
            (mediciones_alerta / total_mediciones) * 100,
            1
        )

        return {

            "total_mediciones": total_mediciones,

            "vs_mes_anterior": "+0%",

            "humedad_promedio": humedad_promedio,
            "variacion_humedad": "+0%",

            "temperatura_promedio": temperatura_promedio,
            "variacion_temperatura": "+0%",

            "mediciones_alerta": mediciones_alerta,
            "porcentaje_alerta": f"{porcentaje_alerta}%"
        }
        
    def ultima_medicion(
        self,
        user_id,
        location_id=None
    ):
        return self.repository.ultima_medicion(
            user_id=user_id,
            location_id=location_id
        )

    def listar_mediciones_por_planta(
        self,
        planta_id
    ):

        mediciones = self.repository.listar_por_planta(
            planta_id
        )

        return mediciones or []

    def crear_medicion(
        self,
        user_id,
        location_id,
        temperatura,
        humedad,
        desarrollo,
        observaciones=None
    ):

        location = self.location_service.detalle_location(
            user_id=user_id,
            location_id=location_id
        )

        if not location:
            raise ValueError(
                "La ubicación no existe."
            )

        temperatura = float(temperatura)
        humedad = float(humedad)

        estado = self.location_profile_service.obtener_estado(
            location,
            temperatura,
            humedad
        )

        medicion = Medicion(
            user_id=user_id,
            location_id=int(location_id),
            temperatura=temperatura,
            humedad=humedad,
            desarrollo=float(desarrollo),
            observaciones=observaciones,
            estado=estado
        )

        location.health_status = estado

        self.location_service.actualizar_location(
            user_id=user_id,
            location_id=location_id,
            location=location
        )

        medicion = self.repository.guardar(
            medicion
        )

        return medicion

    def detalle_medicion(
        self,
        medicion_id,
        user_id
    ):

        return self.repository.obtener_por_id(
            user_id,
            medicion_id
        ) 
        
    def eliminar_medicion(
        self,
        medicion_id,
        user_id
    ):
        
        medicion = self.repository.obtener_por_id(
            medicion_id,
            user_id
        )
        
        if medicion:

            self.repository.eliminar(
                medicion
            )

            return True

        return False
        