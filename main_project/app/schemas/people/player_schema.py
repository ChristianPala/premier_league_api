# Players Schemas

# Libraries:
from app.models.people.player_model import Player
from app.schemas.people.person_schema import PersonSchema


class PlayerSchema(PersonSchema):
    class Meta:
        fields = ('id', 'name', 'surname', 'birth_date', 'height', 'nationality', 'role')
        model = Player
        include_relationships = True
        load_instance = True

