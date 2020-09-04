from django.urls import path
from . import views

urlpatterns = [
    path("news/<str:company>/<str:date>/<int:page>/", views.news.as_view())
]