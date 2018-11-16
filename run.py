from urllib.request import urlopen
from xml.etree import ElementTree as ET


def naviny_rss(event, context):
    return _get_rss_by_author(event['query']['author']).decode()


def _get_rss_by_author(author: str):
    root = ET.fromstring(urlopen('https://naviny.by/rss/articles.xml').read())
    channel = root.find('channel')
    for item in channel.findall('item'):
        if author != item.find('{http://purl.org/dc/elements/1.1/}creator').text:
            channel.remove(item)

    return ET.tostring(root)


