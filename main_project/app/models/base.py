from flask_sqlalchemy import SQLAlchemy
# Initialize the sql alchemy database connection for all models.
from app.database.database_config import DatabaseHandler

db = DatabaseHandler.create_or_get_db()[0]
