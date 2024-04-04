from django.urls import path

from main.api.controller.search_movie_controller import SearchMovieController

urlpatterns = [
    path(
        'main/search/movie',
        SearchMovieController.as_view(),
        name='search-movie'
    ),
]
