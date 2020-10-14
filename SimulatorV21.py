
from ChanelState import Channel, ChannelState
from SimulationStatistic import SimulationStatistic
from SimulatorState import SimulatorState
from SourceState import Source, SourceState
from constants import QUEUE_MAX_ITEMS_COUNT


class SimulatorV21:

    def __init__(self, generator):
        self.generator = generator

    @classmethod
    def simulation_statistics(cls, generator_type, tact_count, pi1: int, pi2: int):
        statistic = SimulationStatistic(0, 0, 0, 0, 0, 0)
        simulator = SimulatorState(Source(SourceState.FIRST_TIC),
                                   Channel(ChannelState.EMPTY),
                                   0,
                                   Channel(ChannelState.EMPTY))

        cls.update_statistics(simulator, statistic)

        for _ in range(tact_count-1):
            cls.change_simulator_state(generator_type, simulator, statistic, pi1, pi2)
            cls.update_statistics(simulator, statistic)

        statistic.A = statistic.A / tact_count
        statistic.Loch = statistic.Loch / tact_count
        statistic.K1 = statistic.K1 / tact_count
        statistic.K2 /= tact_count

        return statistic

    @staticmethod
    def update_statistics(simulator: SimulatorState, statistics):
        if simulator.channel1 != ChannelState.EMPTY:
            statistics.K1 += 1
        if simulator.channel2 != ChannelState.EMPTY:
            statistics.K2 += 1
        if simulator.queue != 0:
            statistics.Loch += simulator.queue

        state = simulator.source.state + simulator.channel1.state + str(simulator.queue) + simulator.channel2.state
        statistics.SimulationStates[state] = statistics.SimulationStates[state] + 1

    @staticmethod
    def change_simulator_state(generator, simulator, statistic, pi1, pi2):
        if simulator.channel2.state == ChannelState.BUSY.value and (generator.generator.next > pi2):
            simulator.channel2.state = ChannelState.EMPTY
            statistic.A += 1

        if simulator.queue > 0 and simulator.channel2.state == ChannelState.EMPTY.value:
            simulator.channel2.state = ChannelState.BUSY
            simulator.queue -= 1

        if simulator.channel1.state == ChannelState.BUSY.value and (generator.generator.next > pi1):
            if simulator.queue == 0 and simulator.channel2.state == ChannelState.EMPTY.value:
                simulator.channel2.state = ChannelState.BUSY
                simulator.channel1.state = ChannelState.EMPTY
            elif simulator.channel2.state == ChannelState.BUSY.value and simulator.queue < QUEUE_MAX_ITEMS_COUNT:
                simulator.queue += 1
                simulator.channel1.state = ChannelState.EMPTY
            elif simulator.channel2.state == ChannelState.BUSY.value and simulator.queue == QUEUE_MAX_ITEMS_COUNT:
                simulator.channel1.state = ChannelState.BLOCKED
        elif simulator.channel1.state == ChannelState.BLOCKED.value:
            if simulator.queue == 0 and simulator.channel2.state == ChannelState.EMPTY.value:
                simulator.channel2.state = ChannelState.BUSY
                simulator.channel1.state = ChannelState.EMPTY
            elif simulator.channel2.state == ChannelState.BUSY.value and simulator.queue < QUEUE_MAX_ITEMS_COUNT:
                simulator.queue += 1
                simulator.channel1.state = ChannelState.EMPTY

        if simulator.source.state == SourceState.LAST_TIC.value or simulator.source.state == SourceState.BLOCKED.value:
            if simulator.channel1.state == ChannelState.EMPTY.value:
                simulator.channel1.state = ChannelState.BUSY
                simulator.source.state = SourceState.FIRST_TIC
            else:
                simulator.source.state = SourceState.BLOCKED
        elif simulator.source.state == SourceState.FIRST_TIC.value:
            simulator.source.state = SourceState.LAST_TIC