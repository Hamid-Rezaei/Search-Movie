from main.utils.common_base_rddao import CommonsBaseRDDao, RDKey
from main.utils.singleton import Singleton


class SearchMovieRDDao(CommonsBaseRDDao, metaclass=Singleton):
    MOVIE_KEY = RDKey('movie:{title}', ttl=None)

    def cache_search_result(self, title: str, value: str):
        key = self.MOVIE_KEY.key.format(title=title)
        self.client.sadd(key, *value)

    def get_cached_search_result(self, title: str):
        key = self.MOVIE_KEY.key.format(title=title)
        return self.client.smembers(key)
