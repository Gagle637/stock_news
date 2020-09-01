from django.urls import path
from . import views

urlpatterns = [
    path("news/", views.news.as_view())
]