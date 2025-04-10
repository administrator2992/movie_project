## Step 1

Generate your project
```bash
django-admin startproject <your_project_name>
django-admin startapp <your_app_name>
```

## Step 2

Define app model at `<your_app_name>/models.py` to generate the database table

Example :
```python3
from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    img_path = models.CharField(max_length=200)
    duration = models.PositiveIntegerField()
    genre = models.CharField(max_length=200)
    language = models.CharField(max_length=50)
    mpaa_type = models.CharField(max_length=10)
    mpaa_label = models.CharField(max_length=100)
    user_rating = models.CharField(max_length=5)

    def __str__(self):
        return self.name
```

If any this code or no code like attached below at `movie_project/settings.py`, change/add the code as below
```python3
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [BASE_DIR / 'static']
```

add app database config at `<your_app_name>/apps.py`

Example :
```python3
from django.apps import AppConfig


class MoviesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'movies'
```

## Step 3

Generate database table

```bash
python manage.py makemigrations
python manage.py migrate
```

## Step 4

Load initial data if any

```bash
python manage.py loaddata your_inital_data.json
```

Make sure the initial data has been converted to fixtures json

Example of fixtures json :
```python3
 fixture_entry = {
    "model": "<your_app_name>.<your_model_class_lowercase_name>",
    "pk": <primary_key>,
    "fields": {
        "details": any,
        .. : ..,

    }
}
```
the detail of fields should be same as the model setting at `<your_app_name>/models.py`

## Step 5

Create web page setting at `<your_app_name>/views.py`

Example :
```python3
from django.views.generic import ListView, DetailView
from .models import Movie

class MovieListView(ListView):
    model = Movie
    template_name = 'movies/index.html'
    context_object_name = 'movies'

class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movies/detail.html'
    context_object_name = 'movie'
```

## Step 6

Configure the url route for each web page view

Example :

```python3
from django.urls import path
from .views import MovieListView, MovieDetailView

urlpatterns = [
    path('', MovieListView.as_view(), name='movie_list'),
    path('<int:pk>/', MovieDetailView.as_view(), name='movie_detail'),
]
```

The view (template) is explained in the file itself. Please check files in `templates/movies`, `static/css/style.css`, and `static/js/search.js`