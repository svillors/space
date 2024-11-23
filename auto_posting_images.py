import os
import time
import random
from posting_image import post_image
from general_functions import get_env_variables as env_var


def auto_post_images(interval, bot_token, chat_id):
    first_iteration = True
    while True:
        if first_iteration:
            for dirpath, dirnames, filenames in os.walk('Images'):
                for file in filenames:
                    post_image(os.path.join(dirpath, file), bot_token, chat_id)
                    time.sleep(interval)
            first_iteration = False
        else:
            paths = []
            for dirpath, dirnames, filenames in os.walk('Images'):
                for file in filenames:
                    paths.append(os.path.join(dirpath, file), bot_token,
                                 chat_id)
            random.shuffle(paths)
            for path in paths:
                post_image(path)
                time.sleep(interval)


if __name__ == "__main__":
    auto_post_images(env_var()['break_of_posting'],
                     env_var()['tg_bot_token'],
                     env_var()['tg_chat_id'])
