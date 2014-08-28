import unittest
from pyflareOLD import PyFlare


class test_PyFlare(unittest.TestCase):

    def test_getip(self):
        self.assertRegexpMatches(PyFlare().getip(), "^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")