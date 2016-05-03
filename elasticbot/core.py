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
                if readedData:
                    message = readedData[0]
                    if 'type' in message:
                        print(readedData)
                        messageType = readedData[0]['type']
                        if messageType == 'message':
                            messageText = readedData[0]['text']
                            messageChannel = readedData[0]['channel']
                            print("message '", messageText,"' from channel", messageChannel)
                            slackClient.rtm_send_message(messageChannel, messageText)
                time.sleep(self.config.getCheckInterval())
        else:
            print("Connection Failed, invalid token?")       

class ElasticBotConfig:
    def __init__(self):
        print("loading config")
        
    def setToken(self, token):
         self.token = token
         
    def getToken(self):
         return self.token
         
    def setCheckInterval(self, interval):
        self.interval = interval
         
    def getCheckInterval(self):
        return self.interval
