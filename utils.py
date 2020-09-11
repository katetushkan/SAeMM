from collections import namedtuple
from enum import Enum

import numpy as np
from matplotlib import pyplot

from constants import HIST_INTERVALS, LEMER, LEMER_N


class ParamErrors(Enum):
    NOT_PRIME = 'This number should be prime. '
    NOT_LESS = 'This number should be less then 2^n - 1. '


def create_scheme(sequence, intervals):
    pyplot.hist(sequence, intervals)
    pyplot.show()


def calculate_math_characteristics(sequence):
    array = np.array(sequence)

    m = array.mean()
    d = array.var()
    sq_d = array.std()

    Characteristics = namedtuple('Characteristics', ['math_exp', 'dispersion', 'square_dev'])

    return Characteristics(m, d, sq_d)


def circumstantial_evidence_test(sequence):
    pairs = [(sequence[i], sequence[i + 1]) for i in range(0, len(sequence), 2)]
    k_s = list(filter(lambda pair: pow(pair[0], 2) + pow(pair[1], 2) < 1, pairs))
    k = len(k_s)

    print(f'Got ratio: {2 * k / LEMER_N}')
    print(f'Excpected ration: {np.pi / 4}')


def show_info(obj, dist):

    create_scheme(obj.sequence, HIST_INTERVALS)

    math_exp, dispersion, square_dev = calculate_math_characteristics(obj.sequence)

    if dist == LEMER:
        print(f'{dist} Generator Results:')
    else:
        print(f'{dist} Distribution:')
    print(f'Math expectation = {math_exp}')
    print(f'Dispersion = {dispersion}')
    print(f'Mean square deviation = {square_dev}')
    print()


def calculate_period(sequence):
    xv = sequence[-1]
    values = []
    for i in range(len(sequence)):
        if sequence[i] == xv:
            if len(values) >= 2:
                break
            values.append(i)
    try:
        p = values[1] - values[0]
        print(f'Period = {p}')
    except IndexError:
        print('No period here!')

    try:
        for i in range(len(sequence)):
            if sequence[i] == sequence[i + p]:
                print(f'Aperiodic length = {i + p}')
                break
    except (IndexError, UnboundLocalError) as e:
        print('No aperiodic length')