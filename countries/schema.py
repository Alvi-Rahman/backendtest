from ariadne import gql
from ariadne import ObjectType, QueryType, make_executable_schema
from .models import Country, Currency

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

@query.field("countries")
def resolve_countries(_, info):

    return Country.objects.order_by('symbol')


schema = make_executable_schema(type_defs, query, country)
