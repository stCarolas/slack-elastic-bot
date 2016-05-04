#!/usr/bin/env python

from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search

class ElasticClient:
	def __init__(self):
		self.esClient = Elasticsearch(['manlogint1:9200'])
		print("init elasticsearch client:", self.esClient.info())

	def search(self, query):
		request = Search(using=self.esClient).query("match", message=query)
		response = request.execute()
		print("response: ", response, "\n\n\n\n")
		print("request: ", request, "\n\n\n\n")
		for hit in request:
			print("hit: ", hit, "\n\n\n\n")

