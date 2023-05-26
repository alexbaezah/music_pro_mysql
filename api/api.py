import random
from flask import jsonify, request, Blueprint
from transbank.webpay.webpay_plus.transaction import Transaction


webpay_blueprint = Blueprint('webpay_plus', __name__)

@webpay_blueprint.route("/create", methods=["GET"])
def webpay_plus_create():
    print("Webpay Plus Transaction.create")
    buy_order = str(random.randrange(1000000, 99999999))
    session_id = str(random.randrange(1000000, 99999999))
    amount = random.randrange(10000, 1000000)
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