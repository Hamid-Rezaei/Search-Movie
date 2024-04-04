from main.dal.elsdao.search_movie_elsdao import SearchMovieESDao
from main.dal.rddao.search_movie_rddao import SearchMovieRDDao
from main.utils.singleton import Singleton


class SearchMovieLogic(metaclass=Singleton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.search_movie_rddao = SearchMovieRDDao()
        self.search_movie_esdao = SearchMovieESDao()

    def _search_movie_in_elasticsearch(self):
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

    def search_movie(self, email, audio):
        result = self.search_movie_rddao.get_cached_search_result()

        if not result:
            result = self.search_movie_esdao()
            if result:
                self.search_movie_rddao.cache_search_result()
            else:
                ...  # TODO: call api

        result = self.search_movie_rddao.get_cached_search_result()
        movie_info = None

        return movie_info
