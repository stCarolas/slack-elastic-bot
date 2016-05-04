#!/usr/bin/env python

from elasticbot.slack import ElasticBotConfig
from elasticbot.slack import ElasticBot
from elasticbot.elastic import ElasticClient

if __name__ == "__main__":
    config = ElasticBotConfig()
    config.setToken("")
    config.setCheckInterval(2)
    esClient = ElasticClient()
    esClient.search("GET /api/pingAlbo 200 3ms")
    bot = ElasticBot(config)
    bot.start()