from app import db
from app.infrastructure.models.medicionplanta_model import MedicionPlanta


class MedicionPlantaRepository:
    
    def listar_todas(
        self,
        user_id
    ):
        query = MedicionPlanta.query.filter_by(
            user_id=user_id
        )
        
        return query.all()



    def listar_por_planta(
        self,
        planta_id,
        search=None,
        salud=None,
        plagas=None,
        enfermedad=None
    ):

        query = MedicionPlanta.query.filter(
            MedicionPlanta.planta_id == planta_id
        )

        if search:

            query = query.filter(
                MedicionPlanta.observaciones.ilike(
                    f"%{search}%"
                )
            )

        if salud:

            query = query.filter(
                MedicionPlanta.salud == salud
            )

        if plagas is not None:

            query = query.filter(
                MedicionPlanta.plagas == plagas
            )

        if enfermedad is not None:

            query = query.filter(
                MedicionPlanta.enfermedad == enfermedad
            )

        return (
            query
            .order_by(
                MedicionPlanta.fecha_registro.desc()
            )
            .all()
        )


    def obtener_por_id(
        self,
        medicion_id,
        user_id
    ):

        return (
            MedicionPlanta.query
            .filter_by(
                id=medicion_id,
                user_id=user_id
            )
            .first()
        )


    def ultima_medicion(
        self,
        planta_id
    ):

        return (
            MedicionPlanta.query
            .filter_by(planta_id=planta_id)
            .order_by(MedicionPlanta.fecha_registro.desc())
            .first()
        )


    def guardar(
        self,
        medicion
    ):

        db.session.add(
            medicion
        )

        db.session.commit()

        return medicion


    def actualizar(
        self,
        medicion
    ):

        db.session.commit()

        return medicion


    def eliminar(
        self,
        medicion
    ):

        db.session.delete(
            medicion
        )

        db.session.commit()