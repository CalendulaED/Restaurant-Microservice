from flask import Flask, Response, request, render_template
from datetime import datetime
import json
from restaurant_resource import RestaurantResource
from flask_cors import CORS

from smarty import check_address
import datetime

# Create the Flask application object.
app = Flask(__name__,
            static_url_path='/',
            static_folder='static/class-ui/',
            template_folder='web/templates')

CORS(app)


# @app.get("/api/health")
# def get_health():
#     t = str(datetime.now())
#     msg = {
#         "name": "F22-Starter-Microservice",
#         "health": "Good",
#         "at time": t
#     }

#     # DFF TODO Explain status codes, content type, ... ...
#     result = Response(json.dumps(msg), status=200, content_type="application/json")

#     return result


@app.route("/restaurants/<restaurantID>", methods=["GET"])
def get_restaurant_by_id(restaurantID):

    result = RestaurantResource.get_by_key(restaurantID)

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp

@app.route("/restaurants/<restaurantID>", methods=["PUT"])
def update_restaurant(restaurantID):
    update_data = request.get_json()
    print('The origin parameter is: ', update_data)
    rest_name = str(update_data.get('rest_name')).strip(),
    rest_location = str(update_data.get('rest_location')).strip(),
    rest_size = str(update_data.get('rest_size')).strip()

    rest_location = check_address(rest_location)
    if rest_location is None:
        rsp = Response("Update Failed! (Bad address)", status=404, content_type="text/plain")
        return rsp

    result = RestaurantResource.update_restaurant(rest_name, rest_location, rest_size, restaurantID)
    result_dic = {'rest_id': restaurantID, 'rest_name': rest_name, 'rest_location': rest_location, 'rest_size': rest_size}

    if result:
        rsp = Response(json.dumps(result_dic), status=200, content_type="application.json")
    else:
        rsp = Response("Update Failed! (Duplicate data or bad input parameter)", status=404, content_type="text/plain")

    return rsp

@app.route("/restaurants/<restaurantID>", methods=["DELETE"])
def delete_restaurant(restaurantID):

    result = RestaurantResource.delete_restaurant(restaurantID)

    if result:
        rsp = Response("Deleted", status=200, content_type="text/plain")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp

@app.route("/dishes/<dishID>", methods=["GET"])
def get_dish_by_id(dishID):

    result = RestaurantResource.get_by_key_dish(dishID)

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp

@app.route("/dishes/<dishID>", methods=["PUT"])
def update_dish(dishID):
    update_data = request.get_json()
    print('The origin parameter is: ', update_data)
    dish_name = str(update_data.get('dish_name')).strip(),
    flavor = str(update_data.get('flavor')).strip(),
    dish_description = str(update_data.get('dish_description')).strip(),
    serve_size = str(update_data.get('serve_size')).strip(),
    rest_id = str(update_data.get('rest_id')).strip()

    result = RestaurantResource.update_dish(dish_name, flavor, dish_description, serve_size, rest_id, dishID)
    result_dic = {'dish_id': dishID, 'dish_name': dish_name, 'flavor': flavor, 'dish_description': dish_description, 'serve_size': serve_size, 'rest_id': rest_id}

    if result:
        rsp = Response(json.dumps(result_dic), status=200, content_type="application.json")
    else:
        rsp = Response("Update Failed! (Duplicate data or bad input parameter)", status=404, content_type="text/plain")

    return rsp


@app.route("/dishes/<dishID>", methods=["DELETE"])
def delete_dish(dishID):

    result = RestaurantResource.delete_dish(dishID)

    if result:
        rsp = Response("Deleted", status=200, content_type="text/plain")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp

@app.route("/dishes", methods=["GET"])
def get_dish():

    result = RestaurantResource.get_all_dish()

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp


