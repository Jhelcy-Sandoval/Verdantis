from datetime import datetime

from app import db


class Medicion(db.Model):

    __tablename__ = "mediciones"

    id = db.Column(
        db.Integer,
        primary_key=True
    )
    
    user_id = db.Column(
        db.String(255),
        nullable=True
    )

    location_id = db.Column(
        db.Integer,
        db.ForeignKey("locations.id"),
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
    
    estado = db.Column(
        db.String(20),
        nullable=False,
        default="Óptimo"
    )

    observaciones = db.Column(
        db.Text
    )

    fecha_registro = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False
    )
    
    locations = db.relationship(
        "Location",
        backref="mediciones",
        lazy=True
    )