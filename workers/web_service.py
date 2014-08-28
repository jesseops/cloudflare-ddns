from bottle import route, run, response, abort
import threading
import logging


class WS(threading.Thread):
    def __init__(self, pyflare):
        self.pf = pyflare
        threading.Thread.__init__(self)

    def run(self):
        while not self.pf.shutdown:
            logging.info("Starting PyFlare WS")
            self.service()

    def service(self):
        @route('/')
        def index(self):
            response.content_type = 'application/json'
            return "PyFlare Web Service"

        while True:
            try:
                run(host='0.0.0.0', port=8080, quiet=True)
            except Exception:
                logging.critical("exception in webservice", exc_info=1)