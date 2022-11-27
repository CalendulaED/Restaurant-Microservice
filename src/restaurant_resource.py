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
    def get_all_dish():
        sql = "SELECT * FROM restaurant_databases.Dish";
        conn = RestaurantResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql)
        result = cur.fetchall()

        return result

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
    def insert_restaurant(rest_id, rest_name, rest_location, rest_size):
        sql = "INSERT IGNORE INTO restaurant_databases.Restaurant VALUES (%s, %s, %s, %s)";
        conn = RestaurantResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=(rest_id, rest_name, rest_location, rest_size))
        # result = cur.fetchone()

        return res

    @staticmethod
    def insert_dish(dish_id, dish_name, flavor, dish_description, serve_size):
        sql = "INSERT IGNORE INTO restaurant_databases.Dish VALUES (%s, %s, %s, %s, %s)";
        conn = RestaurantResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=(dish_id, dish_name, flavor, dish_description, serve_size))
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
    def update_dish(dish_name, flavor, dish_description, serve_size, key):
        sql = "UPDATE restaurant_databases.Dish SET dish_name = %s, flavor = %s, dish_description = %s, serve_size = %s WHERE dish_id = %s"
        conn = RestaurantResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=(dish_name, flavor, dish_description, serve_size, key))

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
