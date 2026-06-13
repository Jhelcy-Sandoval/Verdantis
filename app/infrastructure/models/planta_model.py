from app import db


class Planta(db.Model):

    __tablename__ = "plantas"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    tag = db.Column(
        db.String(50),
        nullable=False
    )

    species = db.Column(
        db.String(100),
        nullable=False
    )

    germination_date = db.Column(
        db.Date,
        nullable=False
    )

    initial_conditions = db.Column(
        db.Text
    )

    mediciones = db.relationship(
        "Medicion",
        backref="planta",
        lazy=True,
        cascade="all, delete-orphan"
    )