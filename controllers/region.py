from flask import Blueprint, jsonify, request
from model import Region 
from app import db


regiones_blueprint = Blueprint('regiones', __name__)


@regiones_blueprint.route('/regiones', methods=['GET'])
def obtener_regiones():
    regiones = Region.query.all()
    datos_regiones = [{'ID_REGION': region.ID_REGION, 'NOMBRE_REG': region.NOMBRE_REG} for region in regiones]
    return jsonify(datos_regiones)


""" 
@regiones_blueprint.route('/crear', methods=['POST'])
def create_region():
    data = request.get_json()

    id_region = data.get('ID_REGION')
    nombre_reg = data.get('NOMBRE_REG')

    region = Region(ID_REGION=id_region, NOMBRE_REG=nombre_reg)

    db.session.add(region)
    db.session.commit()

    return jsonify({'message': 'Región creada exitosamente'}), 201
"""