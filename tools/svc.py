import logging


class PyFlareObj(object):
    """
    Common obj to aid in communication between workers
    """
    svc = None


class SVC(object):
    """
    SVC object, where the magic happens
    """
    def __init__(self):
        self.shutdown = False
        self.cfg = None