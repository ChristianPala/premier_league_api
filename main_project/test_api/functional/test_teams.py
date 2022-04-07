import pytest
from marshmallow import ValidationError
from app import create_app
from app.routes.main_routes import resource_not_found


def test_teams_routes():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/teams' page is requested (GET / POST)
    THEN check that the response is valid.
    """
    """
    Warning executing tests will change the database.
    Since we have a simple database we did not create a mock database but manually corrected the test corruption.
    """

    flask_app = create_app('config.TestingConfig')

    # create test client using Flask application:
    with flask_app.test_client() as test_client:
        response = test_client.get('/teams')
        assert response.status_code == 200
        assert b'name' in response.data

    # testing a team is added if name is provided.

    response = test_client.post('/teams', json={'name': 'Lugano', 'address': 'Corso Elvezia 1'})
    assert response.status_code == 200

    # testing a team is not added if name is not provided.
    with pytest.raises(ValidationError):
        response = test_client.post('/teams', json={'stadium': 'Cornaredo'})


def test_team_routes():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/teams/{int: id}' page is requested (GET / PUT / DELET)
    THEN check that the response is valid.
    """

    flask_app = create_app('config.TestingConfig')

    # create test client using Flask application:
    with flask_app.test_client() as test_client:

        # testing normal GET behavior.
        response = test_client.get('/teams/1')
        assert response.status_code == 200
        assert b'Bournemouth' in response.data

        # testing GET resource not found if id not found.
        response = test_client.get('/teams/1000')
        assert response.status_code == 404
        assert b"Resource not found." in response.data

        # testing normal PUT behavior.
        """
        Warning, this modifies the database and impact GET test results.
        """
        response = test_client.put('/teams/1', json={'stadium': 'Piotta'})
        assert response.status_code == 200
        assert b'Piotta' in response.data

        # testing PUT resource not found if id not found.
        response = test_client.put('/teams/1000', json={'stadium': 'England'})
        assert response.status_code == 404
        assert b"Resource not found." in response.data

        # testing DELETE normal behavior.
        """
        Warning, this modifies the database and impacts the next del    ete test.
        """
        response = test_client.delete('/teams/50')
        assert response.status_code == 200
        assert b'"name":"Wolverhampton Wander"' in response.data

        # testing DELETE resource not found
        response = test_client.delete('/teams/1000')
        assert response.status_code == 404
        assert b"Resource not found." in response.data


def test_team_search_route():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/teams/{int: id}' page is requested (GET / PUT / DELET)
    THEN check that the response is valid.
    """

    flask_app = create_app('config.TestingConfig')

    # create test client using Flask application:
    with flask_app.test_client() as test_client:
        # # testing normal GET behavior.
        response = test_client.get('/teams/search?name=Arsenal+FC')
        assert response.status_code == 200
        assert b'Arsenal' in response.data

        # testing search missing resource GET behavior.
        response = test_client.get('/teams/search?name=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
        assert response.status_code == 404
        assert b"Resource not found." in response.data

        # testing combined fields GET behavior.
        response = test_client.get('/teams/search?name=Arsenal%20FC&stadium=Emirates%20Stadium')
        assert response.status_code == 200
        assert b'Arsenal' in response.data

        # Testing not_found response:
        response = resource_not_found
        assert response.status_code == 404
        assert b'Resource not found' in response.data


# Testing not_found response:
def test_resource_not_found():
    response = resource_not_found
    assert response.status_code == 404
    assert b'Resource not found' in response.data
