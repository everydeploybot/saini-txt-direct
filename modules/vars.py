#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "23163471"))
API_HASH = environ.get("API_HASH", "d0fdee13a4197d27e7d7fc73fdf0954b")
BOT_TOKEN = environ.get("BOT_TOKEN", "8209895268:AAGaugZXFLL2M6Ok93u6VAYqwDz_NWgtfXw")

OWNER = int(environ.get("OWNER", "7863031849"))
CREDIT = environ.get("CREDIT", "HACKER")
cookies_file_path = os.getenv("cookies_file_path", "youtube_cookies.txt")

TOTAL_USER = os.environ.get('TOTAL_USERS', '7863031849').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '7863031849').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))

