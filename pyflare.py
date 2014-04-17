#!/usr/bin/env python

import unittest
import requests


class PyFlare(object):
    
    def getip(self):
        ip = requests.get('http://icanhazip.com').text.rstrip('\n')
        return ip
    
    def validpost(self):
        pass



# ------ Unittesting ------ #

class test_PyFlare(unittest.TestCase):

    def test_getip(self):
        self.assertEqual(PyFlare().getip(), '71.209.47.192')
        

    def test_validpost(self):
        pass

if __name__ == '__main__':
    unittest.main()