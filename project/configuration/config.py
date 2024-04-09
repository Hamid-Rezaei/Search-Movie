class Config:
    # Postgres Configs
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int = 5432

    # Redis Config
    REDIS_HOST: str = None
    REDIS_SLAVE_HOST: str = None
    REDIS_PORT: int = 6379
    REDIS_DB: int = 0
    REDIS_PASSWORD: str = None
    REDIS_USERNAME: str = None
    REDIS_DECODE_RESPONSES: bool = True

    # Elastic Config
    ELASTIC_SEARCH_KWARG: dict = {}
    ELASTIC_SEARCH_API_KEY: str = None
    ELASTIC_SEARCH_HTTP_AUTH_PASSWORD: str = None
    ELASTIC_SEARCH_HTTP_AUTH_USER_NAME: str = None
    ELASTIC_SEARCH_HOSTS = ['http://localhost:9200/']
    ELASTIC_SEARCH_HTTPS_VERIFY_CERTS: str = None
    ELASTIC_SEARCH_INDEX_NAME: str = 'movies'
