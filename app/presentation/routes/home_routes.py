from flask import Blueprint
from flask import render_template

from app.infrastructure.auth.auth_guard import login_required
from app.infrastructure.auth.supabase_client import supabase
from app.application.services.home_service import HomeService


home_bp = Blueprint(
    "home",
    __name__
)

service_home = HomeService()

@home_bp.route("/")
@login_required
def home():
    
    user = supabase.auth.get_user()
    
    dashboard = service_home.obtener_dashboard(
        user.user.id,
    )
    

    return render_template(
        "home/index.html",
        title="Métricas Verdes",
        dashboard=dashboard
    )