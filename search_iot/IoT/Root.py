from typing import List
from .IoT import Iot


class Root:
    iots: List[Iot]

    def __init__(self, iots: List[Iot]):
        self.iots = iots

    def search_words(self, words: List[str]):
        for iot in self.iots:

