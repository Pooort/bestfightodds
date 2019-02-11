import requests

headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36'}


def get_content():
    response = requests.get('https://www.bestfightodds.com/events/ufc-231-holloway-vs-ortega-1584', headers=headers)
    return response.text
