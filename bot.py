#!/usr/bin/env python

from elasticbot.slack import SlackBot
from elasticbot.elastic import ElasticClient
from elasticbot.config import Configuration

if __name__ == "__main__":
    config = Configuration(
        token = "",
        check_interval = 2,
        elastic = "localhost:9200",
        bot_id = "U16ER7H40"
    )
    # esClient = ElasticClient()
    # esClient.search(query = "GET /api/pingAlbo 200 3ms")
    SlackBot(config).start()