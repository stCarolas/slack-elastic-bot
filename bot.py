#!/usr/bin/env python

from elasticbot.core import ElasticBotConfig
from elasticbot.core import ElasticBot

if __name__ == "__main__":
    config = ElasticBotConfig();
    config.setToken("xoxb-39134108566-fm7WHjqnT282WZH9JbpLaTr9")
    config.setCheckInterval(2)
    bot = ElasticBot(config)
    bot.start()