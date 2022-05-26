from ariadne import gql
from ariadne import ObjectType, QueryType, make_executable_schema
from django.db.models import Q
from .models import Country

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

# Task 1
@query.field("countries")
def resolve_countries(obj, info):
    # Used `symbol` as per example as `name` doesn't produce the example output provided
    return Country.objects.order_by('symbol')


# Task 2
# @query.field("countries")
# def resolve_currencies(*obj, currencies=None):
#
#     countries = Country.objects.prefetch_related('currencies')
#     lst = []
#     for c in countries:
#         lst.append({**c.__dict__, **{"currencies": c.currencies.order_by('name')}})
#
#     return lst


# Task 2 and 3
@query.field("countries")
def resolve_country_and_currencies(*_, currencies=None, search=None):
    if search:
        countries = Country.objects.filter(
            Q(name__icontains=search) | Q(symbol__icontains=search)
        ).prefetch_related('currencies')
    else:
        countries = Country.objects.prefetch_related('currencies')

    # Couldn't find any other alternatives (as per StackOverflow and Stack Exchange)
    # for GraphQL other than using for loop
    # In case of Serializers adding (many=True) would have done the work

    lst = []
    for c in countries:
        lst.append({**c.__dict__, **{"currencies": c.currencies.order_by('name')}})

    return lst


schema = make_executable_schema(type_defs, query, country)
