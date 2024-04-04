from main.utils.base_esdao import BaseESDao


class SearchMovieESDao(BaseESDao):
    def __init__(self, index_name):
        super().__init__()
        self.index_name = index_name

    def search_documents(self, body):
        res = self.client.search(index=self.index_name, body=body)
        return res.get('hits', {}).get('hits')
