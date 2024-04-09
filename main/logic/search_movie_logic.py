import requests

from main.dal.elsdao.search_movie_elsdao import SearchMovieESDao
from main.dal.rddao.search_movie_rddao import SearchMovieRDDao
from main.utils.singleton import Singleton
from project.configuration.config import Config
from project.configuration.configuration import Configuration


class SearchMovieLogic(metaclass=Singleton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.search_movie_rddao = SearchMovieRDDao()
        self.search_movie_esdao = SearchMovieESDao(Config.ELASTIC_SEARCH_INDEX_NAME)

    def _search_movie_in_elasticsearch(self, title):
        query = {
            "match": {
                "Series_Title": f"{title}"
            }
        }

        return self.search_movie_esdao.search_documents(query=query)[0]['_source'].get('Poster_Link')

    def _search_movie_in_rapid_api(self, title):
        url = "https://imdb-search2.p.rapidapi.com/the%20game"

        headers = {
            "X-RapidAPI-Key": "a936da7104msh4f5d3eb7358a19cp14b04bjsnb3f9dd254e78",
            "X-RapidAPI-Host": "imdb-search2.p.rapidapi.com"
        }

        response = requests.get(url, params=title, headers=headers)

        return response.json()

    def search_movie(self, query):
        result = self.search_movie_rddao.get_cached_search_result(title=query)

        if not result:
            result = self._search_movie_in_elasticsearch(title=query)
            if result:
                self.search_movie_rddao.cache_search_result(title=query, value=result)
            else:
                # call api
                result = self._search_movie_in_rapid_api(query)
                if result:
                    self.search_movie_rddao.cache_search_result(title=query, value=result)
                else:
                    raise Exception('Movie not found')

        movie_url = self.search_movie_rddao.get_cached_search_result(title=query)

        return movie_url


if __name__ == '__main__':
    Configuration.configure(Config)
    s = SearchMovieLogic()
    # print(s._search_movie_in_elasticsearch('Game of Thrones'))
    # print(s._search_movie_in_rapid_api('Game of Thrones'))
    s.search_movie_rddao.cache_search_result('Game of Thrones', s._search_movie_in_elasticsearch('Game of Thrones'))
    print(s.search_movie_rddao.get_cached_search_result(title='Game of Thrones'))

