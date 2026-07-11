from app.infrastructure.models.medicion_model import Medicion
from app import db


class MedicionRepository:
    
    def listar_todas(
        self,
        user_id,
        search=None,
        location_id=None
    ):

        query = Medicion.query.filter(
            Medicion.user_id == user_id
        )

        if search:

            query = query.filter(
                Medicion.observaciones.ilike(f"%{search}%")
            )

        if location_id:

            query = query.filter(
                Medicion.locations_id == location_id
            )

        return query.order_by(
            Medicion.fecha_registro.desc()
        ).all()


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

    def ultima_medicion(
        self,
        user_id,
        location_id=None
    ):

        query = Medicion.query.filter_by(
            user_id=user_id
        )

        if location_id:
            query = query.filter_by(
                location_id=location_id
            )

        return query.order_by(
            Medicion.fecha_registro.desc()
        ).first()

    def obtener_ultima_medicion(self, planta_id):

        return (
            Medicion.query
            .filter_by(planta_id=planta_id)
            .order_by(Medicion.fecha_registro.desc())
            .first()
        )


    def obtener_por_id(self, medicion_id, user_id):
        
        return Medicion.query.filter_by(
            id=medicion_id,
            user_id=user_id
        ).first()

    def eliminar(self, medicion):

        db.session.delete(medicion)
        db.session.commit()