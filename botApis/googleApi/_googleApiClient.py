# pip install google-api-python-client
import os
from googleapiclient.discovery import build
from dotenv import load_dotenv


def google_search(search_term, **kwargs):
    load_dotenv()
    api_key = os.environ.get('api_key')
    cse_id = os.environ.get('cse_id')
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    data = [(e['title'], e['link'], e['snippet'])
            for e in res['items']]
    return data
