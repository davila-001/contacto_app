from flask import Flask
from . import routes

def create_app():
    app = Flask(__name__)
    
    # Configuración opcional
    app.config["SECRET_KEY"] = "clave-secreta"
    
    # Registrar rutas
    app.register_blueprint(routes.bp)
    
    return app