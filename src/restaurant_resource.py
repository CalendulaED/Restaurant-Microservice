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
    def get_all_restaurant():
        # get all restaurants result
        sql = "SELECT * FROM restaurant_databases.Restaurant";
        conn = RestaurantResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql)
        result = cur.fetchall()

        return result

    @staticmethod
    def get_all_dish():
        # get all dish result
        sql = "SELECT * FROM restaurant_databases.Dish";
        conn = RestaurantResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql)
        result = cur.fetchall()

        return result



    @staticmethod
    def insert_restaurant(rest_id, rest_name, rest_location, rest_size):
        sql = "INSERT INTO restaurant_databases.Restaurant VALUES (%s, %s, %s, %s)";
        conn = RestaurantResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=(rest_id, rest_name, rest_location, rest_size))
        result = cur.fetchall()

        return result