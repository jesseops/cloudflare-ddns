import ConfigParser
import logging
import requests
import json
from time import sleep
from workers import WS


class PyFlare(object):
    """
    Simple python app to auto update dynamic DNS using the Cloudflare API
    """
    
    def __init__(self):
        self.key = None
        self.email = None
        self.a = None   # API uses this for determining the request type
        self.post = {}
        self.rec_id = None
    
    def run(self):
        while True:
            self.setlogging()  # Enable logging
            logging.info('Starting up')
            self.loadcfg()  # Access config file
            self.rec_id = self.getrec_id(self.callapi(req='rec_load_all'))  # Load current record id from cloudflare
            self.callapi(req='rec_edit')  # POST record update to Cloudflare
            logging.info('Sleeping for 5 minutes')
            sleep(300)

    def getip(self):
        """
        Gets external IP address and strips to plain string
        """
        ip = requests.get('http://icanhazip.com').text.rstrip('\n')
        logging.info('Got current IP - {}'.format(ip))
        return ip
    
    def loadcfg(self):
        """
        Opens config file and returns cfg for key passed in
        """
        cfg = ConfigParser.ConfigParser()
        cfg.read("/etc/pyflare.conf")  # Expected location, make sure you have access here!
        self.key = cfg.get('account', 'api_key')
        self.email = cfg.get('account', 'email')
        self.zone = cfg.get('dns', 'zone')
        self.record = cfg.get('dns', 'record')
        return self

    def setlogging(self):
        logging.basicConfig(filename='/var/log/pyflare.log', level=logging.DEBUG)

    def callapi(self, req=None):
        url = 'https://www.cloudflare.com/api_json.html'
        headers = {'content-type': 'application/json'}
        if req == 'rec_edit':
            post = self.rec_edit()
        elif req == 'rec_load_all':
            post = self.rec_load_all()
        try:
            data = json.dumps(post)
            response = requests.post(url, data=post)
        except Exception as e:
            logging.warning('API Call Unsuccessful, Reason: {}'.format(e))
        else:
            logging.info('API Call Successful: {}'.format(req))
            return response.json()
    
    def getrec_id(self, raw):
        self.rec_id = [x['rec_id'] for x in raw['response']['recs']['objs'] if x['display_name'] == self.record]
        logging.info('Got Record ID {}'.format(self.rec_id))
        return self.rec_id
    
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
        logging.debug('Built rec_edit POST: {}'.format(post))
        return post
    
    def rec_load_all(self):
        post = {
            'a': 'rec_load_all',
            'act': 'rec_load_all',
            'tkn': self.key,
            'email': self.email,
            'z': self.zone
        }
        logging.debug('Built rec_load_all POST: {}'.format(post))
        return post
