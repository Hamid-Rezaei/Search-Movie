from main.utils.base_esdao import BaseESDao
from project.configuration.config import Config
from project.configuration.configuration import Configuration


class SearchMovieESDao(BaseESDao):
    def __init__(self, index_name):
        super().__init__()
        self.index_name = index_name

    def search_documents(self, query):
        res = self.client.search(index=self.index_name, query=query)
        return res.get('hits', {}).get('hits')


if __name__ == '__main__':
    Configuration.configure(Config)
    search_movie = SearchMovieESDao('movie')

