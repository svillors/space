import general_functions as gen_func
import requests
import argparse
import os


def fetch_spacex_images(id):
    response = requests.get(f'https://api.spacexdata.com/v5/launches/{id}')
    response.raise_for_status()
    image_links = response.json()['links']['flickr']['original']
    for number, link in enumerate(image_links, start=1):
        extension = gen_func.get_image_extension(link)
        gen_func.download_image(link, os.path.join(
                                    'Images', f'spacex_{number}{extension}'))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Downloading spaceX images")
    parser.add_argument("id", type=str, nargs="?", default='latest')
    args = parser.parse_args()
    fetch_spacex_images(args.id)
