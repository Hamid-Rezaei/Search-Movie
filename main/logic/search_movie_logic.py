from main.utils.singleton import Singleton


class SearchMovieLogic(metaclass=Singleton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.search_movie_dao = SearchMovieRDDao()

    def search_movie(self, email, audio):
        ...



