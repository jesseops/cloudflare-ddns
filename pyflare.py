#!/usr/bin/env python

import ConfigParser
import unittest
import requests
import json
from time import sleep


class PyFlare(object):
    """
    Simple python app to auto update dynamic DNS using the Cloudflare API
    """
    
    def __init__(self):
        self.key = None
        self.email = None
        self.a = None # API uses this for determining the request type
        self.post = {}
    
    def run(self):
        pass
    
    def getip(self):
        ip = requests.get('http://icanhazip.com').text.rstrip('\n')
        return ip
    
    def loadcfg(self):
        '''Opens config file and returns cfg for key passed in'''
        config = ConfigParser.ConfigParser()
        config.read("./pyflare.conf")
        self.key = config.get('account', 'api_key')
        self.email = config.get('account', 'email')
        self.zone = config.get('dns', 'zone')
        self.record = config.get('dns', 'record')
        return self

    def callapi(self, post):
        url = 'https://www.cloudflare.com/api_json.html'
        headers = {'content-type' : 'application/json'}
        try:
            response = requests.post(url, json.dumps(post), headers=headers)
        except Exception as e:
            print 'Could not POST update, Reason: {}'.format(e)
        else:
            self.parsejson(response)
    
    def parsejson(self, raw):
        
        return flareid
    
    def rec_edit(self):
        post = {
        'a': 'rec_edit',
        'tkn': self.key,
        'id': '',
        'email': self.email,
        'z': self.zone,
        'type': 'A',
        'name': self.record,
        'content': self.getip(),
        'service_mode': '1',
        'ttl': '1'
        }
        return post
    
    def rec_load_all(self):
        post = {
        'a': 'rec_load_all',
        'tkn': self.key,
        'email': self.email,
        'z': self.zone
        }
        return post


# ------ Unittesting ------ #

class test_PyFlare(unittest.TestCase):

    def test_getip(self):
        self.assertRegexpMatches(PyFlare().getip(), "^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")


if __name__ == '__main__':
    unittest.main()