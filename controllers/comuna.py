from flask import Blueprint, jsonify
from model import Comuna, Region


comunas_blueprint = Blueprint('comunas', __name__)



@comunas_blueprint.route('/comunas', methods=['GET'])
def obtener_comunas():
    comunas = Comuna.query.all()
    datos_comunas = [{'ID_COM': comuna.ID_COM, 'NOM_COM': comuna.NOM_COM} for comuna in comunas]
    return jsonify(datos_comunas)


