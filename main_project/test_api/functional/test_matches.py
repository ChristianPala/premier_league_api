import pytest
from marshmallow import ValidationError
from app import create_app
from app.routes.main_routes import resource_not_found


def test_matches_routes():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/matches' page is requested (GET / POST)
    THEN check that the response is valid.
    """
    """
    Warning executing tests will change the database.
    Since we have a simple database we did not create a mock database but manually corrected the test corruption.
    """

    flask_app = create_app('config.TestingConfig')

    # create test client using Flask application:
    with flask_app.test_client() as test_client:
        response = test_client.get('/matches')
        assert response.status_code == 200
        assert b'[{"away":"Arsenal FC",' in response.data

    # testing a match is added if name is provided.
    response = test_client.post('/matches', json={'home': 'Lugano', 'away': 'Chiasso',
                                                  'day': "2021-09-10", 'result': '1-0',
                                                  'season_start': '2021-08-13', 'season_end': '2022-05-22'})
    assert response.status_code == 200

    # testing a match is not added if the correct fields are not provided.
    with pytest.raises(ValidationError):
        response = test_client.post('/matches', json={'home': 'Cornaredo'})


def test_match_routes():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/matches/{int: id}' page is requested (GET / PUT / DELET)
    THEN check that the response is valid.
    """

    flask_app = create_app('config.TestingConfig')

    # create test client using Flask application:
    with flask_app.test_client() as test_client:

        # testing normal GET behavior.
        response = test_client.get('/matches/432')
        assert response.status_code == 200
        assert b'Brentford' in response.data

        # testing GET resource not found if id not found.
        response = test_client.get('/matches/1000')
        assert response.status_code == 404
        assert b"Resource not found." in response.data

        # testing normal PUT behavior.
        """
        Warning, this modifies the database and impact GET test results.
        """
        response = test_client.put('/matches/432', json={'home': 'Locarno'})
        assert response.status_code == 200
        assert b'Locarno' in response.data

        # testing PUT resource not found if id not found.
        response = test_client.put('/matches/1000', json={'home': 'Lugano'})
        assert response.status_code == 404
        assert b"Resource not found." in response.data

        # testing DELETE normal behavior.
        """
        Warning, this modifies the database and impacts the next delete test.
        """
        response = test_client.delete('/matches/432')
        assert response.status_code == 200
        assert b'"home":"Locarno"' in response.data

        # testing DELETE resource not found
        response = test_client.delete('/matches/1000')
        assert response.status_code == 404
        assert b"Resource not found." in response.data


def test_match_search_route():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/matches/{int: id}' page is requested (GET / PUT / DELET)
    THEN check that the response is valid.
    """

    flask_app = create_app('config.TestingConfig')

    # create test client using Flask application:
    with flask_app.test_client() as test_client:
        # # testing normal GET behavior.
        response = test_client.get('/matches/search?home=Arsenal%20FC')
        assert response.status_code == 200
        assert b'Arsenal' in response.data

        # testing search missing resource GET behavior.
        response = test_client.get('/matches/search?home=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
        assert response.status_code == 404
        assert b"Resource not found." in response.data

        # testing combined fields GET behavior.
        response = test_client.get('/matches/search?result=3:0&home=Chelsea%20FC')
        assert response.status_code == 200
        assert b'Chelsea' in response.data

        # Testing not_found response:
        response = resource_not_found
        assert response.status_code == 404
        assert b'Resource not found' in response.data


# Testing not_found response:
def test_resource_not_found():
    response = resource_not_found
    assert response.status_code == 404
    assert b'Resource not found' in response.data
