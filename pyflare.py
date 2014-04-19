#!/usr/bin/env python

import unittest
import requests


class PyFlare(object):
    
    def __init__(self):
        self.tkn = None
        self.email = None
        self.a = None # API uses this for determining the request type
        self.url = 'https://www.cloudflare.com/api_json.html'
        self.post = {}
    
    def getip(self):
        ip = requests.get('http://icanhazip.com').text.rstrip('\n')
        return ip
    
    def loadcfg(self, cfg=None):
        '''Opens config file and returns cfg for key passed in'''
        cfg = cfg
        pass

    def rec_edit(self):
        post = {
        'a': 'rec_edit',
        'tkn': self.loadcfg(cfg='api_key'),
        'id': '', #dns record id
        'email': self.loadcfg(cfg='email'),
        'z': self.loadcfg(cfg='zone'),
        'type': 'A',
        'name': self.loadcfg(cfg='record_name'),
        'content': self.getip(),
        'service_mode': '1',
        'ttl': '1'
        }
        return post
    
    def rec_load_all(self):
        


# ------ Unittesting ------ #

class test_PyFlare(unittest.TestCase):

    def test_getip(self):
        self.assertEqual(PyFlare().getip(), '71.209.47.192')
        

    def test_getapiendpoint(self):
        pass

if __name__ == '__main__':
    unittest.main()