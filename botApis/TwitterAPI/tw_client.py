"""

    Jorge E. Campos II
    Project: DM twitter integration
    Course: Client Server Computing
    Date 12/2/2021

    blk_client.py

"""

import json
import requests
import requests_oauthlib


class TwitterDMClient:
    def __init__(self,
                 consumer_key,
                 consumer_secret,
                 access_token,
                 access_secret):

        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_secret = access_secret

    def verify_credentials(self, auth_obj):
        url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
        response = requests.get(url, auth=auth_obj)
        return response.status_code == 200

    def init_auth(self):
        auth_obj = requests_oauthlib.OAuth1(self.consumer_key,
                                            self.consumer_secret,
                                            self.access_token,
                                            self.access_secret)

        if self.verify_credentials(auth_obj):
            self.auth_obj = auth_obj
            return auth_obj
        else:
            raise Exception('verify your API keys')

    def list_dms(self):
        url = 'https://api.twitter.com/1.1/direct_messages/events/list.json'

        response = requests.get(url, auth=self.auth_obj)
        response.raise_for_status()
        r_json = json.loads(response.text)
        messages = [(e['id'], e['message_create']['message_data']['text'])
                    for e in r_json['events']]
        return messages

    def get_followers(self):
        url = 'https://api.twitter.com/1.1/followers/list.json'
        response = requests.get(url=url, auth=self.auth_obj)
        response.raise_for_status()
        r_json = json.loads(response.text)
        return [{'screen_name': r['screen_name'],
                 'name': r['name'],
                 'id': r['id']}
                for r in r_json['users']]

    def send_dm(self, id, msg):
        url = 'https://api.twitter.com/1.1/direct_messages/events/new.json'
        payload = {"event":
                       {"type": "message_create",
                        "message_create":
                            {"target": {"recipient_id": id},
                             "message_data": {"text": msg}
                             }
                        }
                   }

        response = requests.post(url, data=json.dumps(payload), auth=self.auth_obj)
        response.raise_for_status()
        return json.loads(response.text)

    def get_stream(self):
        url = 'https://api.twitter.com/1.1/tweets/status'
        response = requests.get(url=url, auth=self.auth_obj)
        print(response)
