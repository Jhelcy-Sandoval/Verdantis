from app.infrastructure.models.locations_model import Location

from app import db

class LocationsRepository:
    
    def listar_locations(
        self,
        user_id,
        search=None
    ):

        query = Location.query.filter_by(
            user_id=user_id
        )

        if search:

            query = query.filter(
                Location.name.ilike(
                    f"%{search}%"
                )
            )

        return query.all()
    
    def guardar_ubicacion(
        self,
        location
    ):
        db.session.add(
            location
        )

        db.session.commit()

        return location

    def obtener_por_id(
        self,
        location_id,
        user_id
    ):
        return Location.query.filter_by(
            id=location_id,
            user_id=user_id
        ).first()

    
    def eliminar_ubicacion(
        self,
        location
    ):
        db.session.delete(
            location
        )

        db.session.commit()
    
    def actualizar_ubicacion(
        self,
        location
    ):

        db.session.commit()

        return location