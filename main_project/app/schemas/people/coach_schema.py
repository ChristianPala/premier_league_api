# Coach schema
from app.models.people.coach_model import Coach
from app.schemas.people.person_schema import PersonSchema


class CoachSchema(PersonSchema):
    class Meta:
        fields = ('id', 'name', 'surname', 'nationality')
        model = Coach
        include_relationships = True
        load_instance = True


