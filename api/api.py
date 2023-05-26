import random
from flask import jsonify, request, Blueprint
from transbank.webpay.webpay_plus.transaction import Transaction
from model import Pago, db, Carrito


webpay_blueprint = Blueprint('webpay_plus', __name__)

@webpay_blueprint.route("/create/<int:id_pago>", methods=["GET"])
def webpay_plus_create(id_pago):
    print("Webpay Plus Transaction.create")
    pago = Pago.query.get(id_pago)
    buy_order = str(pago.ID_PAGO)
    session_id = str(random.randrange(1000000, 99999999))
    amount = str(pago.MONTO_TOTAL_PAGO)
    return_url = request.url_root + 'webpay-plus/commit'

    create_request = {
        "buy_order": buy_order,
        "session_id": session_id,
        "amount": amount,
        "return_url": return_url
    }

    response = Transaction().create(buy_order, session_id, amount, return_url)

    print(response)

    return jsonify({
        "request": create_request,
        "response": response
    })




@webpay_blueprint.route("commit", methods=["GET"])
def webpay_plus_commit():
    token = request.args.get("token_ws")
    print("commit for token_ws: {}".format(token))

    response = (Transaction()).commit(token=token)
    print("response: {}".format(response))

    # Construye la respuesta en formato JSON
    response_json = {
        "token": token,
        "response": response
    }

    # Retorna la respuesta en formato JSON
    return jsonify(response_json)