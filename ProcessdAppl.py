class Process:

    def __init__(self):
        self.processed = 0

    @property
    def processed(self):
        return self._processed

    @processed.setter
    def processed(self, value):
        self._processed = value