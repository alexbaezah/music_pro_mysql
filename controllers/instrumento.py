from flask import Blueprint, jsonify, render_template
from model import Instrumento


instrumentos_blueprint = Blueprint('instrumentos', __name__)

@instrumentos_blueprint.route('/instrumentos', methods=['GET'])
def get_instrumentos():
    instrumentos = Instrumento.query.all()

    instrumentos_list = []
    for instrumento in instrumentos:
        instrumento_dict = {
            'id': instrumento.ID_INSTR,
            'nombre': instrumento.NOMBRE_INSTR,
            'descripcion': instrumento.DESCRIPCION_INSTR,
            'precio': instrumento.PRECIO_INSTR,
            'stock': instrumento.STOCK_INSTR,
            'id_subtipo': instrumento.ID_SUBTIPO,
            'foto': instrumento.FOTO
        }
        instrumentos_list.append(instrumento_dict)

    return jsonify(instrumentos_list), 200, {'Content-Type': 'application/json; charset=utf-8'}
    

@instrumentos_blueprint.route('/instrumentos/<int:instrumento_id>', methods=['GET'])
def get_instrumento(instrumento_id):
    instrumento = Instrumento.query.get(instrumento_id)

    if not instrumento:
        return jsonify({'error': 'Instrumento no encontrado'}), 404

    instrumento_dict = {
        'id': instrumento.ID_INSTR,
        'nombre': instrumento.NOMBRE_INSTR,
        'descripcion': instrumento.DESCRIPCION_INSTR,
        'precio': instrumento.PRECIO_INSTR,
        'stock': instrumento.STOCK_INSTR,
        'id_subtipo': instrumento.ID_SUBTIPO,
        'foto': instrumento.FOTO
    }

    return jsonify(instrumento_dict), 200, {'Content-Type': 'application/json; charset=utf-8'}
