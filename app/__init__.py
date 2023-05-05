"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chaa62jhp8u791gsdet0-a.oregon-postgres.render.com",
        database="todo_0k0o",
        user="todo_0k0o_user",
        password="PxDV5uMY2cgHFYEa9NF9jPOXFXxgz0n0")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
