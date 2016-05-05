#!/usr/bin/env python
from .elastic import ElasticClient

class Configuration:

    def __init__(self, token = "", check_interval = 1, elastic = "localhost:9200", bot_id = ""):
        self.token = token
        self.check_interval = check_interval
        self.elastic = elastic
        self.query_engine = ElasticClient(config = self)
        self.bot_id = bot_id
        print("configuration created")
        
    def get_token(self):
        return self.token
        
    def get_elastic(self):
        return self.elastic
        
    def get_check_interval(self):
        return self.check_interval
        
    def get_query_engine(self):
        return self.query_engine
        
    def get_bot_id(self):
        return self.bot_id