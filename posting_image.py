import telegram
import os
import random
import argparse
from dotenv import load_dotenv


def post_image(path):
    load_dotenv()
    bot = telegram.Bot(token=os.getenv("TELEGRAM_BOT_TOKEN"))
    if not path:
        for dirpath, dirnames, filenames in os.walk('Images'):
            image_path = os.path.join(dirpath,
                                      random.sample(filenames, 1).pop())
            post_image(image_path)
        return
    with open(path, 'rb') as image:
        bot.send_photo(photo=image, chat_id=os.getenv('CHAT_ID'))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Posting image in telegram chanel")
    parser.add_argument("path", type=str, nargs="?", default=None)
    args = parser.parse_args()
    post_image(args.path)
