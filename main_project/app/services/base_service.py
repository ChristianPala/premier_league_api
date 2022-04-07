from abc import ABC
from flask import jsonify, request
from sqlalchemy import and_
from typing import Dict, Any, List, Type, Union
from app.database.database_config import DatabaseHandler


# Custom JSON type hint.
JSON = Union[Dict[str, Any], List[Any], int, str, float, bool, Type[None]]


class BaseService(ABC):

    # abstract class to model a base server business logic.

    def __init__(self, model, schemas) -> None:
        """
        constructor for a generic server. remember to insert the single schema first in the
        list of schemas.
        """
        self._model = model
        self._schemas = schemas
        self._db = DatabaseHandler.create_or_get_db()[0]

    def get_items(self) -> JSON:
        """method to fetch all items in the database."""
        all_items = self._model.query.all()
        result = self._schemas[1].dump(all_items)

        return jsonify(result)

    def add_item(self) -> JSON:
        """
        method to add an item to the database.
        """
        new_item = self._schemas[0].load(request.get_json(force=True))
        self._db.session.add(new_item)
        self._db.session.commit()

        return self._schemas[0].dump(new_item)

    def get_item_by_id(self, item_id: int) -> JSON:
        """
        method to fetch an item by id
        """
        selected_item = self._model.query.get(item_id)

        return self._schemas[0].dump(selected_item)

    def delete_item_by_id(self, item_id) -> JSON:
        """
        method to delete an item by id.
        """
        selected_item = self._model.query.get(item_id)
        self._db.session.delete(selected_item)
        self._db.session.commit()

        return self._schemas[0].dump(selected_item)

    def update_item_by_id(self, item_id) -> JSON:
        """
        method to update an item by id.
        """
        selected_item = self._model.query.get(item_id)
        updated_item = self._schemas[0].load(request.get_json(force=True), instance=selected_item, partial=True)
        # since the referee to be updated is attached to a session we use merge to create it in the local session.
        local_updated_item = self._db.session.merge(updated_item)
        self._db.session.add(local_updated_item)
        self._db.session.commit()

        return self._schemas[0].dump(local_updated_item)

    def search_items(self) -> JSON:
        """
        method to search an item by all exposed fields.
        """
        result = self.model_search_request_parsing(self._model, self._schemas[1])
        return result

    def model_search_request_parsing(self, model, schema):
        """
            parses through a search request for a given model and returns the json result:
        """
        args = request.args
        filtered_args = {k: v for k, v in args.items() if v is not None}
        filters = [getattr(model, attribute) == value for attribute, value in filtered_args.items()]
        selected_players = self._db.session.query(model).filter(and_(*filters)).all()
        result = schema.dump(selected_players)
        return jsonify(result)
