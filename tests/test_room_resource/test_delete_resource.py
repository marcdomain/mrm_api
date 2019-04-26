import sys
import os

from tests.base import BaseTestCase, CommonTestCases
from fixtures.room_resource.delete_room_resource import (
  delete_resource, expected_response_after_delete, delete_non_existent_resource)
from fixtures.room.assign_resource_fixture import (
    assign_resource_mutation,
    assign_resource_mutation_response)


sys.path.append(os.getcwd())


class TestDeleteRoomResource(BaseTestCase):

    def test_delete_resource_mutation_when_not_admin(self):
        CommonTestCases.user_token_assert_in(
            self,
            delete_resource,
            "You are not authorized to perform this action"
        )

    def test_delete_resource_mutation_when_admin(self):
        CommonTestCases.admin_token_assert_equal(
           self,
           assign_resource_mutation,
           assign_resource_mutation_response,
        )
        CommonTestCases.admin_token_assert_equal(
            self,
            delete_resource,
            expected_response_after_delete
        )

    def test_delete_non_existent_resource(self):
        CommonTestCases.admin_token_assert_in(
            self,
            delete_non_existent_resource,
            "Resource not found"
        )

    def test_delete_already_deleted_resource(self):
        CommonTestCases.admin_token_assert_equal(
            self,
            delete_resource,
            expected_response_after_delete
        )
        CommonTestCases.admin_token_assert_in(
            self,
            delete_resource,
            "Resource not found"
        )
