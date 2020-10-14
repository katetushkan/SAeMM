from ChanelState import Channel, ChannelState
from SimulatorState import SimulatorState
from SourceState import Source, SourceState


class SimulationStatistic:

    SimulationStates = {

        #
        # SimulatorState(Source(SourceState.FIRST_TIC),
        #                Channel(ChannelState.EMPTY),
        #                0,
        #                Channel(ChannelState.EMPTY))
        '2000': 0,

        # 1000
        # SimulatorState(Source(SourceState.LAST_TIC),
        #                Channel(ChannelState.EMPTY),
        #                0,
        #                Channel(ChannelState.EMPTY)): 0,
        '1000': 0,

        # 2100
        # SimulatorState(Source(SourceState.FIRST_TIC),
        #                Channel(ChannelState.BUSY),
        #                0,
        #                Channel(ChannelState.EMPTY)): 0,
        '2100': 0,

        # 1001
        # SimulatorState(Source(SourceState.LAST_TIC),
        #                Channel(ChannelState.EMPTY),
        #                0,
        #                Channel(ChannelState.BUSY)): 0,
        '1001': 0,

        # 2101
        # SimulatorState(Source(SourceState.FIRST_TIC),
        #                Channel(ChannelState.BUSY),
        #                0,
        #                Channel(ChannelState.BUSY)): 0,
        '2101': 0,

        # 1011
        # SimulatorState(Source(SourceState.LAST_TIC),
        #                Channel(ChannelState.EMPTY),
        #                1,
        #                Channel(ChannelState.BUSY)): 0,
        '1011': 0,

        # 1101
        # SimulatorState(Source(SourceState.LAST_TIC),
        #                Channel(ChannelState.BUSY),
        #                0,
        #                Channel(ChannelState.BUSY)): 0,
        '1101': 0,

        # 2111
        # SimulatorState(Source(SourceState.FIRST_TIC),
        #                Channel(ChannelState.BUSY),
        #                1,
        #                Channel(ChannelState.BUSY)): 0,
        '2111': 0,

        # 0101
        # SimulatorState(Source(SourceState.BLOCKED),
        #                Channel(ChannelState.BUSY),
        #                0,
        #                Channel(ChannelState.BUSY)): 0,
        '0101': 0,

        # 1X11
        # SimulatorState(Source(SourceState.LAST_TIC),
        #                Channel(ChannelState.BLOCKED),
        #                1,
        #                Channel(ChannelState.BLOCKED)): 0,
        '1X11': 0,

        # 0X11
        # SimulatorState(Source(SourceState.BLOCKED),
        #                Channel(ChannelState.BLOCKED),
        #                1,
        #                Channel(ChannelState.BLOCKED)): 0,
        '0X11': 0,

        # 2011
        # SimulatorState(Source(SourceState.FIRST_TIC),
        #                Channel(ChannelState.EMPTY),
        #                1,
        #                Channel(ChannelState.BUSY)): 0,
        '2011': 0,

        # 1100
        # SimulatorState(Source(SourceState.LAST_TIC),
        #                Channel(ChannelState.BUSY),
        #                0,
        #                Channel(ChannelState.EMPTY)): 0,
        '1100': 0,

        # 0100
        # SimulatorState(Source(SourceState.BLOCKED),
        #                Channel(ChannelState.BUSY),
        #                1,
        #                Channel(ChannelState.EMPTY)): 0,
        '0100': 0,

        # 2001
        # SimulatorState(Source(SourceState.FIRST_TIC),
        #                Channel(ChannelState.EMPTY),
        #                0,
        #                Channel(ChannelState.BUSY)): 0,
        '2001': 0,
        '1111': 0,
        '0111': 0,


    }

    def __init__(self, A, K1, K2, Loch, Lk, P):
        self.A = A
        self.K1 = K1
        self.K2 = K2
        self.Loch = Loch
        self. Lk = Lk
        self.P = P

    @property
    def A(self):
        return self._A

    @A.setter
    def A(self, value):
        self._A = value

    @property
    def K1(self):
        return self._K1

    @property
    def K2(self):
        return self._K2

    @property
    def Loch(self):
        return self._Loch

    @K1.setter
    def K1(self, value):
        self._K1 = value

    @K2.setter
    def K2(self, value):
        self._K2 = value

    @Loch.setter
    def Loch(self, value):
        self._Loch = value
