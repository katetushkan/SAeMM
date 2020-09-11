from constants import (LEMER_N, M, R0, A, LEMER,
                       SIMPSON, SIMPSON_A, SIMPSON_B,
                       TRIANGULAR, TRIANGLE_A, TRIANGLE_B,
                       GAMMA, GAMMA_TETT, GAMMA_LAMB, EXPONENTIAL,
                       EXPONENTIAL_LAMB, GAUSSIAN_N, GAUSSIAN_MEAN,
                       GAUSSIAN_STD, GAUSS, UNIFORM, UNIFORM_A, UNIFORM_B)
from distrib import (SimpsonDistribution, TriangularDistribution,
                     GammaDistribution, ExponentialDistribution,
                     GaussDistribution, UniformDistribution, SequenceMixin)
from lemer_generator import LemerGenerator
from utils import show_info, circumstantial_evidence_test, calculate_period

if __name__ == '__main__':

    lemer = LemerGenerator(A, R0, M, LEMER_N)
    show_info(lemer, LEMER)

    circumstantial_evidence_test(lemer.sequence)
    print()
    calculate_period(lemer.sequence)
    print()

    temp = SequenceMixin(lemer.sequence)

    # in each distribution below params are set for the best visualisation of distribution histograms
    # lab with this values was successfully passed
    # all params were set by the educator to show right work of the algorithms
    # math characteristics are calculated by numpy functions based on real got values
    # theoretical characteristics don't satisfy the educator

    # Uniform Distribution
    uniform = UniformDistribution(UNIFORM_A, UNIFORM_B)
    show_info(uniform, UNIFORM)

    # Gaussian Distribution
    gauss = GaussDistribution(GAUSSIAN_N, GAUSSIAN_MEAN, GAUSSIAN_STD)
    show_info(gauss, GAUSS)

    # Exponential Distribution
    exp = ExponentialDistribution(EXPONENTIAL_LAMB)
    show_info(exp, EXPONENTIAL)

    # before working with this distribution put 1000-5000 as a 3rd param for a quick resul
    # length here 1000 by default
    # Gamma Distribution
    gamma = GammaDistribution(GAMMA_TETT, GAMMA_LAMB)
    show_info(gamma, GAMMA)

    # before working with this distribution put LEMER_N to a high value if start params are large
    # or to a low value in the other case
    # Triangular Distribution
    triangle = TriangularDistribution(TRIANGLE_A, TRIANGLE_B)
    show_info(triangle, TRIANGULAR)

    # Simpson Distribution
    simpson = SimpsonDistribution(SIMPSON_A, SIMPSON_B)
    show_info(simpson, SIMPSON)