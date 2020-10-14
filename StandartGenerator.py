import random


class StandartGenerator:

    def __init__(self):
        self.random = random

    @property
    def next(self):
        return self.random.random()