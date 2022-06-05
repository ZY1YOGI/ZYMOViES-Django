from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexHome.as_view(), name='home'),
    path("search/", views.search, name="search"),
    path("test/", views.test, name="test"),
    path("tv/<int:tv_id>/", views.view_tv_detail, name="tvdetail"),
    path("movie/<int:movie_id>/", views.view_movie_detail, name="moviedetail"),
]