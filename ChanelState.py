from enum import Enum


class ChannelState(Enum):
    BLOCKED = "X"
    BUSY = "1"
    EMPTY = "0"


class Channel:

    def __init__(self, state):
        self.state = state

    @property
    def state(self):
        return self._state.value

    @state.setter
    def state(self, stat):
        self._state = stat