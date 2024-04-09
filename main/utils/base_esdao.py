from elasticsearch.client import Elasticsearch

from project.configuration.configuration import Configuration


class ABCBaseESDao:
    def __init__(self):
        kwargs = self._get_init_kwargs()
        self.client = Elasticsearch(**kwargs)

        self.client.search()  # just for test

    def _orgnize_kwargs(self, kwargs, api_key, hosts, http_auth_password, http_auth_user_name, https_verify_certs):
        if hosts is not None:
            kwargs["hosts"] = hosts
        if api_key is not None:
            kwargs["api_key"] = api_key
        if https_verify_certs is not None:
            kwargs["verify_certs"] = https_verify_certs
        if kwargs.get("http_compress") is not None:
            kwargs["http_compress"] = True
        if kwargs.get("timeout") is not None:
            kwargs["timeout"] = 120
        if http_auth_user_name is not None:
            kwargs["http_auth"] = (http_auth_user_name, http_auth_password)

        return kwargs

    def search(self, query: dict, index_name: str):
        return self.client.search(body=query, index=index_name)

    def index(self, doc_id: str, doc: dict, index_name: str):
        self.client.index(index=index_name, document=doc, id=doc_id)

    def create(self, doc_id: str, doc: dict, index_name: str):
        self.client.create(index=index_name, id=doc_id, document=doc)

    def delete(self, doc_id: str, index_name: str):
        self.client.delete(index=index_name, id=doc_id)

    def update(self, doc_id: str, doc: dict, index_name: str):
        self.client.update(index=index_name, id=doc_id, doc=doc)

    def update_by_query(self, query: dict, index_name: str):
        return self.client.update_by_query(index=index_name, body=query)

    def get_by_id(self, doc_id: str, index_name: str):
        return self.client.get(index=index_name, id=doc_id)

    def exists(self, doc_id: str, index_name: str):
        return self.client.exists(id=doc_id, index=index_name)


class BaseESDao(ABCBaseESDao):

    def _get_init_kwargs(self):
        kwargs = Configuration.config().ELASTIC_SEARCH_KWARG
        api_key = Configuration.config().ELASTIC_SEARCH_API_KEY
        http_auth_password = Configuration.config().ELASTIC_SEARCH_HTTP_AUTH_PASSWORD
        http_auth_user_name = Configuration.config().ELASTIC_SEARCH_HTTP_AUTH_USER_NAME
        hosts = Configuration.config().ELASTIC_SEARCH_HOSTS
        https_verify_certs = Configuration.config().ELASTIC_SEARCH_HTTPS_VERIFY_CERTS

        return self._orgnize_kwargs(
            kwargs,
            api_key,
            hosts,
            http_auth_password,
            http_auth_user_name,
            https_verify_certs
        )
