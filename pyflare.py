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
        self.rec_id = None
        self.run()
    
    def run(self):
        while True:
            self.loadcfg()
            self.rec_id = self.getrec_id(self.callapi(req='rec_load_all'))
            self.callapi(req='rec_edit')
            sleep(300)
        

    def getip(self):
        ip = requests.get('http://icanhazip.com').text.rstrip('\n')
        return ip
    
    def loadcfg(self):
        '''Opens config file and returns cfg for key passed in'''
        cfg = ConfigParser.ConfigParser()
        cfg.read("/etc/pyflare.conf")
        self.key = cfg.get('account', 'api_key')
        self.email = cfg.get('account', 'email')
        self.zone = cfg.get('dns', 'zone')
        self.record = cfg.get('dns', 'record')
        return self

    def callapi(self, req=None):
        url = 'https://www.cloudflare.com/api_json.html'
        headers = {'content-type' : 'application/json'}
        if req == 'rec_edit':
            post = self.rec_edit()
        elif req == 'rec_load_all':
            post = self.rec_load_all()
        try:
            data = json.dumps(post)
            response = requests.post(url, data=post)
        except Exception as e:
            print 'Could not POST update, Reason: {}'.format(e)
        else:
            print 'Successfully made POST request, Response: {}'.format(response.json())
            return response.json()
    
    def getrec_id(self, raw):
        self.rec_id = [x['rec_id'] for x in raw['response']['recs']['objs'] if x['display_name'] == self.record][0]
        print 'Got rec id {}'.format(self.rec_id)
    
    def rec_edit(self):
        post = {
        'a': 'rec_edit',
        'act': 'rec_edit',
        'tkn': self.key,
        'id': self.rec_id,
        'email': self.email,
        'z': self.zone,
        'type': 'A',
        'name': self.record,
        'content': self.getip(),
        'service_mode': '1',
        'ttl': '1'
        }
        print 'Got POST: {}'.format(post)
        return post
    
    def rec_load_all(self):
        post = {
        'a': 'rec_load_all',
        'act': 'rec_load_all',
        'tkn': self.key,
        'email': self.email,
        'z': self.zone
        }
        print 'Got POST: {}'.format(post)        
        return post


# ------ Unittesting ------ #

class test_PyFlare(unittest.TestCase):

    def test_getip(self):
        self.assertRegexpMatches(PyFlare().getip(), "^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")


if __name__ == '__main__':
    PyFlare()