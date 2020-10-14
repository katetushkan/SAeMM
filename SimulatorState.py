import typing

from ChanelState import Channel
from SourceState import Source


class SimulatorState:

    def __init__(self, source: Source, channel1: Channel, queue: int,  channel2: Channel):
        self.source = source
        self.channel1 = channel1
        self.channel2 = channel2
        self.queue = queue


