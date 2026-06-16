from app.infrastructure.models.planta_model import Planta
from app import db

class AlertaRepository:
    def listar_por_usuario(
        self,
        user_id
    ):

        return Planta.query.filter_by(
            user_id=user_id
        ).all()