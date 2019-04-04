# -*- coding: utf-8 -*-
# ############################################### #
#   Atividade I de Meta-Heurística                #
#   Steepest Ascent Hill-Climbing (mais íngreme)  #
#   Autor: Luan H Alves (2278)                    #
# ############################################### #


from random import randint, uniform
from math import sqrt, exp, cos, e, pi

NUM_ITERACOES = 30
NUM_AMOSTRA = 1000


def hill_climbing( file=file ):

    soma_s = 0
    soma_s1 = 0
    soma_s2 = 0

    # Dominio de busca -10 a 10
    S = randint(-10, 11) 
    # Dominio de busca -5 a 5
    S1 = randint(-5, 6)
    S2 = randint(-5, 6)

    S1 = 0.1
    S2 = 0.1

    file.write('S Quatratica; S1 Ackley; S2 Ackley\n')

    for i in range(0, NUM_ITERACOES):
        s = solucao_otima_quadratica(S)
        s1, s2 = solucao_otima_ackley(S1, S2)
        print(s, s1, s2)
        soma_s = soma_s+s
        soma_s1 = soma_s1+s1
        soma_s2 = soma_s2+s2

        solucao_file = str(s)+ ';' + str(s1)+ ';' + str(s2) + '\n'
        file.write(solucao_file)
    
    media_s = soma_s/NUM_ITERACOES
    media_s1 = soma_s1/NUM_ITERACOES
    media_s2 = soma_s2/NUM_ITERACOES

    file.write('\n'+str(media_s)+ ';' +str(media_s1)+ ';' +str(media_s2)+ '\n')

    return 0


def solucao_otima_quadratica(S):

    R = perturbacao(S)
    for j in range(0, NUM_AMOSTRA):
        W = perturbacao(S)
        if (funcao_quadratica(W) < funcao_quadratica(R)):
            R = W

    if (funcao_quadratica(R) < funcao_quadratica(S)):
        S = R

    return S


def solucao_otima_ackley(S1, S2):

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

    return S1, S2


def perturbacao(S):

    return ((S * uniform(-0.8, 0.8)) + S)


def funcao_quadratica(x):

    return pow(x, 2)


def funcao_ackley(X, Y):

    term1 = -20 * exp(-0.2*sqrt(0.5*(X**2 + Y**2)))

    term2 = exp(0.5 * (cos(2*pi*X) + cos(2*pi*Y)))

    ackley = (term1 - term2) + e + 20

    return ackley


def main():

    file = open('resultados.csv', 'w+')
    hill_climbing(file=file)


if __name__ == '__main__':
    main()    
