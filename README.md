# Vibely

This web app tries to bring together bands and establishments that wants to make an event of music

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

You will need to have installed docker and docker-compose. To know if this is working properly use
`docker run hello-world` and `docker-compose --version`. To get them installed properly at your OS, 
  refer to the oficial pages of docker and use:
  ```
  python3 -m pip install docker-compose
  ```

### Installing

Copy '.env.example' to file named '.env'. Then change the variable `DJANGO_SECRET_KEY=[key]`
to a value generated. For example, using [this site](https://miniwebtool.com/django-secret-key-generator/).

So the contents of .env should be:
```
#Django configuration 

OPEN_PORT=8000
DJANGO_PORT=8000

DJANGO_SECRET_KEY=<your secret key goes here>
DJANGO_DEBUG=1
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1] 0.0.0.0

POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=db
POSTGRES_PORT=5432
POSTGRES_NAME=postgres

DATABASE_URL=postgres://postgres:postgres@db:5432/postgres
#DATABASE_URL=postgres://USER:PASSWORD@HOST:PORT/NAME
```

Then apply the changes to you database using:
```
docker-compose exec web python3 manage.py makemigrations
docker-compose exec web python3 manage.py migrate
```

To create a super user, use:
`docker-compose exec web python3 manage.py createsuperuser`

Then use `docker-compose up -d` to get it running. Connect to `localhost:8000/admin`
to see the admin login page

To stop it, use `docker-compose down`

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Master branch is deployed in CI/CD at [this site](https://vibely-udl.herokuapp.com/admin/)

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

