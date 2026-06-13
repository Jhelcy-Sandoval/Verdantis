from app.infrastructure.models.medicion_model import Medicion
from app import db


class MedicionRepository:

    def guardar(self, medicion):

        db.session.add(medicion)
        db.session.commit()

        return medicion


    def listar_por_planta(self, planta_id):

        return (
            Medicion.query
            .filter_by(planta_id=planta_id)
            .all()
        )


    def obtener_ultima_medicion(self, planta_id):

        return (
            Medicion.query
            .filter_by(planta_id=planta_id)
            .order_by(Medicion.fecha_registro.desc())
            .first()
        )


    def obtener_por_id(self, medicion_id):

        return Medicion.query.get(medicion_id)


    def eliminar(self, medicion):

        db.session.delete(medicion)
        db.session.commit()