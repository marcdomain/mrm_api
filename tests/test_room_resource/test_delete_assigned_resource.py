from tests.base import BaseTestCase, CommonTestCases
from fixtures.room_resource.delete_assigned_resource_fixtures import (
    delete_assigned_resource_mutation,
    delete_non_existing_assigned_resource_mutation,
    delete_assigned_resource_response)
from fixtures.room.assign_resource_fixture import (
    assign_resource_mutation,
    assign_resource_mutation_response)


class TestDeleteAssignedResorce(BaseTestCase):

    def test_delete_assigned_resource_by_non_admin(self):
        """
        Test that non admin accounts cannot delete an
        assigned resource
        """
        CommonTestCases.user_token_assert_in(
            self,
            delete_assigned_resource_mutation,
            "You are not authorized to perform this action"
        )

    def test_delete_non_existing_assigned_resource(self):
        """
        Test that an admin cannot delete an assigned resource
        that does not exist
        """
        CommonTestCases.admin_token_assert_in(
            self,
            delete_non_existing_assigned_resource_mutation,
            "Resource does not exist in the room"
        )

    def test_delete_assigned_resource_by_admin(self):
        """
        Test that admins can delete an assigned room resource
        """
        CommonTestCases.admin_token_assert_equal(
            self,
            assign_resource_mutation,
            assign_resource_mutation_response,
        )

        CommonTestCases.admin_token_assert_equal(
            self,
            delete_assigned_resource_mutation,
            delete_assigned_resource_response
        )
