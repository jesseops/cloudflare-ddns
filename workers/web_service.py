from bottle import route, run, response, abort
import threading
import logging


class WS(threading.Thread):
    def __init__(self, pyflare):
        self.pf = pyflare
        threading.Thread.__init__(self)

    def run(self):
        while not self.pf.svc.shutdown:
            logging.info("Starting PyFlare WS")
            self.service()

    def service(self):

        @route('/')
        def index():
            response.content_type = 'application/json'
            return "PyFlare Web Service"

        @route('/shutdown')
        def shutdown():
            self.pf.svc.shutdown = True
            response.content_type = 'application/json'
            return "Shutting Down"

        @route('/404')
        def notfound():
            return abort(code=404, text='Just testing.')

        while True:
            try:
                run(host='0.0.0.0', port=8080, quiet=True)
            except Exception as e:
                logging.critical("Uncaught WS Exception: {}".format(e), exc_info=1)