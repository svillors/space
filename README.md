# Space Telegram

This project includes scripts for downloading space images and a Telegram bot for posting them

Examples:
```
$ python3 fetch_spacex_images.py
# Downloads images from SpaceX's latest launches or launch of your ID
```
```
$ python3 get_apod_images.py your_number_of_images
# Downloads images from NASA APOD
```
```
$ python3 get_epic_images.py your_number_of_images
# Downloads images from NASA EPIC of Earth
```
```
$ python3 posting_image.py path_to_image
# Posts an image in your Telegram channel
```
```
$ python3 auto_posting_images.py
# Posts images in your Telegram channel with interval
```

### How to install

You should create .env file in root directory and write in it these keys:
- NASA_API_KEY='your_key'

You can get this key in [api.nasa.gov](https://api.nasa.gov/)
- TELEGRAM_BOT_TOKEN='your_token'

To get this token you should create a Telegram bot by using [Botfather](https://telegram.me/BotFather)
- CHAT_ID='@chanel_id'

To get the chat ID, copy the link to your channel in Telegram
- BREAK_OF_POSTING=14400

The time interval in seconds between posting images


Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).