# Movie Lists and Detail Project

Build simple movie lists app web based.

## Prerequisite

*Recommended*

```bash
# install python env on base python3
python3 -m venv <your_env_name>

# install conda env
conda create -n <your_env_name>
```

Install the requirement framework
```bash
# base python3
pip install -r requirements.txt

# conda
conda install --file requirements.txt
```

Make migration if any change at `movies/models.py`
```bash
python manage.py makemigrations movies && python manage.py migrate
```

Migrate if any change at `movie_project/settings.py` or after pulling and any update this repo
```bash
python manage.py migrate
```

## Run this app on local

```bash
python3 manage.py runserver
```

## Run this app on docker

Build docker based on `docker-compose.yaml` (create that file first)

`docker-compose.yaml` example
```yaml
services:
  web:
    build: .
    volumes:
      - ./db.sqlite3:/app/db.sqlite3  # Database persistence
      - ./staticfiles:/app/staticfiles  # Collected static files
    ports:
      - "8000:8000"
    environment:
      - DEBUG=False
      - ALLOWED_HOSTS=localhost,127.0.0.1
      - SECRET_KEY=your-secret-key
    restart: unless-stopped
```

```bash
# Clean build (if existing)
docker-compose down -v

docker-compose build
docker-compose up
```

## Notes

If `movies/fixtures/movies.json` is not found, please generate fixtures json by using `convert_fixtures.py` program. add your API key of TMDB after `convert_fixtures.py` (`python3 convert_fixtures.py api_key`). Create your TMDB account first and then create new API key at https://www.themoviedb.org. Please read the documentation at https://developer.themoviedb.org/docs/getting-started.

Follow the tutorial at `tutorial.md` if you want to build your own app.