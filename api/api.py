import random
from flask import render_template, request, Blueprint, jsonify
from transbank.webpay.webpay_plus.transaction import Transaction

from app import db
from model import Carrito, Pago

webpay_blueprint = Blueprint('webpay', __name__)

@webpay_blueprint.route('/webpay/pagar', methods=['GET'])
def webpay_pagar():
    # Generar datos de prueba para la transacción
    buy_order = 'carrito-test-' + str(random.randrange(1000000, 99999999))
    session_id = 'session-test-' + str(random.randrange(1000000, 99999999))
    amount = random.randrange(10000, 1000000)
    return_url = request.url_root + 'webpay/confirmar'

    # Crear la transacción en Webpay Plus
    transaction = Transaction()
    response = transaction.create(buy_order, session_id, amount, return_url)
    token = response.token
    url = response.url

    # Guardar los datos de la transacción en la base de datos
    carrito = Carrito(buy_order=buy_order, session_id=session_id, amount=amount, token=token)
    db.session.add(carrito)
    db.session.commit()

    # Preparar la respuesta en formato JSON
    response_data = {
        'token': token,
        'url': url,
        'buy_order': buy_order,
        'amount': amount
    }

    # Retornar la respuesta en formato JSON
    return jsonify(response_data)


@webpay_blueprint.route('/webpay/confirmar', methods=['GET'])
def webpay_confirmar():
    token = request.args.get('token_ws')

    # Obtener la información del carrito asociado al token
    carrito = Carrito.query.filter_by(token=token).first()

    if carrito:
        # Crear el registro de pago en la base de datos
        pago = Pago(carrito_id=carrito.id, amount=carrito.amount)
        db.session.add(pago)
        db.session.commit()

        # Preparar la respuesta en formato JSON
        response_data = {
            'token': token,
            'carrito_id': carrito.id,
            'amount': carrito.amount
        }

        # Retornar la respuesta en formato JSON
        return jsonify(response_data)
    else:
        return "Carrito no encontrado"


@webpay_blueprint.route('/webpay/reembolso', methods=['POST'])
def webpay_reembolso():
    carrito_id = request.form.get('carrito_id')
    amount = request.form.get('amount')

    # Obtener el carrito y el pago asociados al ID del carrito
    carrito = Carrito.query.get(carrito_id)
    pago = Pago.query.filter_by(carrito_id=carrito_id).first()

    if carrito and pago:
        # Realizar el reembolso a través de Webpay Plus
        transaction = Transaction()
        response = transaction.refund(token=carrito.token, amount=amount)

        # Actualizar el estado del pago y guardar los datos del reembolso en la base de datos
        pago.reembolso_realizado = True
        pago.monto_reembolso = amount
        db.session.commit()

        # Preparar la respuesta en formato JSON
        response_data = {
            'carrito_id': carrito.id,
            'amount': amount,
            'response': response
        }

        # Retornar la respuesta en formato JSON
        return jsonify(response_data)
    else:
        return "Carrito o pago no encontrado"