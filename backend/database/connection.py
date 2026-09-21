import os
import pymysql
from dotenv import load_dotenv

load_dotenv()

DB_CONFIG = {
    "host":        os.getenv("DB_HOST"),
    "database":    os.getenv("DB_NAME"),
    "user":        os.getenv("DB_USER"),
    "password":    os.getenv("DB_PASSWORD"),
    "cursorclass": pymysql.cursors.DictCursor
}


def get_connection():
    return pymysql.connect(**DB_CONFIG)