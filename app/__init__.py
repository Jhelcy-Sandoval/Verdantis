from flask import Flask
from sqlalchemy import text

from app.infrastructure.database.connection import db
from app.infrastructure.database.connection import migrate

# Modelos
from app.infrastructure.models.planta_model import Planta
from app.infrastructure.models.medicion_model import Medicion

# Blueprints
from app.presentation.routes.home_routes import home_bp
from app.presentation.routes.planta_routes import planta_bp
from app.presentation.routes.medicion_routes import medicion_bp
from app.presentation.routes.especie_routes import especie_bp
from app.presentation.routes.location_routes import locations_bp
from app.presentation.routes.auth_routes import auth_bp
from app.presentation.routes.error_routes import error_bp


def create_app():

    app = Flask(
        __name__,
        template_folder="presentation/templates",
        static_folder="presentation/static"
    )

    # Configuración
    app.config.from_object("config.Config")

    # Base de datos
    db.init_app(app)
    migrate.init_app(app, db)

    # Verificar conexión
    with app.app_context():

        try:

            with db.engine.connect() as connection:

                connection.execute(text("SELECT 1"))

                print("✓ Database connection successfully")

        except Exception as error:

            print(
                f"✗ Database connection error: {error}"
            )

    # Registro de blueprints
    app.register_blueprint(home_bp)

    app.register_blueprint(
        planta_bp,
        url_prefix="/plantas"
    )

    app.register_blueprint(
        medicion_bp,
        url_prefix="/mediciones"
    )
    
    
    app.register_blueprint(
        especie_bp,
        url_prefix="/especie"
    )
    
    app.register_blueprint(
        locations_bp,
        url_prefix="/locations"
    )

    app.register_blueprint(
        auth_bp,
        url_prefix="/auth"
    )
    
    app.register_blueprint(
        error_bp,
        url_prefix="/error"
    )

    return app