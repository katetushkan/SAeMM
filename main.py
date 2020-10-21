from SimulatorV21 import SimulatorV21
from StandartGenerator import StandartGenerator
from constants import TICKS, PI1, PI2

if __name__ == '__main__':
    generator = StandartGenerator()
    simulator = SimulatorV21(generator)
    statistics = SimulatorV21.simulation_statistics(simulator, TICKS, PI1, PI2)
    for _ in statistics.SimulationStates:
        print('P[{state}]={value:.5f}'.format(state=_, value=(statistics.SimulationStates.get(_) / TICKS)))
    print('Potkz={value}'.format(value=statistics.Potkz))
    print('Q={value}'.format(value=statistics.Q))
    print('Pbl={value}'.format(value=statistics.Pbl))
    print('Pblk={value}'.format(value=statistics.Pblk))
    print('A={value}'.format(value=statistics.A))
    print('Loch={value}'.format(value=statistics.Loch))
    print('Lc={value}'.format(value=statistics.Lc))
    print('Woch={value}'.format(value=statistics.Woch))
    print('Wc={value}'.format(value=statistics.Wc))
    print('K1={value}'.format(value=statistics.K1))
    print('L1={value}'.format(value=statistics.L1))
    print('K2={value}'.format(value=statistics.K2))


