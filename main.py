
# Press the green button in the gutter to run the script.
from SimulationStatistic import SimulationStatistic
from SimulatorV21 import SimulatorV21
from StandartGenerator import StandartGenerator

if __name__ == '__main__':
    generator = StandartGenerator()
    simulator = SimulatorV21(generator)
    statistics = SimulatorV21.simulation_statistics(simulator, 100000, 0.4, 0.5)




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
