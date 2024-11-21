import os
import urllib.parse
import requests


def get_image_extension(url):
    return os.path.splitext(urllib.parse.unquote(url))[1]


def image_downloading(url, path):
    response = requests.get(url)
    response.raise_for_status()
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.mkdir(directory)
    with open(path, 'wb') as file:
        file.write(response.content)
