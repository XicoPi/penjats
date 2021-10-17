from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, jsonify
)
from flask import current_app as app

from . import db

bp = Blueprint('routes', __name__,
               static_folder='templates')


@bp.route('/')
def index():
    """                                                                                                    Ruta de la pagina principal.                                                                           """
    return render_template('sites/index.html')

@bp.route('/friends')
def friends():
    """
    Ruta a la pàgina d'amics
    """
    return render_template('sites/friends.html')
