from tests.base import BaseTestCase, CommonTestCases
from fixtures.room_resource.update_resource_fixtures import (
    update_room_resource_query,
    non_existant_resource_id_query,
    update_room_resource_negative_integer,
    expected_update_room_resource_negative_integer
)

import os
import sys
sys.path.append(os.getcwd())


class TestUpdateRoomResorce(BaseTestCase):

    def test_update_resource_mutation_by_non_admin(self):
        CommonTestCases.user_token_assert_in(
            self,
            update_room_resource_query,
            "You are not authorized to perform this action"
        )

    def test_update_resource_mutation_by_admin(self):
        CommonTestCases.admin_token_assert_in(
            self,
            update_room_resource_query,
            "Markers"
        )

    def test_update_resource_mutation_with_invalid_resource_id(self):
        CommonTestCases.admin_token_assert_in(
            self,
            non_existant_resource_id_query,
            "Resource not found"
        )

    def test_update_resource_mutation_with_negative_integer(self):
        CommonTestCases.admin_token_assert_equal(
            self,
            update_room_resource_negative_integer,
            expected_update_room_resource_negative_integer
        )
