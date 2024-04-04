from main.dal.rddao.search_movie_rddao import SearchMovieRDDao
from main.utils.singleton import Singleton


class SearchMovieLogic(metaclass=Singleton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.search_movie_rddao = SearchMovieRDDao()
        self.search_movie_esdao = SearchMovieESDao()

    def search_movie(self, email, audio):
        result = self.search_movie_rddao.get_cached_search_result()

        if not result:
            result = self.search_movie_esdao()
            if result:
                self.search_movie_rddao.cache_search_result()
            else:
             ... #TODO: call api

        result = self.search_movie_rddao.get_cached_search_result()
        movie_info = None

        return movie_info



