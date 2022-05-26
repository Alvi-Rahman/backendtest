import pytest
from django.test import Client, TestCase
import json
import os
from django.db import connection

from countries.__tests__.test_setup import TestSetUp

pytestmark = [pytest.mark.django_db]

GRAPHQL_URL = "/graphql/"


def test_graphql_countries():

    query = """
    query {
        countries {
            name
            symbol
            currencies {
                name
                symbol
            }
        }
    }
    """

    client = Client()
    response = client.post(
        GRAPHQL_URL,
        {"query": query},
        content_type="application/json",
    )

    print(len(connection.queries))

    assert response.status_code == 200
    assert response.json().get("errors") is None

    # TODO Make assertions on the returned JSON
    file_path = (os.path.dirname(__file__)) + "/task_2_expected_output.json"
    with open(file_path, "r+") as f:
        assert json.loads(f.read()) == response.json()

    # TODO Make assertions on the number of database queries
    TestCase().assertNumQueries(2)


# TODO Test querying with the filter as well
class TestGraphQlCountriesWithFilter(TestSetUp):
    def test_with_aus_filter(self):
        response = self.client.post(
            self.GRAPHQL_URL,
            {"query": self.aus_query},
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 200)
        self.assertIsNone(response.json().get("errors"))

        self.assertEqual(self.aus_filter_response, response.json())

    def test_with_gbr_filter(self):
        response = self.client.post(
            self.GRAPHQL_URL,
            {"query": self.gbr_query},
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 200)
        self.assertIsNone(response.json().get("errors"))

        self.assertEqual(self.gbr_filter_response, response.json())

    def test_with_no_filter(self):
        response = self.client.post(
            self.GRAPHQL_URL,
            {"query": self.no_filter_query},
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 200)
        self.assertIsNone(response.json().get("errors"))

        self.assertEqual(self.no_filter_response, response.json())
