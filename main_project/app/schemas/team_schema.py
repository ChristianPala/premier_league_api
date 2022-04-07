# Teams Schemas

# Libraries:
from app import DatabaseHandler
from app.models.team_model import Team


ma = DatabaseHandler.create_or_get_db()[1]


class TeamSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        fields = ('id', 'name', 'address', 'stadium', 'url')
        model = Team
        include_relationships = True
        load_instance = True
