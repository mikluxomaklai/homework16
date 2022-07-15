import json
from flask import request
from config import app
from models import Order, User, Offer
from servise import init_db, get_all_by_id, get_all, insert_data_user, update_universal, insert_data_order, \
    insert_data_offer, delete_universal


@app.route("/users/", methods=['GET', 'POST'])
###загрузка пользователей###
def get_users():
    if request.method == 'GET':
        return app.response_class(
            response=json.dumps(get_all(User), indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'POST':
        if isinstance(request.json, list):
            insert_data_user(User, request.json)
        elif isinstance(request.json, dict):
            insert_data_user(User, [request.json])
        else:
            print("Неизвестный тип данных")

        return app.response_class(
            response=json.dumps(request.json, indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )


@app.route("/orders/", methods=['GET', 'POST'])
###загрузка заказов###
def get_orders():
    if request.method == 'GET':
        return app.response_class(
            response=json.dumps(get_all(Order), indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'POST':
        if isinstance(request.json, list):
            insert_data_order(Order, request.json)
        elif isinstance(request.json, dict):
            insert_data_order(Order, [request.json])
        else:
            print("Неизвестный тип данных")

        return app.response_class(
            response=json.dumps(request.json, indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )


@app.route("/offers/", methods=['GET', 'POST'])
###загрузка предложений###
def get_offers():
    if request.method == 'GET':
        return app.response_class(
            response=json.dumps(get_all(Offer), indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'POST':
        if isinstance(request.json, list):
            insert_data_offer(Offer, request.json)
        elif isinstance(request.json, dict):
            insert_data_offer(Offer, [request.json])
        else:
            print("Неизвестный тип данных")

        return app.response_class(
            response=json.dumps(request.json, indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )


@app.route("/users/<int:user_id>", methods=['GET', 'PUT', 'DELETE'])
###загрузка пользователей по id###
def get_user_by_id(user_id):
    if request.method == 'GET':
        data = get_all_by_id(User, user_id)

        return app.response_class(
            response=json.dumps(data, indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'PUT':
        update_universal(User, user_id, request.json)
        return app.response_class(
            response=json.dumps(["OK"], indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )

    elif request.method == 'DELETE':
        delete_universal(User, user_id)
        return app.response_class(
            response=json.dumps(["OK"], indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )


@app.route("/orders/<int:user_id>", methods=['GET', 'PUT', 'DELETE'])
###загрузка заказов по id###
def get_order_by_id(user_id):
    if request.method == 'GET':
        data = get_all_by_id(Order, user_id)

        return app.response_class(
            response=json.dumps(data, indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'PUT':
        update_universal(Order, user_id, request.json)
        return app.response_class(
            response=json.dumps(["OK"], indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )

    elif request.method == 'DELETE':
        delete_universal(Order, user_id)
        return app.response_class(
            response=json.dumps(["OK"], indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )


@app.route("/offers/<int:user_id>", methods=['GET', 'PUT', 'DELETE'])
###загрузка предложений по id###
def get_offer_by_id(user_id):
    if request.method == 'GET':
        data = get_all_by_id(Offer, user_id)

        return app.response_class(
            response=json.dumps(data, indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'PUT':

        update_universal(Offer, user_id, request.json)
        return app.response_class(
            response=json.dumps(["OK"], indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )

    elif request.method == 'DELETE':
        delete_universal(Offer, user_id)
        return app.response_class(
            response=json.dumps(["OK"], indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )


if __name__ == '__main__':
    init_db()
    app.run(host="0.0.0.0", port=8080, debug=True)
