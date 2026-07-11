from datetime import datetime

from app import db


class MedicionPlanta(db.Model):

    __tablename__ = "mediciones_planta"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.String(255),
        nullable=False
    )

    planta_id = db.Column(
        db.Integer,
        db.ForeignKey("plantas.id"),
        nullable=False
    )

    altura = db.Column(
        db.Float
    )

    diametro_tallo = db.Column(
        db.Float
    )

    numero_hojas = db.Column(
        db.Integer
    )

    numero_flores = db.Column(
        db.Integer
    )

    numero_frutos = db.Column(
        db.Integer
    )


    desarrollo = db.Column(
        db.Float
    ) 

    humedad_sustrato = db.Column(
        db.Float
    ) 

    salud = db.Column(
        db.String(20),
        default="Óptima"
    )

    color_hojas = db.Column(
        db.String(30)
    )

    plagas = db.Column(
        db.Boolean,
        default=False
    )

    enfermedad = db.Column(
        db.Boolean,
        default=False
    )

    observaciones = db.Column(
        db.Text
    )

    foto_url = db.Column(
        db.String(255)
    )

    fecha_registro = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    planta = db.relationship(
        "Planta",
        back_populates="mediciones"
    )