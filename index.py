from flask import Blueprint, jsonify
from model import Instrumento, Accesorio

index_blueprint = Blueprint('index', __name__)

@index_blueprint.route('/instrumentos_ajax', methods=['GET'])
def instrumentos_ajax():
    # Obtener solo 3 instrumentos
    instrumentos = Instrumento.query.limit(3).all()

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

    return jsonify(instrumentos_list)

@index_blueprint.route('/accesorios_ajax', methods=['GET'])
def accesorios_ajax():
    # Obtener solo 3 accesorios
    accesorios = Accesorio.query.limit(3).all()

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

    return jsonify(accesorios_list)
