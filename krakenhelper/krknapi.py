
import requests
import json

fn_url = 'https://krknapi.com'
headers = {'content-type': 'application/json'}
cookies = {'actionId': 'action_ok'}

class Kraken_data:
    # Class to interact with krknapi (get, post data)

    def __init__(self, record_type, record_id):
        self.record_type = record_type
        self.record_id = record_id
        self.record = None


    def get(self):

        params = {
            'record_type': self.record_type,
            'record_id': self.record_id
        }

        r = requests.get(fn_url, params=params, cookies=cookies)

        self.record = r.json()

        return self.record


    def post(self, record = None):

        if record:
            self.record = record

        data = json.dumps(record, default=str)

        r = requests.post(fn_url, headers = headers, data=data)

        if r.status_code < 250:
            return 'ok'
        else:
            return 'error'
