from app.infrastructure.models.especie_model import Especie
from app import db
from sqlalchemy import or_

class EspecieRepository:
    
    def listar_especies(
        self,
        user_id=None,
        search=None,
        difficulty=None,
        growth=None,
        origin=None
    ):

        query = Especie.query

        if origin == "global":

            query = query.filter(
                Especie.user_id.is_(None)
            )

        elif origin == "custom":

            query = query.filter(
                Especie.user_id == user_id
            )

        else:

            query = query.filter(
                (Especie.user_id == user_id)
                |
                (Especie.user_id.is_(None))
            )

        if search:

            query = query.filter(
                Especie.name.ilike(
                    f"%{search}%"
                )
            )

        if difficulty:

            query = query.filter(
                Especie.difficulty_level
                == difficulty
            )

        if growth:

            query = query.filter(
                Especie.expected_growth_rate
                == growth
            )

        return query.order_by(
            Especie.name.asc()
        ).all()

    def obtener_por_id(
        self,
        especie_id,
        user_id
    ):

        return (
            Especie.query
            .filter(
                Especie.id == especie_id,
                or_(
                    Especie.user_id == user_id,
                    Especie.user_id.is_(None)
                )
            )
            .first()
        )

    def guardar(
        self,
        especie
    ):

        db.session.add(
            especie
        )

        db.session.commit()

        return especie

    def actualizar(
        self,
        especie
    ):

        db.session.commit()

        return especie

    def eliminar(
        self,
        especie
    ):

        db.session.delete(
            especie
        )

        db.session.commit()