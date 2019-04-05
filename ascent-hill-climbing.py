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


def hill_climbing():
    
    file_quad = open('resultados_quad.csv', 'w+')
    file_ackley = open('resultados_ackley.csv', 'w+')

    # Dominio de busca -10 a 10
    S = randint(-10, 11) 
    # Dominio de busca -5 a 5
    S1 = randint(-5, 6)
    S2 = randint(-5, 6)

    S1 = 0.1
    S2 = 0.1

    solucao_otima_quadratica(S, file_quad)
    solucao_otima_ackley(S1, S2, file_ackley)

    return 0


def solucao_otima_quadratica(S, file):

    soma_s = 0

    file.write('Solucao Inicial: ')
    file.write('S= ' + str(S) + '\n')
    file.write('Iteracoes;S Quadratica\n')

    for i in range(0, NUM_ITERACOES):
        R = perturbacao(S)
        for j in range(0, NUM_AMOSTRA):
            W = perturbacao(S)
            if (funcao_quadratica(W) < funcao_quadratica(R)):
                R = W

        if (funcao_quadratica(R) < funcao_quadratica(S)):
            S = R
        
        soma_s = soma_s+S
        file.write(str(i+1) + ';' + str(S) + '\n')

    media_s = soma_s/NUM_ITERACOES
    file.write('\n' + str(media_s) + '\n')


    return S


def solucao_otima_ackley(S1, S2,  file):
    
    soma_s1 = 0
    soma_s2 = 0

    file.write('Solucao Inicial: ')
    file.write('S1= ' + str(S1) + ' S2= ' + str(S2) + '\n')
    file.write('Iteracoes;S1 Ackley; S2 Ackley\n')

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

        soma_s1 = soma_s1+S1
        soma_s2 = soma_s2+S2
        file.write(str(i+1) + ';' + str(S1) + ';' + str(S2) + '\n')

    media_s1 = soma_s1/NUM_ITERACOES
    media_s2 = soma_s2/NUM_ITERACOES
    file.write('\n' +str(media_s1)+ ';' +str(media_s2)+ '\n')

    return S1, S2


def perturbacao(S):

    return ((S * uniform(-0.1, 0.1)) + S)


def funcao_quadratica(x):

    return pow(x, 2)


def funcao_ackley(X, Y):

    term1 = -20 * exp(-0.2*sqrt(0.5*(X**2 + Y**2)))

    term2 = exp(0.5 * (cos(2*pi*X) + cos(2*pi*Y)))

    ackley = (term1 - term2) + e + 20

    return ackley


def main():
    hill_climbing()


if __name__ == '__main__':
    main()    
