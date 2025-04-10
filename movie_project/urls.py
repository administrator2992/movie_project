from django.contrib import admin
from django.urls import path, include  # Add 'include' here

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('movies/', include('movies.urls')),  # Add this line
    path('', include('movies.urls')),  # Optional: For root path
]
