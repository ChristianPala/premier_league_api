from app import create_app
from app.routes.main_routes import resource_not_found


def test_home_page():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid.
    """

    flask_app = create_app('config.TestingConfig')

    # create test client using Flask application:
    with flask_app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200
        assert b'Premier League API' in response.data

        """
        GIVEN a Flask application configured for testing
        WHEN the '/' page is requested (POST)
        THEN check that the response is a method not allowed: 405.
        """
        response = test_client.post('/')
        assert response.status_code == 405
        assert b'API' not in response.data


# Testing not_found response:
def test_resource_not_found():
    response = resource_not_found
    assert response.status_code == 404
    assert b'Resource not found' in response.data
