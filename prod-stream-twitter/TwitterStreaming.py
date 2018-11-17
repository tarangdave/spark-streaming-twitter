import sys

import json
import socket

import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

class TweetsListener(StreamListener):

    def __init__(self, socket):
        print "Tweet Listener Initialized"
        self.client_socket = socket

    def on_data(self, data):
        try:
            jsonMessage = json.loads(data)
            message = jsonMessage['text'].encode('utf-8')
            print message
            self.client_socket.send(message)
        except BaseException as e:
            print "Error on_data: {0}".format(e)
        return True

    def on_error(self, status):
        print status
        return True

def connect_to_twitter(connection):
    api_key = ""
    api_secret = ""

    access_token = ""
    access_secret = ""

    auth = OAuthHandler(api_key, api_secret)
    auth.set_access_token(access_token, access_secret)

    twitter_stream = Stream(auth, TweetsListener(connection))
    twitter_stream.filter(track=['#'])

if __name__ == "__main__":
    s = socket.socket()
    host = "localhost"
    port = 7777
    s.bind((host, port))

    print "Listening on port: {0}".format(port)
    
    s.listen(5)

    connection, client_address = s.accept()

    print "Received request from: {0}".format(client_address)

    connect_to_twitter(connection)