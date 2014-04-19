#!/usr/bin/env python

import unittest
import requests
import json
from time import sleep


class PyFlare(object):
    """
    Simple python app to auto update dynamic DNS using the Cloudflare API
    """
    
    def __init__(self):
        self.tkn = None
        self.email = None
        self.a = None # API uses this for determining the request type
        self.post = {}
    
    def getip(self):
        ip = requests.get('http://icanhazip.com').text.rstrip('\n')
        return ip
    
    def loadcfg(self, cfg=None):
        '''Opens config file and returns cfg for key passed in'''
        cfg = cfg
        self.tkn = 'api_key'
        self.email = 'email'
        self.zone = 'zone'
        self.record = 'record'
        return cfg_item

    def callapi(self, post):
        url = 'https://www.cloudflare.com/api_json.html'
        try:
            requests.post(url, json.dumps(post))
        except Exception as e:
            print 'Could not POST update, Reason: {}'.format(e)
            sleep(5)
            requests.post(url, json.dumps(post))
        
    
    def rec_edit(self):
        post = {
        'a': 'rec_edit',
        'tkn': self.tkn,
        'id': '', #dns record id
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
        'tkn': self.tkn,
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