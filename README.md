# AC Backend Coding Test

## Installing

0. This requires Python 3.7 or later.
1. Fork this repo and clone it locally on your dev machine.
2. Install the necessary libraries with `pip install -r requirements.txt`. Use of a virtualenv or some other way of isolating library installations is strongly recommended.
2. Note that unlike a production Django repo, note that this comes with a local database checked in, `db.sqlite3`, with data already in it. There is no need to migrate or import any data.
3. Check that this runs OK with `./manage.py runserver`. A server should start on [http://localhost:8000/](http://localhost:8000/) and it should display "Hello, world" at that URL.

This app uses the Ariadne library for the graphql endpoint. If you are not familiar with it then check it out at [https://ariadnegraphql.org/](https://ariadnegraphql.org/) and familiarise yourself with how it works.

## The tasks

This Django app is a simple GraphQL API. The database is filled with data about countries of the world and their currencies. The structure of this data is detailed in `countries/models.py` and is quite simple.

If you open the database file `db.sqlite3` in a database editor, you will see the Country & Currency tables have been filled with data, as has the table for the many-to-many relation between them.

The tasks are to create a graphql API to access country info, using the existing data in the database.

### Task 1

With the dev server running, go to: [http://localhost:8000/graphql/](http://localhost:8000/graphql/)

Enter the following query in the left hand panel:

```
query {
  countries {
    name
    symbol
  }
}
```

An error will come up (`Cannot return null...`) in the right hand panel. This is because no resolver for `countries` has been defined yet.s

This task is as follows: Open `countries/schema.py` and add a resolver for the `countries` query so that it returns a list of all the countries in the countries table, sorted alphabetically by name, like this:

![](/images/screenshot1.png)

### Task 2

Update the query in the panel to:

```
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
```

And run it. There will be an error (`__call__() takes 1 positional argument but 2 were given...`).

This task is as follows: Add a resolver for the `currencies` field on Country so that it returns that particular country's currencies, sorted alphabetically by name, as below:

![](/images/screenshot2.png)

### Task 3

Update the query in the panel to:

```
query {
  countries(search: "aus") {
    name
    symbol
    currencies {
      name
      symbol
    }
  }
}
```

And run. You will likely get an error again (`got an unexpected keyword argument 'search').

This task is as follows: Update your resolver for `countries` so that, if a search term is provided, it optionally filters the list of countries to only include those with the search term in either its name _or_ its symbol. The search should be case-insensitive. If no search is provided, then list all countries.

So a search for `"aus"` should return a list containing Australia & Austria, while a search for `"gbr"` should return a list containing just the United Kingdom only:

![](/images/screenshot3.png)
![](/images/screenshot4.png)

### Task 4

Add a way of measuring the number of queries your API calls are making, and optimize the queries in your resolvers you are making so that the fewest possible database queries are being made.

### Task 5

On the command line in a new terminal, run:

    pytest

This will call `countries/__tests__/test_graphql.py`, which runs a simple test of the graphql endpoint. It should pass, if the above tasks are written correctly.

However, the test needs completing. Firstly, the query given should have assertions on it to make sure the number of results returned is as expected, and the number of database queries is as efficient as possible.

Secondly, there should also be tests to make sure the filters work and are returning results for searching for `aus` and `gbr` (as illustrated above) correctly.

Bonus sub-task: you could also add capability to measure test coverage so that we know for sure every line of code has been tested.

### Task 6 (optional)

If you have time and the inclination, write a graphql query called `currencies` that does the reverse of the above - i.e. lists all currencies and the country or countries that use each one, and implement it in `schema.py`.

### Finally

Save all you changes & push them to your forked version of this repository, and email us back the URL to your forked version. Do not file a pull request (or else other candidates will see your work).
