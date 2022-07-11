# Django Rest Framework API for Redux Toolkit Testing 
## Summary 

A simple Django Rest Framework app to work with the [Redux Toolkit](https://redux-toolkit.js.org/rtk-query/usage-with-typescript).

A number of API end points are provided to interact with a database of movie information.

## API Documentation

The API endpoints are documented as part of the project and can be accessed at http://127.0.0.1:8000/swagger .

## Sample API calls

### Movies 

#### ADD a new movie

```
curl -X POST http://127.0.0.1:8000/movies -H 'Content-Type: application/json' -d '{"audience_score_percent": "55", "film": "Test Film 2", "genre": "Comedy", "lead_studio": "Warner Bros.", "profitability": "1.9802064", "rotten_tomatoes_percent": "8", "worldwide_gross_usd": "$69.31 ", "year": "2017"}'

```


## Credits
The initial movie data, movie.csv, is from https://gist.github.com/tiangechen/b68782efa49a16edaf07dc2cdaa855ea which has no explicit license so I'm assuming is free to use, I'm happy to remove it from the project if anyone wishes to complain.
