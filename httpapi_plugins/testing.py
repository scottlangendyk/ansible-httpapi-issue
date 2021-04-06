from ansible.plugins.httpapi import HttpApiBase

class HttpApi(HttpApiBase):
    def __init__(self, connection):
        super(HttpApi, self).__init__(connection)

    def send_request(self, data, **message_kwargs):
        response, response_content = self.connection.send('/', '')
        return str(response_content.read())