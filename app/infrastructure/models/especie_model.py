from app import db

class Especie(db.Model):

    __tablename__ = "especies"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.String(255),
        nullable=True
    )

    name = db.Column(
        db.String(100),
        nullable=False,
        unique=True
    )

    scientific_name = db.Column(
        db.String(150)
    )

    description = db.Column(
        db.Text
    )

    photo_url = db.Column(
        db.Text,
        nullable=True
    )

    ideal_humidity_min = db.Column(
        db.Float
    )

    ideal_humidity_max = db.Column(
        db.Float
    )

    ideal_temperature_min = db.Column(
        db.Float
    )

    ideal_temperature_max = db.Column(
        db.Float
    )

    expected_growth_rate = db.Column(
        db.String(50)
    )

    average_germination_days = db.Column(
        db.Integer
    )

    average_transplant_days = db.Column(
        db.Integer
    )

    sunlight_requirement = db.Column(
        db.String(50)
    )

    watering_frequency_days = db.Column(
        db.Integer
    )

    difficulty_level = db.Column(
        db.String(50)
    )

    plantas = db.relationship(
        "Planta",
        backref="especie",
        lazy=True
    )