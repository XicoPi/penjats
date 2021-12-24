from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, jsonify
)
from flask import current_app as app

#from . import db

main_bp = Blueprint("main_bp", __name__,
                    static_folder="templates")


@main_bp.route("/")
def index():
    """
    Ruta de la pagina principal.
    """
    return render_template("sites/index.html")

@main_bp.route("/profile")
def profile():
    return render_template("sites/profile.html")

@main_bp.route("/history")
def history():
    return render_template("sites/history.html")
