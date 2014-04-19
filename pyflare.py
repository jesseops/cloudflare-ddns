#!/usr/bin/env python

import unittest
import requests


class PyFlare(object):
    
    def getip(self):
        ip = requests.get('http://icanhazip.com').text.rstrip('\n')
        return ip
    
    def getapiendpoint(self):
        api = 'https://www.cloudflare.com/api_json.html'



# ------ Unittesting ------ #

class test_PyFlare(unittest.TestCase):

    def test_getip(self):
        self.assertEqual(PyFlare().getip(), '71.209.47.192')
        

    def test_getapiendpoint(self):
        pass

if __name__ == '__main__':
    unittest.main()