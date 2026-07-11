from app.infrastructure.models.especie_model import Especie
from app.infrastructure.repositories.especie_repository import EspecieRepository
from app.infrastructure.storage.supabase_storage import SupabaseStorage


class EspecieService:

    def __init__(self):
        self.repository = EspecieRepository()
        self.storage = SupabaseStorage()


    def listar_todas_especies(
        self, 
        user_id=None,
        search=None,
        difficulty=None,
        growth=None,
        origin=None
    ):
        
        return self.repository.listar_especies(
            user_id=user_id,
            search=search,
            difficulty=difficulty,
            growth=growth,
            origin=origin
        )
    
    def obtener_resumen(self, user_id=None):

        especies = self.repository.listar_especies(
            user_id=user_id,
        )

        total_especies = len(especies)

        especies_faciles = len([
            especie
            for especie in especies
            if especie.difficulty_level == "Fácil"
        ])

        especies_rapidas = len([
            especie
            for especie in especies
            if especie.expected_growth_rate == "Rápido"
        ])

        especies_en_uso = len([
            especie
            for especie in especies
            if len(especie.plantas) > 0
        ])

        porcentaje_faciles = (
            round(
                (especies_faciles / total_especies) * 100,
                1
            )
            if total_especies > 0
            else 0
        )

        porcentaje_rapidas = (
            round(
                (especies_rapidas / total_especies) * 100,
                1
            )
            if total_especies > 0
            else 0
        )

        porcentaje_en_uso = (
            round(
                (especies_en_uso / total_especies) * 100,
                1
            )
            if total_especies > 0
            else 0
        )

        return {

            "total_especies": total_especies,

            "vs_mes_anterior": "+0%",

            "especies_faciles": especies_faciles,
            "porcentaje_faciles": f"{porcentaje_faciles}%",

            "especies_rapidas": especies_rapidas,
            "porcentaje_rapidas": f"{porcentaje_rapidas}%",

            "especies_en_uso": especies_en_uso,
            "porcentaje_en_uso": f"{porcentaje_en_uso}%"
        }
        
    
    
    def obtener_por_id(
        self,
        especie_id,
        user_id
    ):

        return self.repository.obtener_por_id(
            especie_id,
            user_id
        )

    def create_especie(
        self,
        user_id,
        name,
        scientific_name,
        description,
        ideal_humidity_min,
        ideal_humidity_max,
        ideal_temperature_min,
        ideal_temperature_max,
        expected_growth_rate,
        average_germination_days,
        average_transplant_days,
        sunlight_requirement,
        watering_frequency_days,
        difficulty_level,
        photo=None
    ):
        
        photo_url = None

        if photo and photo.filename:
            photo_url = self.storage.upload_image(photo)

        especie = Especie(
            user_id=user_id,
            name=name,
            scientific_name=scientific_name,
            description=description,
            ideal_humidity_min=ideal_humidity_min,
            ideal_humidity_max=ideal_humidity_max,
            ideal_temperature_min=ideal_temperature_min,
            ideal_temperature_max=ideal_temperature_max,
            expected_growth_rate=expected_growth_rate,
            average_germination_days=average_germination_days,
            average_transplant_days=average_transplant_days,
            sunlight_requirement=sunlight_requirement,
            watering_frequency_days=watering_frequency_days,
            difficulty_level=difficulty_level,
            photo_url=photo_url
        )

        return self.repository.guardar(
            especie
        )

    def eliminar_especie(
        self,
        especie_id,
        user_id
    ):

        especie = self.repository.obtener_por_id(
            especie_id,
            user_id
        )

        if especie:

            self.repository.eliminar(
                especie
            )

            return True

        return False
    