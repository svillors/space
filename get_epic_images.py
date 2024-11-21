import requests
import datetime
import os
import argparse
from general_functions import image_downloading
from dotenv import load_dotenv


def get_nasa_epic_images(count):
    load_dotenv()
    params = {'api_key': os.getenv("NASA_API_KEY")}
    response = requests.get('https://api.nasa.gov/EPIC/api/natural',
                            params=params)
    for number, img_data in enumerate(response.json(), start=1):
        if number > count:
            break
        date = datetime.datetime.fromisoformat(
                                        img_data['date']).strftime('%Y/%m/%d')
        image_id = img_data['image']
        link = f'https://api.nasa.gov/EPIC/archive/natural/{date}/png/{image_id}.png?api_key=nloxLcoGwLThDJF7F3fbCj1Yg04Ig924M1CtYm3d'
        image_downloading(link, os.path.join('Images',
                                             f'nasa_epic_{number}.png'))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Downloading NASA EPIC images")
    parser.add_argument("count", type=int, nargs="?", default='1')
    args = parser.parse_args()
    get_nasa_epic_images(args.count)
