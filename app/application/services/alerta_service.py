from app.infrastructure.repositories.alerta_repository import AlertaRepository

class AlertaService:
    def __init__(self):
        self.repository = AlertaRepository()
    
    