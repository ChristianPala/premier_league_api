# Libraries
from flask import Blueprint, Response

# Initialize the main blueprint
main_routes = Blueprint("main", __name__)
# Initialize the minimum package response size:
minimum_request_bytes = 4
# Initialize the resource not found response
resource_not_found = Response("Resource not found.", status=404)


@main_routes.route('/', methods=['GET'])
def home() -> str:
    return "<h1> Premier League API <h1>"

