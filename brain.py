import requests
from pandas.io.json import json_normalize

def make_request(url, params=None, headers=None):
    try:
        r = requests.get(
            url,
            params=params,
            headers=headers,
        )
        r.raise_for_status()
    except:
        exit(r.status_code)
    
    return r.json()


def get_pronounce(data):
    
    df = json_normalize(data, record_path=[
            'results', 'lexicalEntries',
            'pronunciations'])

    return df['phoneticSpelling'][0] 


def get_examples(data):

    df = json_normalize(data, record_path=[
            'exact_matches', 'translations',
            'examples'])
    
    return df
