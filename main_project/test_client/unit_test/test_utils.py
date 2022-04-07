# Unit testing the client utility repository.
# Libraries:
from datetime import date
from pl_client.services.utils import string_to_date, date_to_long_string


class TestUtils:
    """
        testing the utility functions for the client library.
    """
    def test_client_string_to_date_none_case(self):
        """
        GIVEN None
        WHEN the utility method is called
        THEN check None is outputted.
        """

        assert string_to_date(None) is None

    def test_client_string_to_date_non_empty_case(self):
        """
        GIVEN None
        WHEN the utility method is called
        THEN check the desired date is outputted.
        """

        assert string_to_date('2022-01-01') == date(2022, 1, 1)

    def test_client_date_to_long_string_zero_case(self):
        """
        GIVEN a day from 1 to 9
        WHEN the utility method is called
        THEN check the desired string is outputted.
        """

        assert date_to_long_string(date(2022, 1, 1)) == "1 of January 2022"

    def test_client_date_to_long_string_non_zero_case(self):
        """
        GIVEN a day from 10 to end of month
        WHEN the utility method is called
        THEN check the desired string is outputted.
        """

        assert date_to_long_string(date(2022, 1, 10)) == "10 of January 2022"

