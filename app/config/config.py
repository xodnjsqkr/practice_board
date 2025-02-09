import os
from dotenv import load_dotenv

load_dotenv()  # .env 파일 로드

class Config:
    DB_HOST=os.getenv("MYSQL_HOST")
    DB_PORT=os.getenv("DB_PORT")
    DB_NAME=os.getenv("DB_NAME")
    DB_USER=os.getenv("DB_USER")
    DB_PASSWORD=os.getenv("DB_PASSWORD")