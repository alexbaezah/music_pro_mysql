from flask import Blueprint, jsonify, render_template
from model import Accesorio

accesorios_blueprint = Blueprint('accesorios', __name__)

@accesorios_blueprint.route('/accesorios', methods=['GET'])
def get_accesorios():
    accesorios = Accesorio.query.all()

    accesorios_list = []
    for accesorio in accesorios:
        accesorio_dict = {
            'id': accesorio.ID_ACCESORIO,
            'nombre': accesorio.NOMBRE,
            'descripcion': accesorio.DESCRIPCION,
            'precio': accesorio.PRECIO_ACCE,
            'stock': accesorio.STOCK_ACCE,
            'id_marca': accesorio.ID_MARCA,
            'foto': accesorio.FOTO
        }
        accesorios_list.append(accesorio_dict)

    return jsonify(accesorios_list), 200, {'Content-Type': 'application/json; charset=utf-8'}
    
@accesorios_blueprint.route('/accesorios/<int:accesorio_id>', methods=['GET'])
def get_accesorio(accesorio_id):
    accesorio = Accesorio.query.get(accesorio_id)

    if not accesorio:
        return jsonify({'error': 'accesorio no encontrado'}), 404

    accesorio_dict = {
        'id': accesorio.ID_ACCESORIO,
        'nombre': accesorio.NOMBRE,
        'descripcion': accesorio.DESCRIPCION,
        'precio': accesorio.PRECIO_ACCE,
        'stock': accesorio.STOCK_ACCE,
        'id_marca': accesorio.ID_MARCA,
        'foto': accesorio.FOTO
    }

    return jsonify(accesorio_dict), 200, {'Content-Type': 'application/json; charset=utf-8'}
