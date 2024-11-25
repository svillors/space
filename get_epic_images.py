import requests
import datetime
import os
import argparse
import general_functions as gen_func


def get_nasa_epic_images(count, api_key):
    params = {'api_key': api_key}
    response = requests.get('https://api.nasa.gov/EPIC/api/natural',
                            params=params)
    response.raise_for_status()
    for number, img_data in enumerate(response.json(), start=1):
        if number > count:
            break
        date = datetime.datetime.fromisoformat(
                                        img_data['date']).strftime('%Y/%m/%d')
        image_id = img_data['image']
        link = f'https://api.nasa.gov/EPIC/archive/natural/{date}/png/{image_id}.png'
        params = {'api_key': api_key}
        gen_func.download_image(link, os.path.join('Images',
                                                   f'nasa_epic_{number}.png'), params)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Downloading NASA EPIC images")
    parser.add_argument("count", type=int, nargs="?", default='1')
    args = parser.parse_args()
    get_nasa_epic_images(args.count,
                         gen_func.get_env_variables()['nasa_api_key'])
