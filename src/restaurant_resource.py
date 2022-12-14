import pymysql

import os


class RestaurantResource:

    def __init__(self):
        pass

    @staticmethod
    def _get_connection():
        usr = os.environ.get("DBUSER")
        pw = os.environ.get("DBPW")
        h = os.environ.get("DBHOST")

        conn = pymysql.connect(

            user=usr,
            password=pw,
            host=h,
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )
        return conn

    @staticmethod
    def get_by_key(key):
        sql = "SELECT * FROM restaurant_databases.Restaurant where rest_id=%s";
        conn = RestaurantResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=key)
        result = cur.fetchone()

        return result

    @staticmethod
    def get_by_key_dish(key):
        sql = "SELECT * FROM restaurant_databases.Dish where dish_id=%s";
        conn = RestaurantResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=key)
        result = cur.fetchone()

        return result

    @staticmethod
    def get_by_key_serve(rest_id, dish_id):
        sql = "SELECT * FROM restaurant_databases.Serve WHERE rest_id=%s AND dish_id=%s";
        conn = RestaurantResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=(rest_id, dish_id))
        result = cur.fetchone()

        return result

    @staticmethod
    def get_all_dish():
        sql = "SELECT * FROM restaurant_databases.Dish";
        conn = RestaurantResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql)
        result = cur.fetchall()

        return result

    @staticmethod
    def get_all_serve():
        sql = "SELECT * FROM restaurant_databases.Serve";
        conn = RestaurantResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql)
        result = cur.fetchall()

        return str(result)

    @staticmethod
    def get_all_restaurant(args):
        sql = "SELECT * FROM restaurant_databases.Restaurant";
        rest_name = args.get("rest_name")
        if rest_name == "":
            rest_name = None
        rest_location = args.get("rest_location")
        if rest_location == "":
            rest_location = None

        if rest_name is not None or rest_location is not None:
            sql += " WHERE "
        if rest_name is not None:
            sql += "rest_name = \"" + rest_name + "\""
        if None not in (rest_name, rest_location):
            sql += " AND "
        if rest_location is not None:
            sql += "rest_location = \"" + rest_location + "\""

        conn = RestaurantResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql)
        result = cur.fetchall()

        return result

    @staticmethod
    def get_all_dishes_by_rest(restID):
        sql = "SELECT * FROM restaurant_databases.Dish WHERE rest_id=%s";
        conn = RestaurantResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=(restID))
        result = cur.fetchall()

        return str(result)

    @staticmethod
    def insert_restaurant(rest_id, rest_name, rest_location, rest_size):
        sql = "INSERT IGNORE INTO restaurant_databases.Restaurant VALUES (%s, %s, %s, %s)";
        conn = RestaurantResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=(rest_id, rest_name, rest_location, rest_size))
        # result = cur.fetchone()

        return res

    @staticmethod
    def insert_serve(rest_id, dish_id, serve_time, price):
        sql = "INSERT IGNORE INTO restaurant_databases.Serve VALUES (%s, %s, %s, %s)";
        conn = RestaurantResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=(rest_id, dish_id, serve_time, price))
        # result = cur.fetchone()
        return res

    @staticmethod
    def insert_dish(dish_id, dish_name, flavor, dish_description, serve_size, rest_id):
        sql = "INSERT IGNORE INTO restaurant_databases.Dish VALUES (%s, %s, %s, %s, %s, %s)";
        conn = RestaurantResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=(dish_id, dish_name, flavor, dish_description, serve_size, rest_id))
        # result = cur.fetchone()

        return res

    @staticmethod
    def update_restaurant(rest_name, rest_location, rest_size, key):
        sql = "UPDATE restaurant_databases.Restaurant SET rest_name = %s, rest_location = %s, rest_size = %s WHERE rest_id = %s"
        conn = RestaurantResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=(rest_name, rest_location, rest_size, key))

        return res

    @staticmethod
    def update_dish(dish_name, flavor, dish_description, serve_size, rest_id, key):
        sql = "UPDATE restaurant_databases.Dish SET dish_name = %s, flavor = %s, dish_description = %s, serve_size = %s, rest_id = %s WHERE dish_id = %s"
        conn = RestaurantResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=(dish_name, flavor, dish_description, serve_size, rest_id, key))

        return res

    @staticmethod
    def update_serve(serve_time, price, dish_id, rest_id):
        sql = "UPDATE restaurant_databases.Serve SET serve_time = %s, price = %s WHERE dish_id = %s AND rest_id = %s"
        conn = RestaurantResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=(serve_time, price, dish_id, rest_id))

        return res

    @staticmethod
    def delete_restaurant(key):
        sql1 = "DELETE FROM restaurant_databases.Serve where rest_id = %s";
        sql2 = "DELETE FROM restaurant_databases.Restaurant where rest_id = %s";
        conn = RestaurantResource._get_connection()
        cur = conn.cursor()
        cur.execute(sql1, args=key)
        res = cur.execute(sql2, args=key)

        return res

    @staticmethod
    def delete_dish(key):
        sql1 = "DELETE FROM restaurant_databases.Serve where dish_id = %s";
        sql2 = "DELETE FROM restaurant_databases.Dish where dish_id = %s";
        conn = RestaurantResource._get_connection()
        cur = conn.cursor()
        cur.execute(sql1, args=key)
        res = cur.execute(sql2, args=key)

        return res

    @staticmethod
    def delete_serve(rest_id, dish_id):
        sql1 = "DELETE FROM restaurant_databases.Serve where rest_id = %s AND dish_id = %s";
        conn = RestaurantResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql1, args=(rest_id, dish_id))

        return res



