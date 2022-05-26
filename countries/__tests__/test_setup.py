from django.test import TestCase, Client
import json
from string import Template


class TestSetUp(TestCase):
    def setUp(self):

        query = Template("""
            query {
                  countries(search: "${filter}") {
                    name
                    symbol
                    currencies {
                      name
                      symbol
                    }
                  }
                }
            """)
        self.aus_query = query.substitute(filter='aus')

        self.client = Client()
        self.GRAPHQL_URL = "/graphql/"

        self.aus_filter_response = json.loads("""
        {
          "data": {
            "countries": [
              {
                "name": "Australia",
                "symbol": "AUS",
                "currencies": [
                  {
                    "name": "Australian Dollar",
                    "symbol": "AUD"
                  }
                ]
              },
              {
                "name": "Austria",
                "symbol": "AUT",
                "currencies": [
                  {
                    "name": "Euro",
                    "symbol": "EUR"
                  }
                ]
              }
            ]
          }
        }
        """)

        self.gbr_filter_response = json.loads("""
                {
                  "data": {
                    "countries": [
                      {
                        "name": "United Kingdom of Great Britain and Northern Ireland",
                        "symbol": "GBR",
                        "currencies": [
                          {
                            "name": "Pound Sterling",
                            "symbol": "GBP"
                          }
                        ]
                      }
                    ]
                  }
                }
                """)

        return super(TestSetUp, self).setUp()

    def tearDown(self):
        return super(TestSetUp, self).tearDown()

