from tests.base import BaseTestCase, CommonTestCases

from helpers.database import engine, db_session
from fixtures.floor.update_floor_fixtures import (
    update_floor_mutation,
    update_with_empty_field,
    update_with_nonexistent_floor_id,
    floor_mutation_duplicate_name,
    floor_mutation_duplicate_name_response
)


class TestUpdateFloor(BaseTestCase):
    def test_if_all_fields_updates(self):
        CommonTestCases.admin_token_assert_in(
            self,
            update_floor_mutation,
            "2nd"
        )

    def test_floor_update_with_name_empty(self):
        CommonTestCases.admin_token_assert_in(
            self,
            update_with_empty_field,
            "name is required field"
        )

    def test_floor_update_with_duplicate_name(self):
        CommonTestCases.admin_token_assert_equal(
            self,
            floor_mutation_duplicate_name,
            floor_mutation_duplicate_name_response
        )

    def test_for_error_if_floor_id_is_non_existant_room(self):
        CommonTestCases.admin_token_assert_in(
            self,
            update_with_nonexistent_floor_id,
            "Floor not found")

    def test_update_floor_that_is_not_in_admin_location_throws_errors(self):
        CommonTestCases.lagos_admin_token_assert_in(
            self,
            update_floor_mutation,
            "You are not authorized to make changes in Kampala")

    def test_database_connection_error(self):
        """
        test a user friendly message is returned to a user when database
        cannot be reached
        """
        BaseTestCase().tearDown()
        CommonTestCases.admin_token_assert_in(
            self,
            update_floor_mutation,
            "The database cannot be reached"
            )

    def test_update_floors_without_floors_relation(self):
        """
        Test a user cannot delete a floor without floor relation
        """
        db_session.remove()
        with engine.begin() as conn:
            conn.execute("DROP TABLE floors CASCADE")
        CommonTestCases.admin_token_assert_in(
          self,
          update_floor_mutation,
          "does not exist"
        )
