from enum import Enum


class SourceState(Enum):
    BLOCKED = "0"
    FIRST_TIC = "2"
    LAST_TIC = "1"


class Source:

    def __init__(self, state):
        self.state = state

    @property
    def state(self):
        return self._state.value

    @state.setter
    def state(self, stat):
        self._state = stat

