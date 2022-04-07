import pytest
from marshmallow import ValidationError
from app import create_app
from app.routes.main_routes import resource_not_found


def test_referees_routes():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/referees' page is requested (GET / POST)
    THEN check that the response is valid.
    """
    """
    Warning executing tests will change the database.
    Since we have a simple database we did not create a mock database but manually corrected the test corruption.
    """

    flask_app = create_app('config.TestingConfig')

    # create test client using Flask application:
    with flask_app.test_client() as test_client:
        response = test_client.get('/referees')
        assert response.status_code == 200
        assert b'name' in response.data

    # testing a referee is added if name is provided.

    response = test_client.post('/referees', json={'name': 'Alan'})
    assert response.status_code == 200

    # testing a referee is not added if name is not provided.
    with pytest.raises(ValidationError):
        response = test_client.post('/referees', json={'surname': 'mars'})


def test_referee_routes():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/referees/{int: id}' page is requested (GET / PUT / DELET)
    THEN check that the response is valid.
    """

    flask_app = create_app('config.TestingConfig')

    # create test client using Flask application:
    with flask_app.test_client() as test_client:

        # testing normal GET behavior.
        response = test_client.get('/referees/1')
        assert response.status_code == 200
        assert b'{"birth_date":"1960-05-27","name":"Alan","nationality":"England","surname":"Wiley"}' in response.data

        # testing GET resource not found if id not found.
        response = test_client.get('/referees/1000')
        assert response.status_code == 404
        assert b"Resource not found." in response.data

        # testing normal PUT behavior.
        """
        Warning, this modifies the database and impact GET test results.
        """
        response = test_client.put('/referees/1', json={'nationality': 'France'})
        assert response.status_code == 200
        assert b'{"birth_date":"1960-05-27","name":"Alan","nationality":"France","surname":"Wiley"}' in response.data

        # testing PUT resource not found if id not found.
        response = test_client.put('/referees/1000', json={'nationality': 'England'})
        assert response.status_code == 404
        assert b"Resource not found." in response.data

        # testing DELETE normal behavior.
        """
        Warning, this modifies the database and impacts the next delete test.
        """
        response = test_client.delete('/referees/92')
        assert response.status_code == 200
        assert b'"name":"Tony"' in response.data

        # testing DELETE resource not found
        response = test_client.delete('/referees/1000')
        assert response.status_code == 404
        assert b"Resource not found." in response.data


def test_referee_search_route():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/referees/{int: id}' page is requested (GET / PUT / DELET)
    THEN check that the response is valid.
    """

    flask_app = create_app('config.TestingConfig')

    # create test client using Flask application:
    with flask_app.test_client() as test_client:
        # # testing normal GET behavior.
        response = test_client.get('/referees/search?name=Alan')
        assert response.status_code == 200
        assert b'Alan' in response.data

        # testing search missing resource GET behavior.
        response = test_client.get('/referees/search?name=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
        assert response.status_code == 404
        assert b"Resource not found." in response.data

        # testing combined fields GET behavior.
        response = test_client.get('/referees/search?name=Alan&surname=Wiley')
        assert response.status_code == 200
        assert b'Alan' in response.data


# Testing not_found response:
def test_resource_not_found():
    response = resource_not_found
    assert response.status_code == 404
    assert b'Resource not found' in response.data

