import requests

from main.dal.elsdao.search_movie_elsdao import SearchMovieESDao
from main.dal.rddao.search_movie_rddao import SearchMovieRDDao
from main.utils.singleton import Singleton


class SearchMovieLogic(metaclass=Singleton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.search_movie_rddao = SearchMovieRDDao()
        self.search_movie_esdao = SearchMovieESDao('movie')

    def _search_movie_in_elasticsearch(self, query):
        ...
        # search_body = {
        #     "query": {
        #         "parent_id": {
        #             "type": "comment",
        #             "id": post_id
        #         }
        #     },
        #     "sort": [
        #         {
        #             "comment.created_at": {
        #                 "order": "desc"
        #             }
        #         }
        #     ]
        # }
        # res = []
        # response = self.feed_base_es_dao.search_documents(body=search_body)
        # for hit in response:
        #     data = hit['_source'].get('comment')
        #     comment_id = hit.get('_id')
        #     data['id'] = comment_id
        #     user = SocialUtils.get_user_object(user_id=data.get('author_id'))
        #     data['nickname'] = user.userprofileinfo.nickname
        #     avatar = user.userprofileinfo.avatar
        #     data['avatar_url'] = avatar.url if avatar else None
        #     res.append(data)
        # return res
        #

    def _search_movie_in_rapid_api(self, query):


        url = "https://imdb-movies-web-series-etc-search.p.rapidapi.com/thegodfather.json"

        headers = {
            "X-RapidAPI-Key": "a936da7104msh4f5d3eb7358a19cp14b04bjsnb3f9dd254e78",
            "X-RapidAPI-Host": "imdb-movies-web-series-etc-search.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers)

        print(response.json())
        return response.json()

    def search_movie(self, query):
        result = self.search_movie_rddao.get_cached_search_result()

        if not result:
            result = self._search_movie_in_elasticsearch()
            if result:
                self.search_movie_rddao.cache_search_result()
            else:
                # call api
                result = self._search_movie_in_rapid_api(query)
                if result:
                    self.search_movie_rddao.cache_search_result()
                else:
                    raise Exception('Movie not found')

        result = self.search_movie_rddao.get_cached_search_result()
        movie_info = None

        return movie_info
