import sys
import os
import json

from tests.base import BaseTestCase, CommonTestCases
from fixtures.room_resource.get_room_resource_fixtures import (
    resource_query, resource_query_response, get_room_resources_by_room_id,
    get_room_resources_by_room_id_response, get_room_resources_by_room_id_error,
    get_room_resources_by_room_id_error_response,
    filter_unique_resources, filter_unique_resources_response,
    get_paginated_room_resources,
    get_paginated_room_resources_response,
    get_paginated_resources_past_page,
    get_paginated_resources_inexistent_page
)
from helpers.database import db_session
from fixtures.token.token_fixture import USER_TOKEN

sys.path.append(os.getcwd())


class TestGetRoomResource(BaseTestCase):

    def test_get_room_resource_list(self):

        execute_query = self.client.execute(
            resource_query,
            context_value={'session': db_session})

        expected_responese = resource_query_response
        self.assertEqual(execute_query, expected_responese)

    def test_get_room_resources_by_room_id_error(self):
        response = self.app_test.post(
            '/mrm?query='+get_room_resources_by_room_id_error)
        actual_response = json.loads(response.data)
        expected_response = get_room_resources_by_room_id_error_response
        self.assertEquals(
            actual_response["errors"][0]["message"], expected_response)

    def test_get_room_resources_by_room_id(self):

        execute_query = self.client.execute(
            get_room_resources_by_room_id,
            context_value={'session': db_session})

        expected_responese = get_room_resources_by_room_id_response

        self.assertEqual(execute_query, expected_responese)

    def test_get_unique_resources(self):
        headers = {"Authorization": "Bearer" + " " + USER_TOKEN}
        response = self.app_test.post(
            '/mrm?query='+filter_unique_resources, headers=headers)
        actual_response = json.loads(response.data)
        self.assertEquals(actual_response, filter_unique_resources_response)

    def test_get_paginated_responses(self):
        CommonTestCases.admin_token_assert_equal(
            self,
            get_paginated_room_resources,
            get_paginated_room_resources_response
        )

    def test_get_paginated_resources_in_empty_page(self):
        CommonTestCases.admin_token_assert_in(
            self,
            get_paginated_resources_past_page,
            "No more resources"
        )

    def test_get_paginated_response_with_inexistent_page(self):
        CommonTestCases.admin_token_assert_in(
            self,
            get_paginated_resources_inexistent_page,
            "No page requested"
        )
