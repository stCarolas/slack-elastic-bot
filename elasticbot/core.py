#!/usr/bin/env python
import time
from slackclient import SlackClient

class ElasticBot(object):
    def __init__(self, config):
        self.config = config
        print("config ElasticBot")
        
    def start(self):
       print("elasticbot started using token ", self.config.getToken())
       slackClient = SlackClient(self.config.getToken())
       test = True
       if slackClient.rtm_connect():
           while True:
               readedData = slackClient.rtm_read() 
               print(readedData)
               if test:
                   slackClient.rtm_send_message("D152Q9Y83", "fuck you")
                   test = False
               time.sleep(3)
       else:
           print("Connection Failed, invalid token?")       

class ElasticBotConfig:
    def __init__(self):
        print("loading config")
        
    def setToken(self, token):
         self.token = token
         
    def getToken(self):
         return self.token
