from random import randint, uniform
from math import sqrt, exp, cos, e, pi

NUM_ITERACOES = 30
NUM_AMOSTRA = 10


def hill_climbing():

    # Dominio de busca -10 a 10
    S = randint(-10, 11)
    solucao_otima_quadratica(S)

    # Dominio de busca -5 a 5
    S1 = randint(-5, 6)
    S2 = randint(-5, 6)

    S1 = 0.5
    S2 = 0.5
    solucao_otima_ackley(S1, S2)

    return 0


def solucao_otima_quadratica(S):

    for i in range(0, NUM_ITERACOES):
        R = perturbacao(S)
        for j in range(0, NUM_AMOSTRA):
            W = perturbacao(S)
            if (funcao_quadratica(W) < funcao_quadratica(R)):
                R = W

        if (funcao_quadratica(R) < funcao_quadratica(S)):
            S = R

        print(round(S, 5))  # Escrever resultado em um arquivo!!

    return S


def solucao_otima_ackley(S1, S2):

    for i in range(0, NUM_ITERACOES):
        R1 = perturbacao(S1)
        R2 = perturbacao(S2)
        for j in range(0, NUM_AMOSTRA):
            W1 = perturbacao(S1)
            W2 = perturbacao(S2)
            if (funcao_ackley(W1, W2) < funcao_ackley(R1, R2)):
                R1 = W1
                R2 = W2

        if (funcao_ackley(R1, R2) < funcao_ackley(S1, S2)):
            S1 = R1
            S2 = R2

        print(round(S1, 5), round(S2, 5))  # Escrever resultado em um arquivo!!

    return 0


def perturbacao(S):

    return ((S * uniform(-0.05, 0.05)) + S)


def funcao_quadratica(x):

    return pow(x, 2)


def funcao_ackley(X, Y):

    term1 = -20 * exp(-0.2*sqrt(0.5*(X**2 + Y**2)))

    term2 = exp(0.5 * (cos(2*pi*X) + cos(2*pi*Y)))

    ackley = (term1 - term2) + e + 20

    return ackley


if __name__ == '__main__':
    hill_climbing()
