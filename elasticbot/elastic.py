#!/usr/bin/env python

from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
from datetime import datetime

class ElasticClient:
    def __init__(self, config):
        print("init elastic client")

    def do(self, query):
        print("make magic on query ", query)

    # def search(self, query):
		# result = Search(using=self.esClient).query("match", message=query).query('range', ** {'@timestamp': {'to': 'now', 'from': datetime(2016, 4, 20 , 0, 0, 0)}}).execute()
		# print("result: ", result, "\n")
		# for hit in result:
			# print("hit: ", hit, "\n")
			# print("hit message: ", hit['message'], "\n")
			# print("hit timestamp: ", hit['@timestamp'], "\n")


			# s.filter('range', ** {'@timestamp': {'to': 'now'}})
			# s.filter('range', publish_from={'lte': 'now/h'})