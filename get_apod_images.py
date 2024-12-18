import requests
import general_functions as gen_func
import os
import argparse


def get_nasa_apod_images(count, api_key):
    params = {
        'api_key': api_key,
        'count': count
    }
    response = requests.get('https://api.nasa.gov/planetary/apod',
                            params=params)
    response.raise_for_status()
    for number, link in enumerate(response.json(), start=1):
        if link['media_type'] == 'video':
            continue
        extension = gen_func.get_image_extension(link['url'])
        gen_func.download_image(link['url'], os.path.join(
                                'Images', f'nasa_apod_{number}{extension}'))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Downloading NASA APOD images")
    parser.add_argument("count", type=int, nargs="?", default='1')
    args = parser.parse_args()
    get_nasa_apod_images(args.count,
                         gen_func.get_env_variables()['nasa_api_key'])
