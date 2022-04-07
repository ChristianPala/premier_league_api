# Libraries:
from app.database.database_config import DatabaseHandler

ma = DatabaseHandler.create_or_get_db()[1]


class PersonSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        fields = ('id', 'name', 'surname', 'birth_date', 'nationality')

