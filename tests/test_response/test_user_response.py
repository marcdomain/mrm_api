import sys
import os
from tests.base import BaseTestCase, CommonTestCases
from fixtures.response.user_response_fixtures import (
    create_rate_query,
    create_rate_response,
    invalid_rating_number,
    rate_with_non_existent_room
)
from fixtures.response.user_response_check import (
    check_non_existing_question,
    check_with_non_existent_room,
    filter_question_by_room,
    filter_question_by_room_response,
    filter_question_by_invalid_room,
    filter_question_by_invalid_room_response,
    create_check_query,
    create_check_response,
    create_check_query_non_existence_item
)
from fixtures.response.user_response_suggestions import (
    create_suggestion_question,
    create_suggestion_question_response,
    make_suggestion_in_non_existent_room
)


sys.path.append(os.getcwd())


class TestCreateResponse(BaseTestCase):

    def test_create_rate(self):
        """
        Testing for creating rates

        """
        CommonTestCases.user_token_assert_equal(
            self,
            create_rate_query,
            create_rate_response
        )

    def test_invalid_rating_number(self):
        """
        Testing for invalid rating number

        """
        CommonTestCases.user_token_assert_in(
            self,
            invalid_rating_number,
            "Please rate between 1 and 5"
        )

    def test_rate_non_existent_room(self):
        """
        Testing for invalid rating number

        """
        CommonTestCases.user_token_assert_in(
            self,
            rate_with_non_existent_room,
            "Non-existent room id"
        )

    def test_check_wrong_question(self):
        """
        Testing for invalid check number

        """
        CommonTestCases.user_token_assert_in(
            self,
            check_non_existing_question,
            "Response to question"
        )

    def test_check_non_existent_room(self):
        """
        Testing for invalid check number

        """
        CommonTestCases.user_token_assert_in(
            self,
            check_with_non_existent_room,
            "Non-existent room id"
        )

    def test_create_check(self):
        """
        Testing for creating check

        """
        CommonTestCases.user_token_assert_equal(
            self,
            create_check_query,
            create_check_response
        )

    def test_check_non_existence_missing_items(self):
        """
        Testing for no missing items list
        """
        CommonTestCases.user_token_assert_in(
            self,
            create_check_query_non_existence_item,
            "one of the resource provided does not exist"
        )

    def test_create_suggestion(self):
        """
        Testing for invalid rating number

        """
        CommonTestCases.user_token_assert_equal(
            self,
            create_suggestion_question,
            create_suggestion_question_response
        )

    def test_suggestion_on_non_existent_room(self):
        """
        Testing for invalid rating number

        """
        CommonTestCases.user_token_assert_in(
            self,
            make_suggestion_in_non_existent_room,
            "Non-existent room id"
        )

    def test_filter_response_by_valid_room_id(self):
        """
        Testing for creating rates

        """
        CommonTestCases.admin_token_assert_equal(
            self,
            filter_question_by_room,
            filter_question_by_room_response
        )

    def test_filter_response_by_invalid_room_id(self):
        """
        Testing for creating rates

        """
        CommonTestCases.admin_token_assert_equal(
            self,
            filter_question_by_invalid_room,
            filter_question_by_invalid_room_response
        )
