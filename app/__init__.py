from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from app.infrastructure.database.connection import db
from app.infrastructure.database.connection import migrate
from app.infrastructure.models.planta_model import Planta
from app.infrastructure.models.medicion_model import Medicion

from app.presentation.routes.planta_routes import planta_bp
from app.presentation.routes.medicion_routes import medicion_bp

def create_app():

    app = Flask(
        __name__,
        template_folder="presentation/templates",
        static_folder="presentation/static"
    )

    app.config.from_object("config.Config")

    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():

        try:

            with db.engine.connect() as connection:

                connection.execute(text("SELECT 1"))

                print("✓ Database connection successfully")

        except Exception as error:

            print(f"✗ Database connection error: {error}")

    from app.presentation.routes.home_routes import home_bp

    app.register_blueprint(home_bp)
    app.register_blueprint(planta_bp)
    app.register_blueprint(medicion_bp)

    return app