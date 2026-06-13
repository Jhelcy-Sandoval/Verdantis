from app.infrastructure.models.medicion_model import Medicion
from app.infrastructure.repositories.medicion_repository import MedicionRepository


class MedicionService:

    def __init__(self):

        self.repository = MedicionRepository()


    def listar_mediciones_por_planta(self, planta_id):

        return self.repository.listar_por_planta(planta_id)


    def crear_medicion(
        self,
        planta_id,
        temperatura,
        humedad,
        desarrollo,
        observaciones=None
    ):

        medicion = Medicion(
            planta_id=int(planta_id),
            temperatura=float(temperatura),
            humedad=float(humedad),
            desarrollo=float(desarrollo),
            observaciones=observaciones
        )

        return self.repository.guardar(
            medicion
        )