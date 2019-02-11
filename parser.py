from bs4 import BeautifulSoup
import datetime


def date_from_string(date_str):
    date = date_str.replace('th', '')
    return datetime.datetime.strptime(date, '%B %d')


def parse(content):
    soup = BeautifulSoup(content, 'html.parser')
    table_header = soup.select("div.table-header")[0]
    data = {
        'name': table_header.find('a').text,
        'date': date_from_string(table_header.find('span').text),
        'fighters_names': [el.text for el in soup.select("div.table-inner-wrapper > div.table-scroller > table > tbody > tr > th > a > span")]
    }
    return data
