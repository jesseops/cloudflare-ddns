import sys
import logging
from time import sleep
from workers import *
from tools import SVC, PyFlareObj
from time import sleep


class PyFlare(object):
    """
    Python Application to manage CloudFlare DNS
    """
    def __init__(self):
        self.set_logging()
        self.ws = None
        self.svc = SVC()
        PyFlareObj.svc = self.svc
        self.start_workers()

    def run(self):
        """
        Main loop, easily canceled
        :return: None
        """
        try:
            logging.info("Main Thread Stable")
            while not self.svc.shutdown:
                logging.info("loop")
                try:
                    sleep(10)
                except KeyboardInterrupt:
                    self.cleanup()
            logging.info("Shutting Down")
            self.cleanup()
        except Exception as e:
            logging.critical("Error in Main Loop: {}".format(e))
        finally:
            exit()

    def cleanup(self):
        """
        Cleanup threads, shutdown
        :return: None
        """
        logging.info("Cleanup Called, Exiting")
        self.svc.shutdown = True
        self.ws.join(timeout=10)

    def start_workers(self):
        """
        Start the workers
        :return: None
        """
        self.ws = WS(self)
        self.ws.setDaemon(True)
        self.ws.start()

    def set_logging(self):
        logging.basicConfig(format='[PyFlare] - %(asctime)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)
        logging.StreamHandler(sys.stdout)