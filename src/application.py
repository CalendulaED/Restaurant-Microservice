from flask import Flask, Response, request, render_template
from datetime import datetime
import json
from restaurant_resource import RestaurantResource
from flask_cors import CORS


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

@app.route("/dishes/<dishID>", methods=["GET"])
def get_dish_by_id(dishID):

    result = RestaurantResource.get_by_key_dish(dishID)

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
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

@app.route("/restaurants", methods=["GET"])
def get_restaurant():

    result = RestaurantResource.get_all_restaurant()

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

    result = RestaurantResource.insert_restaurant(rest_id, rest_name, rest_location, rest_size)
    result_dic = {'rest_id': rest_id, 'rest_name': rest_name, 'rest_location': rest_location, 'rest_size': rest_size}

    if result:
        rsp = Response(json.dumps(result_dic), status=200, content_type="application.json")
    else:
        rsp = Response("Insert Failed! (Duplicate data)", status=404, content_type="text/plain")

    return rsp


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5011)