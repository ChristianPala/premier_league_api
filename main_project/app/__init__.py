# Libraries:
from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint
from app.database import database_connection
from app.database.database_config import DatabaseHandler
from typing import Tuple


# initialize the flask web application.
def create_app(config: str = None) -> Flask:

    app = Flask(__name__)

    # string of the location of the config class and it's subclass, for instance "config.TestingConfig".
    app.config.from_object(config)

    # connect to the mysql database via sql alchemy:
    db_connection = f"mysql+pymysql://{database_connection.db_user}:{database_connection.db_pass}@" \
                    f"{database_connection.db_host}/{database_connection.db_name}"

    # database, from file named db_sqlite.
    app.config['SQLALCHEMY_DATABASE_URI'] = db_connection
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # swagger configurations, initialized following the documentation provided.
    SWAGGER_URL: str = '/api'
    API_URL: str = '/static/swagger.json'

    swaggerui_blueprint = get_swaggerui_blueprint(
            SWAGGER_URL,
            API_URL,
            config={'app_name': "Premier League API"}
    )

    # initialize the mysql database
    db_and_ma: Tuple = DatabaseHandler.create_or_get_db(app)
    # initialize Marshmallow on the application to create schemas, i.e. determine what you expose to the user.

    db_and_ma[0].init_app(app)

    # initialize blueprints
    # They are imported here to avoid circular imports since blueprints function like scripts instead of classes.
    from app.routes.main_routes import main_routes
    from app.routes.coach_routes import coach_routes
    from app.routes.match_routes import match_routes
    from app.routes.player_routes import player_routes
    from app.routes.referee_routes import referee_routes
    from app.routes.team_routes import team_routes

    app.register_blueprint(main_routes)
    app.register_blueprint(coach_routes)
    app.register_blueprint(match_routes)
    app.register_blueprint(player_routes)
    app.register_blueprint(referee_routes)
    app.register_blueprint(team_routes)
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

    return app
