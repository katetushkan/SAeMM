from constants import LEMER_N, M, R0, A, LEMER
from lemer_generator import LemerGenerator
from utils import show_info, circumstantial_evidence_test, calculate_period

if __name__ == '__main__':

    lemer = LemerGenerator(A, R0, M, LEMER_N)

    show_info(lemer, LEMER)
    circumstantial_evidence_test(lemer.sequence)
    print()
    calculate_period(lemer.sequence)
    print()