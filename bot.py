#!/usr/bin/env python

from elasticbot.slack import ElasticBot
from elasticbot.elastic import ElasticClient
from elasticbot.config import Configuration

if __name__ == "__main__":
    config = Configuration(
        token = "",
        check_interval = 2,
        elastic = "manlogint1:9200",
        bot_id = "U153Y36GN"
    )
    # esClient = ElasticClient()
    # esClient.search(query = "GET /api/pingAlbo 200 3ms")
    ElasticBot(config).start()