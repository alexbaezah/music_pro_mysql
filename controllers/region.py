from flask import Blueprint, jsonify
from model import Region 


regiones_blueprint = Blueprint('regiones', __name__)

@regiones_blueprint.route('/regiones', methods=['GET'])
def obtener_regiones():
    regiones = Region.query.all()
    datos_regiones = [{'ID_REGION': region.ID_REGION, 'NOMBRE_REG': region.NOMBRE_REG} for region in regiones]
    return jsonify(datos_regiones)