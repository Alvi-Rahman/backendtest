from ariadne import gql
from ariadne import ObjectType, QueryType, make_executable_schema

type_defs = gql(
    """
    type Country {
        name: String!
        symbol: String!
        currencies: [Currency!]!
    }
    type Currency {
        name: String!
        symbol: String!
    }
    type Query {
        countries(search: String): [Country!]!
    }
"""
)


query = QueryType()
country = ObjectType("Country")


# TODO: Add resolvers here


schema = make_executable_schema(type_defs, query, country)
