from app import db

class Planta(db.Model):

    __tablename__ = "plantas"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.String(255), nullable=False)

    tag = db.Column(
        db.String(50),
        nullable=False,
        unique=True
    )

    common_name = db.Column(
        db.String(100),
        nullable=False
    )

    variety = db.Column(
        db.String(100)
    )

    status = db.Column(
        db.String(50),
        default="Crecimiento"
    )

    location_id = db.Column(
        db.Integer,
        db.ForeignKey("locations.id")
    )
    
    photo_url = db.Column(
        db.Text,
        nullable=True
    )
    
    especie_id = db.Column(
        db.Integer,
        db.ForeignKey("especies.id"),
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
        "MedicionPlanta",
        back_populates="planta",
        cascade="all, delete-orphan"
    )