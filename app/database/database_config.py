from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


class DatabaseHandler:
    """Database handler class"""

    # Singleton class to solve the problem of passing the database and marshmallow instances to all the classes
    # which need them, unfortunately this is order specific and therefore not optimal.
    __database: SQLAlchemy = None
    __marshmallow: Marshmallow = None

    @classmethod
    def create_or_get_db(cls, app: Flask = None):

        if not cls.__database:
            cls.__database: SQLAlchemy = SQLAlchemy(app)
            cls.__marshmallow: Marshmallow = Marshmallow(app)
        return cls.__database, cls.__marshmallow
