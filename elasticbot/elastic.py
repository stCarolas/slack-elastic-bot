#!/usr/bin/env python

from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
from datetime import datetime
from datetime import date
from datetime import timedelta

class ElasticClient:
    def __init__(self, url):
        self.esClient = Elasticsearch(url)
        print("init elastic client")

    def do(self, query):
        print("make search for query ", query)
        startDate = date.today() - timedelta(days = 7)
        request = Search(using = self.esClient).query("match", message = query)
        request = request.query('range', ** {'@timestamp': {'to': 'now','from': datetime(startDate.year, startDate.month, startDate.day , 0, 0, 0)}})
        result = request.execute()
        print("result: ", result, "\n")
        response = "Result: "
        for hit in result:
            response = response + "\n" + hit['@timestamp'] + " :: " +  hit['message']
        return response