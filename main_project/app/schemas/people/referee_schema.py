# Referee Schemas

# Libraries:
from app.models.people.referee_model import Referee
from app.schemas.people.person_schema import PersonSchema


class RefereeSchema(PersonSchema):
    class Meta:
        fields = ('id', 'name', 'surname', 'birth_date', 'nationality')
        model = Referee
        include_relationships = True
        load_instance = True

