

class ApiTools(object):
    """
    Provides tools for working with the CloudFlare API
    """

class JsonTemplates(object):
    """
    Provides JSON templates for the CloudFlare API
    Each template returns a JSON formatted request
    """
    # todo: add decorator to format these to json...
    def rec_load_all(self):
        post = {
            'a': 'rec_load_all',
            'act': 'rec_load_all',
            'tkn': self.key,
            'email': self.email,
            'z': self.zone
        }
        return post

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
        return post