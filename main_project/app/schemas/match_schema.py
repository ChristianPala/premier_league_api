# Matches Schemas

# Libraries:
from app import DatabaseHandler
from app.models.match_model import Match

ma = DatabaseHandler.create_or_get_db()[1]


class MatchSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        fields = ('home', 'away', 'day', 'season_start', 'season_end', 'result')
        model = Match
        include_relationships = True
        load_instance = True

