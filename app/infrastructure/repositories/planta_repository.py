from app.infrastructure.models.planta_model import Planta
from app import db


class PlantaRepository:

    def obtener_todas(self):
        return Planta.query.all()

    def obtener_por_id(self, id):
        return Planta.query.get(id)

    def guardar(self, planta):
        db.session.add(planta)
        db.session.commit()

    def eliminar(self, planta):
        db.session.delete(planta)
        db.session.commit()