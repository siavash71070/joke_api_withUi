import requests
import random
from abc import ABC, abstractmethod


class Joke(ABC):

    def __init__(self, **kwargs):
        pass

    @abstractmethod
    def get_random(self):
        pass


class A(Joke):
    def __init__(self, **kwargs):
        self.api_token = kwargs.get("api_token")

    def get_random(self):
        try:
            response = requests.get("https://api.api-ninjas.com/v1/jokes",
                                    headers={'X-Api-Key': self.api_token})
            json_data = response.json()[0]["joke"]
        except:
            json_data = "Internet is not active!!!"
        return json_data


class B(Joke):
    def get_random(self):
        try:
            response = requests.get("https://icanhazdadjoke.com/slack")
            json_data = response.json()["attachments"][0]["fallback"]
        except:
            json_data = "Internet is not active!!!"
        return json_data


class C(Joke):

    def get_random(self):
        try:
            response = requests.get("https://api.chucknorris.io/jokes/random")
            json_data = response.json()["value"]

        except:
            json_data = "Internet is not active!!!"
        return json_data
