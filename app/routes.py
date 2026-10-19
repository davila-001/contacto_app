from flask import Blueprint, render_template, request

bp = Blueprint("routes", __name__)

# Página de inicio
@bp.route("/")
def index():
    return render_template("index.html")

# Página de contacto
@bp.route("/contacto", methods=["GET", "POST"])
def contacto():
    if request.method == "POST":
        nombre = request.form.get("nombre")
        correo = request.form.get("correo")
        mensaje = request.form.get("mensaje")
        return render_template("gracias.html", 
                               nombre=nombre,
                               correo=correo,
                               mensaje=mensaje)
    return render_template("contacto.html")