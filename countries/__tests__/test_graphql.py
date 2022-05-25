import pytest
from django.test import Client
import json
import os

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

    assert response.status_code == 200
    assert response.json().get("errors") is None

    # TODO Make assertions on the returned JSON
    file_path = (os.path.dirname(__file__)) + "/task_2_expected_output.json"
    with open(file_path, "r+") as f:
        assert json.loads(f.read()) == response.json()

    # TODO Make assertions on the number of database queries
    

# TODO Test querying with the filter as well
