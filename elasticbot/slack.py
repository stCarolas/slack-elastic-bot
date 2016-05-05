#!/usr/bin/env python
import time
from slackclient import SlackClient

class ElasticBot:
    def __init__(self, config):
        self.config = config
        self.last_ts = "000000000000000000000000"

    def start(self):
        self.slackClient = SlackClient(self.config.get_token())
        if self.slackClient.rtm_connect():
            print("connected")
            while True:
                readedData = self.slackClient.rtm_read()
                if readedData:
                    self.parseMessage(readedData[0])
                time.sleep(self.config.get_check_interval())
        else:
            print("connection failed")

    def parseMessage(self, message):
        if 'type' in message:
            messageType = message['type']
            if messageType == 'message':
                messageText = message['text']
                messageChannel = message['channel']
                messageTs = message['ts']
                if message['user'] != self.config.get_bot_id():
                    if self.last_ts < messageTs:
                        print("message '", messageText,"' from channel", messageChannel)
                        self.config.get_query_engine().do(query = messageText)
                        self.slackClient.rtm_send_message(messageChannel, messageText)
                        self.last_ts = messageTs