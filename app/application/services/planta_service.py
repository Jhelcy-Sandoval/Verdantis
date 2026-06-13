from app.infrastructure.models.planta_model import Planta
from app.infrastructure.repositories.planta_repository import PlantaRepository


class PlantaService:

    def __init__(self):
        self.repository = PlantaRepository()

    def listar_plantas(self):
        return self.repository.obtener_todas()

    def obtener_por_id(self, id):
        return self.repository.obtener_por_id(id)

    def crear_planta(
        self,
        tag,
        species,
        germination_date,
        initial_conditions
    ):

        planta = Planta(
            tag=tag,
            species=species,
            germination_date=germination_date,
            initial_conditions=initial_conditions
        )

        self.repository.guardar(planta)

    def eliminar_planta(self, id):

        planta = self.repository.obtener_por_id(id)

        if planta:
            self.repository.eliminar(planta)