import telegram
import os
import random
import argparse
from general_functions import get_env_variables as env_var


def post_image(path, bot_token, chat_id):
    bot = telegram.Bot(token=bot_token)
    if not path:
        for dirpath, dirnames, filenames in os.walk('Images'):
            image_path = os.path.join(dirpath,
                                      random.sample(filenames, 1).pop())
            with open(image_path, 'rb') as image:
                bot.send_photo(photo=image, chat_id=chat_id)
        return
    with open(path, 'rb') as image:
        bot.send_photo(photo=image, chat_id=chat_id)


def post_random_image(bot_token, chat_id):
    bot = telegram.Bot(token=bot_token)
    for dirpath, dirnames, filenames in os.walk('Images'):
        image_path = os.path.join(dirpath,
                                  random.sample(filenames, 1).pop())
        with open(image_path, 'rb') as image:
            bot.send_photo(photo=image, chat_id=chat_id)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Posting image in telegram chanel")
    parser.add_argument("path", type=str, nargs="?", default=None)
    args = parser.parse_args()
    env_vars = env_var()
    if args.path:
        post_image(args.path, env_vars['tg_bot_token'], env_vars['tg_chat_id'])
    else:
        post_random_image(env_vars['tg_bot_token'], env_vars['tg_chat_id'])
