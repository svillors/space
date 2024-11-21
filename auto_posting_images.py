import os
import time
import random
from posting_image import post_image
from dotenv import load_dotenv


def auto_post_images():
    load_dotenv()
    flag = True
    while True:
        if flag:
            for dirpath, dirnames, filenames in os.walk('Images'):
                for file in filenames:
                    post_image(os.path.join(dirpath, file))
                    time.sleep(int(os.getenv('BREAK_OF_POSTING')))
        else:
            paths = []
            for dirpath, dirnames, filenames in os.walk('Images'):
                for file in filenames:
                    paths.append(os.path.join(dirpath, file))
            random.shuffle(paths)
            for path in paths:
                post_image(path)
                time.sleep(int(os.getenv('BREAK_OF_POSTING')))
        flag = False


if __name__ == "__main__":
    auto_post_images()
