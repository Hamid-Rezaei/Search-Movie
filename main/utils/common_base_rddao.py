from collections import namedtuple

import redis

from main.utils.singleton import Singleton
from project.configuration.configuration import Configuration

RDKey = namedtuple('RDKey', ['key', 'ttl'])


class CommonsBaseRDDao(metaclass=Singleton):
    def __init__(self):
        password = Configuration.config().REDIS_PASSWORD

        kwargs = {"host": Configuration.config().REDIS_HOST,
                  "port": Configuration.config().REDIS_PORT,
                  "db": Configuration.config().REDIS_DB,
                  "decode_responses": Configuration.config().REDIS_DECODE_RESPONSES}

        if Configuration.config().REDIS_PASSWORD:
            kwargs["password"] = Configuration.config().REDIS_PASSWORD

        self.client = redis.Redis(**kwargs)

        if redis_slave_host := Configuration.config().REDIS_SLAVE_HOST is not None:
            kwargs["host"] = redis_slave_host
            self.read_only_client = redis.Redis(**kwargs)
