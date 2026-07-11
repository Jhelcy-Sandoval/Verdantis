from app.infrastructure.models.planta_model import Planta
from app.infrastructure.repositories.planta_repository import PlantaRepository
from app.infrastructure.storage.supabase_storage import SupabaseStorage

from app.application.services.location_profile_service import LocationProfileService
from app import db

class PlantaService:

    def __init__(self):
        self.repository = PlantaRepository()
        self.storage = SupabaseStorage()
        self.location_profile_service = LocationProfileService()

    def listar_plantas_por_usuario(
        self,
        user_id,
        search=None,
        status=None,
        location=None
    ):
        return self.repository.listar_por_usuario(
            user_id,
            search=search,
            status=status,
            location=location
        )

    def obtener_resumen(self, user_id):

        plantas = self.repository.listar_por_usuario(
            user_id
        )

        total_plantas = len(plantas)

        estados_saludables = [
            "Germinación",
            "Crecimiento",
            "Saludable"
        ]

        estados_observacion = [
            "Observación",
            "Trasplante",
            "Recuperación"
        ]

        estados_alerta = [
            "Alerta",
            "Crítico"
        ]

        plantas_saludables = len([
            planta
            for planta in plantas
            if planta.status in estados_saludables
        ])

        plantas_observacion = len([
            planta
            for planta in plantas
            if planta.status in estados_observacion
        ])

        plantas_alerta = len([
            planta
            for planta in plantas
            if planta.status in estados_alerta
        ])

        porcentaje_saludables = (
            round(
                (plantas_saludables / total_plantas) * 100,
                1
            )
            if total_plantas > 0
            else 0
        )

        porcentaje_observacion = (
            round(
                (plantas_observacion / total_plantas) * 100,
                1
            )
            if total_plantas > 0
            else 0
        )

        porcentaje_alerta = (
            round(
                (plantas_alerta / total_plantas) * 100,
                1
            )
            if total_plantas > 0
            else 0
        )

        return {

            "total_plantas": total_plantas,

            "vs_mes_anterior": "+0%",

            "plantas_saludables": plantas_saludables,
            "porcentaje_saludables": f"{porcentaje_saludables}%",

            "plantas_observacion": plantas_observacion,
            "porcentaje_observacion": f"{porcentaje_observacion}%",

            "plantas_alerta": plantas_alerta,
            "porcentaje_alerta": f"{porcentaje_alerta}%"
        }
    
    def obtener_por_id_y_usuario(
        self,
        planta_id,
        user_id
    ):

        return self.repository.obtener_por_id_y_usuario(
            planta_id,
            user_id
        )

    def crear_planta(
        self,
        user_id,
        tag,
        common_name,
        especie_id,
        germination_date,
        initial_conditions,
        location_id,
        photo=None,
        variety=None,
    ):

        if self.repository.obtener_por_tag(tag):
            raise ValueError(
                "Ya existe una planta registrada con ese tag."
            )

        photo_url = None

        if photo and photo.filename:
            photo_url = self.storage.upload_image(photo)

        try:

            planta = Planta(
                user_id=user_id,
                tag=tag,
                common_name=common_name,
                especie_id=especie_id,
                germination_date=germination_date,
                initial_conditions=initial_conditions,
                variety=variety,
                location_id=location_id,
                photo_url=photo_url
            )

            planta = self.repository.guardar(planta)

            self.location_profile_service.actualizar_perfil(
                location_id=location_id,
                user_id=user_id
            )

            return planta

        except Exception:
            db.session.rollback()
            raise
    
    def eliminar_planta(
        self,
        planta_id,
        user_id
    ):

        planta = self.repository.obtener_por_id_y_usuario(
            planta_id,
            user_id
        )

        if planta:

            self.repository.eliminar(
                planta
            )

            return True

        return False
    
    def plantas_especie(
        self,
        user_id,
        especie_id
    ):

        plantas = self.repository.listar_por_usuario(
            user_id=user_id
        )

        return [
            planta
            for planta in plantas
            if planta.especie_id == especie_id
        ]