from datetime import datetime

from app import db


class Medicion(db.Model):

    __tablename__ = "mediciones"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    planta_id = db.Column(
        db.Integer,
        db.ForeignKey("plantas.id"),
        nullable=False
    )

    temperatura = db.Column(
        db.Float,
        nullable=False
    )

    humedad = db.Column(
        db.Float,
        nullable=False
    )

    desarrollo = db.Column(
        db.Float,
        nullable=False
    )

    observaciones = db.Column(
        db.Text
    )

    fecha_registro = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False
    )