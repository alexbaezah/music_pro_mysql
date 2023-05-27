from flask import Blueprint, jsonify
from model import Ciudad


ciudades_blueprint = Blueprint('ciudades', __name__)



@ciudades_blueprint.route('/ciudades', methods=['GET'])
def obtener_ciudades():
    ciudades = Ciudad.query.all()
    datos_ciudades = [{'ID_CIUDAD': ciudad.ID_CIUDAD, 'NOM_CIUD': ciudad.NOM_CIUD} for ciudad in ciudades ]
    return jsonify(datos_ciudades)


