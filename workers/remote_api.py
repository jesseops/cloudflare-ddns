import requests
import logging
import threading


class CFApi(threading.Thread):
    def __init__(self, pyflare):
        self.pf = pyflare
        threading.Thread.__init__(self)

