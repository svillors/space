import os
import time
import random
from posting_image import post_image
from general_functions import get_env_variables as env_var


def auto_post_images(interval, bot_token, chat_id):
    first_iteration = True
    while True:
        for dirpath, dirnames, filenames in os.walk('Images'):
            for file in filenames:
                if first_iteration:
                    post_image(os.path.join(dirpath, file), bot_token, chat_id)
                    time.sleep(interval)
                else:
                    paths = []
                    paths.append(os.path.join(dirpath, file))
                    random.shuffle(paths)
                    for path in paths:
                        post_image(path, bot_token, chat_id)
                        time.sleep(interval)
        first_iteration = False


if __name__ == "__main__":
    env_vars = env_var()
    auto_post_images(env_vars['break_of_posting'],
                     env_vars['tg_bot_token'],
                     env_vars['tg_chat_id'])
