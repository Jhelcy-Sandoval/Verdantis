from app.infrastructure.models.planta_model import Planta
from app import db


class PlantaRepository:

    def listar_por_usuario(
        self,
        user_id,
        search=None,
        status=None,
        location=None
    ):

        query = Planta.query.filter(
            Planta.user_id == user_id
        )

        if search:
            query = query.filter(
                Planta.tag.ilike(f"%{search}%")
            )

        if status:
            query = query.filter(
                Planta.status == status
            )

        if location:
            query = query.filter(
                Planta.location_id == int(location)
            )

        return query.all()

    def obtener_por_tag(
        self,
        tag
    ):
        return Planta.query.filter_by(
            tag=tag
        ).first()

    def obtener_por_id(
        self,
        planta_id
    ):
        return Planta.query.get(
            planta_id
        )

    def obtener_por_id_y_usuario(
        self,
        planta_id,
        user_id
    ):
        return Planta.query.filter_by(
            id=planta_id,
            user_id=user_id
        ).first()

    def guardar(
        self,
        planta
    ):
        db.session.add(planta)
        db.session.commit()

        return planta

    def eliminar(
        self,
        planta
    ):
        db.session.delete(planta)
        db.session.commit()