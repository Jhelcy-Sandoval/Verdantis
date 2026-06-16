from app.infrastructure.models.planta_model import Planta
from app.infrastructure.repositories.planta_repository import PlantaRepository


class PlantaService:

    def __init__(self):
        self.repository = PlantaRepository()

    def listar_plantas_por_usuario(
        self,
        user_id
    ):

        return self.repository.listar_por_usuario(
            user_id
        )

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
        species,
        germination_date,
        initial_conditions
    ):

        planta = Planta(
            user_id=user_id,
            tag=tag,
            species=species,
            germination_date=germination_date,
            initial_conditions=initial_conditions
        )

        return self.repository.guardar(
            planta
        )

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