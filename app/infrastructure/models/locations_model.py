from app import db


class Location(db.Model):

    __tablename__ = "locations"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.String(255),
        nullable=False
    )

    name = db.Column(
        db.String(100),
        nullable=False
    )

    description = db.Column(
        db.String(255)
    )

    ideal_temperature_min = db.Column(
        db.Float,
        nullable=True
    )

    ideal_temperature_max = db.Column(
        db.Float,
        nullable=True
    )

    ideal_humidity_min = db.Column(
        db.Float,
        nullable=True
    )

    ideal_humidity_max = db.Column(
        db.Float,
        nullable=True
    )

    plants_count = db.Column(
        db.Integer,
        default=0
    )

    species_count = db.Column(
        db.Integer,
        default=0
    )

    health_status = db.Column(
        db.String(20),
        nullable=True
    )

    profile_updated_at = db.Column(
        db.DateTime,
        nullable=True
    )

    plantas = db.relationship(
        "Planta",
        backref="location",
        lazy=True
    )