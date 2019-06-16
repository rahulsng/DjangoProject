from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
     path('Music/',include('Music.urls')), #localhost:8000/Music
]
