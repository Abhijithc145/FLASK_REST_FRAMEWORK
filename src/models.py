import os
import psycopg2


psql = psycopg2.connect(
        host="localhost",
        database="newflask",
        user="postgres",
        password="postgres")


cur = psql.cursor(dictionary=True)