@app.route("/dishes", methods=["POST"])
def add_dish():
    post_data = request.get_json()
    print('The origin parameter is: ', post_data)
    dish_id = str(post_data.get('dish_id')).strip(),
    dish_name = str(post_data.get('dish_name')).strip(),
    flavor = str(post_data.get('flavor')).strip(),
    dish_description = str(post_data.get('dish_description')).strip(),
    serve_size = str(post_data.get('serve_size')).strip(),
    rest_id = str(post_data.get('rest_id')).strip()

    result = RestaurantResource.insert_dish(dish_id, dish_name, flavor, dish_description, serve_size, rest_id)
    result_dic = {'dish_id': dish_id, 'dish_name': dish_name, 'flavor': flavor, 'dish_description': dish_description, 'serve_size': serve_size, 'rest_id': rest_id}

    if result:
        rsp = Response(json.dumps(result_dic), status=200, content_type="application.json")
    else:
        rsp = Response("Insert Failed! (Duplicate data)", status=404, content_type="text/plain")

    return rsp

@app.route("/restaurants", methods=["GET"])
def get_restaurant():
    args = request.args
    result = RestaurantResource.get_all_restaurant(args)

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp


@app.route("/restaurants", methods=["POST"])
def add_restaurant():
    post_data = request.get_json()
    print('The origin parameter is: ', post_data)
    rest_id = str(post_data.get('rest_id')).strip(),
    rest_name = str(post_data.get('rest_name')).strip(),
    rest_location = str(post_data.get('rest_location')).strip(),
    rest_size = str(post_data.get('rest_size')).strip()

    rest_location = check_address(rest_location)
    if rest_location is None:
        rsp = Response("Insert Failed! (Bad address)", status=404, content_type="text/plain")
        return rsp

    result = RestaurantResource.insert_restaurant(rest_id, rest_name, rest_location, rest_size)
    result_dic = {'rest_id': rest_id, 'rest_name': rest_name, 'rest_location': rest_location, 'rest_size': rest_size}

    if result:
        rsp = Response(json.dumps(result_dic), status=200, content_type="application.json")
    else:
        rsp = Response("Insert Failed! (Duplicate data)", status=404, content_type="text/plain")

    return rsp


@app.route("/serves", methods=["POST"])
def add_serve():
    post_data = request.get_json()
    print('The origin parameter is: ', post_data)
    rest_id = str(post_data.get('rest_id')).strip(),
    dish_id = str(post_data.get('dish_id')).strip(),
    # serve_time = str(post_data.get('serve_time')).strip(),
    price = str(post_data.get('price')).strip()
    serve_time = datetime.datetime.now()

    result = RestaurantResource.insert_serve(rest_id, dish_id, serve_time, price)
    result_dic = {'rest_id': rest_id, 'dish_id': dish_id, 'serve_time': str(serve_time), 'price': price}

    if result:
        rsp = Response(json.dumps(result_dic), status=200, content_type="application.json")
    else:
        rsp = Response("Insert Failed! (Duplicate data)", status=404, content_type="text/plain")

    return rsp


@app.route("/serves", methods=["GET"])
def get_serve():
    result = RestaurantResource.get_all_serve()
    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp

@app.route("/serves/<restID>/<dishID>", methods=["GET"])
def get_serve_by_id(restID, dishID):

    result = RestaurantResource.get_by_key_serve(restID, dishID)

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp


@app.route("/serves/<restID>/<dishID>", methods=["PUT"])
def update_serve(serve_time, price, restID, dishID):
    update_data = request.get_json()
    print('The origin parameter is: ', update_data)
    serve_time = str(update_data.get('serve_time')).strip(),
    price = str(update_data.get('price')).strip()

    result = RestaurantResource.update_serve(serve_time, price, dishID, restID)
    result_dic = {'serve_time': serve_time, 'price': price, 'dish_id': dishID, 'rest_id': restID}

    if result:
        rsp = Response(json.dumps(result_dic), status=200, content_type="application.json")
    else:
        rsp = Response("Update Failed! (Duplicate data or bad input parameter)", status=404, content_type="text/plain")

    return rsp


@app.route("/serves/<restID>/<dishID>", methods=["DELETE"])
def delete_serve(restID, dishID):

    result = RestaurantResource.delete_serve(restID, dishID)

    if result:
        rsp = Response("Deleted", status=200, content_type="text/plain")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp


@app.route("/restaurants/dishes/<restID>", methods=["GET"])
def get_dishes_by_rest(restID):
    result = RestaurantResource.get_all_dishes_by_rest(restID)
    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5011)