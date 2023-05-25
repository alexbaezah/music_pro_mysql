from flask import Blueprint, jsonify, render_template
from model import Pago

pagos_blueprint = Blueprint('pagos', __name__)

@pagos_blueprint.route('/pagos', methods=['GET'])
def get_pagos():
    pagos = Pago.query.all()

    pagos_list = []
    for pago in pagos:
        pagos_dict = {
            'id_pago': pago.ID_PAGO,
            'id_carrito': pago.ID_CARRITO,
            'monto_total': pago.MONTO_TOTAL_PAGO,
            'fecha_pago': pago.FECHA_PAGO,
            'id_estado' : pago.ID_ESTADO_PAGO
        }
        pagos_list.append(pagos_dict)
    return jsonify(pagos_list), 200, {'Content-Type': 'application/json; charset=utf-8'}