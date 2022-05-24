import os
from dotenv import load_dotenv

load_dotenv()


class Config(object):
    TOKEN:str = str(os.getenv("TOKEN"))


