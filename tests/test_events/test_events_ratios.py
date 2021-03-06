import sys
import os
from unittest.mock import patch

from tests.base import BaseTestCase, CommonTestCases
from helpers.calendar.calendar import get_events_mock_data
from fixtures.events.events_ratios_fixtures import (
    event_ratio_query,
    event_ratio_response,
    event_ratio_for_one_day_query,
    event_ratio_per_room_query,
    event_ratio_per_room_response,
    event_ratio_single_room_query,
    event_ratio_single_room_response,
    event_ratio_single_room_query_with_non_existing_id,
    event_ratio_single_room_with_non_existing_id_response
)

sys.path.append(os.getcwd())


class TestEventRatios(BaseTestCase):
    @patch("helpers.calendar.analytics_helper.get_events_within_datetime_range",
           spec=True)
    def test_events_checkins_to_bookings_ratio_on_date_range(self,
                                                             mock_get_json):
        """
        Test that an admin is able to get the ratio of checkins to bookings
        on a date range
        """
        mock_get_json.return_value = get_events_mock_data()
        CommonTestCases.admin_token_assert_equal(
            self,
            event_ratio_query,
            event_ratio_response
        )

    @patch("helpers.calendar.analytics_helper.get_events_within_datetime_range",
           spec=True)
    def test_events_checkins_to_bookings_ratio_for_single_day(self,
                                                              mock_get_json):
        """
        Test that an admin is able to get the ratio of checkins to bookings
        with a single date supplied
        """
        mock_get_json.return_value = get_events_mock_data()
        CommonTestCases.admin_token_assert_equal(
            self,
            event_ratio_for_one_day_query,
            event_ratio_response
        )

    @patch("helpers.calendar.analytics_helper.get_events_within_datetime_range",
           spec=True)
    def test_event_checkin_and_cancellation_ratio_per_room(self, mock_get_json):
        """
        Test that an admin is able to get the ratio of checkins to bookings
        for each individual room
        """
        mock_get_json.return_value = get_events_mock_data()
        CommonTestCases.admin_token_assert_equal(
            self,
            event_ratio_per_room_query,
            event_ratio_per_room_response
        )

    @patch("helpers.calendar.analytics_helper.get_events_within_datetime_range",
           spec=True)
    def test_event_checkin_and_cancellation_single_room(self, mock_get_json):
        """
        Test that an admin is able to get the ratio of checkins to bookings
        for a single room
        """
        mock_get_json.return_value = get_events_mock_data()
        CommonTestCases.admin_token_assert_equal(
            self,
            event_ratio_single_room_query,
            event_ratio_single_room_response
        )

    @patch("helpers.calendar.analytics_helper.get_events_within_datetime_range",
           spec=True)
    def test_event_checkin_cancellation_single_room_wrong_id(self,
                                                             mock_get_json):
        """
        Tests that an admin cannot get the ratio of check-ins to bookings for a
        single room with invalid room id
        """
        mock_get_json.return_value = get_events_mock_data()
        CommonTestCases.admin_token_assert_equal(
            self,
            event_ratio_single_room_query_with_non_existing_id,
            event_ratio_single_room_with_non_existing_id_response
        )

    def test_database_connection_error(self):
        """
        test a user friendly message is returned to a user when database
        cannot be reached
        """
        BaseTestCase().tearDown()
        CommonTestCases.admin_token_assert_in(
            self,
            event_ratio_query,
            "The database cannot be reached"
        )
        CommonTestCases.admin_token_assert_in(
            self,
            event_ratio_for_one_day_query,
            "The database cannot be reached"
        )
        CommonTestCases.admin_token_assert_in(
            self,
            event_ratio_per_room_query,
            "The database cannot be reached"
        )
