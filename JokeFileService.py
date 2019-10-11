from loguru import logger
import requests
from urllib.parse import urljoin
import random

DEFAULT_JOKE = "Mmh, je ne suis pas très inspiré"
JOKE_FILE = "jokes_normalized.txt"


class JokeFileService:
    def __init__(self):
        with open(JOKE_FILE) as f:
            self.jokes = f.readlines()

    def get_joke(self) -> str:
        joke = random.choice(self.jokes)

        return joke
