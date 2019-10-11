from loguru import logger
import requests
from urllib.parse import urljoin
import random

DEFAULT_JOKE = "Mmh, je ne suis pas très inspiré"


class JokeService:
    def __init__(self, base_url: str, end_point: str):
        self.base_url = base_url
        self.end_point = end_point

    def get_joke(self) -> str:
        url = urljoin(self.base_url, self.end_point)
        try:
            parameters = {}
            logger.info("Calling {} for getting parking state".format(url))
            response = requests.get(url, params=parameters)
            if response.status_code >= 400:
                e = Exception(
                    "HTTP Error calling {} => {} : {}".format(url, response.status_code, response.text)
                )
                logger.error(e)
                return DEFAULT_JOKE
            response_json = response.json()
            return self.parse_response(response_json)
        except Exception as e:
            logger.error(e)
            return DEFAULT_JOKE

    @staticmethod
    def parse_response(jokes: list) -> str:
        joke = random.choice(jokes)

        return joke.get("blagues", DEFAULT_JOKE)
