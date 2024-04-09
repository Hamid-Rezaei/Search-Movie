from main.utils.singleton import Singleton


class Documents(metaclass=Singleton):

    def __init__(self):
        self.movie_mapping = {
            "mappings": {
                "_meta": {
                    "created_by": "file-data-visualizer"
                },
                "properties": {
                    "Certificate": {
                        "type": "keyword"
                    },
                    "Director": {
                        "type": "keyword"
                    },
                    "Genre": {
                        "type": "keyword"
                    },
                    "Gross": {
                        "type": "keyword"
                    },
                    "IMDB_Rating": {
                        "type": "double"
                    },
                    "Meta_score": {
                        "type": "keyword"
                    },
                    "No_of_Votes": {
                        "type": "long"
                    },
                    "Overview": {
                        "type": "text"
                    },
                    "Poster_Link": {
                        "type": "keyword"
                    },
                    "Released_Year": {
                        "type": "long"
                    },
                    "Runtime": {
                        "type": "keyword"
                    },
                    "Series_Title": {
                        "type": "text"
                    },
                    "Star1": {
                        "type": "keyword"
                    },
                    "Star2": {
                        "type": "keyword"
                    },
                    "Star3": {
                        "type": "keyword"
                    },
                    "Star4": {
                        "type": "keyword"
                    },
                    "index": {
                        "properties": {
                            "_index": {
                                "type": "text",
                                "fields": {
                                    "keyword": {
                                        "type": "keyword",
                                        "ignore_above": 256
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }

    def get_movie_mapping(self):
        return self.movie_mapping
