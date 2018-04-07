# -*- coding: utf-8 -*-
import random


def desafio_1(lista, numero):
# Implementação de um algoritimo de pesquisa binaria.

# Inicialização dos parametros iniciais.
    inicio = 0
    fim = len(lista) - 1
    centro = len(lista) / 2

    while(True):
# Retorna a posição da lista onde se encontra o número desejado.
        if(lista[centro] == numero):
            return centro

# Caso não tenha achado o valor desejado retorna -1.
        if(inicio == fim):
            return -1
        else:
# Atualização dos parametros de busca para a proxima iteração.
            if(numero > lista[centro]):
                inicio = centro + 1
                #print inicio
            else:
                fim = centro
                #print fim

        centro = (fim + inicio) / 2


def mergeSort(lista):
# Implementação do algoritimo de ordenação Merge sort.

    if len(lista) > 1:

        index_esq = 0
        index_dir = 0
        index_sorted = 0
        centro = len(lista) / 2

        esquerda = lista[0:centro]
        direita = lista[centro:len(lista)]

        mergeSort(esquerda)
        mergeSort(direita)

        while index_esq < len(esquerda) and index_dir < len(direita):
            if esquerda[index_esq] < direita[index_dir]:
                lista[index_sorted] = esquerda[index_esq]
                index_esq += 1
            else:
                lista[index_sorted] = direita[index_dir]
                index_dir += 1

            index_sorted += 1

        while index_esq < len(esquerda):
            lista[index_sorted] = esquerda[index_esq]
            index_esq += 1
            index_sorted += 1

        while index_dir < len(direita):
            lista[index_sorted] = direita[index_dir]
            index_dir += 1
            index_sorted += 1


def desafio_2(lista1, lista2):
    lista_intersec = []

# Organiza a lista1 a para poder usar o algoritimo de pesquisa binaria
# do desafio_1.
    mergeSort(lista1)
# Percorre a lista 2 e verifica se o valor existe na lista2.
    for index in range(0, len(lista2)):
        pos = desafio_1(lista1, lista2[index])
# Caso a função retorne uma posição valida adiciona na lista que sera retornada.
        if(pos != -1):
            lista_intersec.append(lista2[index])
    return lista_intersec


def desafio_3(numero):
    lista_primos = []

# Como o primeiro número primo é 2 só necessario continuar caso o número
# selecionado seja maior ou igual.
    if(numero >= 2):
        lista_primos.append(2)

# A Pesquisa de numeros primos começa a partir do número 3 e vai até o numero
# passado como parametro com passos de dois descosiderando assim os números
# pares.
        for atual in range(3, numero + 1, 2):
            for index in range(0, len(lista_primos)):
# Para evitar calculos desnecessarios só são usados os números primos
# anteriores ao número atual como divisores.
                resto = atual % lista_primos[index]
# Termina a iteração do loop assim que for encontrado o primeiro divisor.
                if (resto == 0):
                    break
# Caso o número não tenha nenhum divisor na lista ele é adicionado como um
# número primo.
                elif (index == len(lista_primos) - 1):
                    lista_primos.append(atual)

    return lista_primos


def desafio_4(palavra):
# Inicialização dos parametros iniciais. as variaveis upper_offset e
# lower_offset servem para que na hora que seja feita a soma todos os
# caracteres tenham os valores esperados, esse valores foram obitidos com base
# na table ASCII.
    valor_palavra = 0
    upper_offset = 38
    lower_offset = 96
    primo = True

# Varre a string passada e faz a soma do valor de seus caracteres.
    for index in range(0, len(palavra)):
        if palavra[index].isupper():
            valor_palavra += ord(palavra[index]) - upper_offset
        else:
            valor_palavra += ord(palavra[index]) - lower_offset

# Retorna falso caso o somatório seja menor que dois ou seja um número par
# diferente de dois.
    if((((valor_palavra % 2) == 0) and (valor_palavra != 2)) or (valor_palavra < 2)):
        primo = False
    else:
# Retorna falso caso o somatório seja divisel pelo valor pelo valor da variavel
# atual, para diminuir o numero de calculos, é usado passo 2 para evitar
# números pares que já são cosiderados na decisão anterior e só o limite do for
# é a metade do valor do somatório já que qualquer valor acima não tera um
# resultado inteiro.
        for atual in range(3, (valor_palavra / 2) + 1, 2):
            if ((valor_palavra % atual) == 0):
                primo = False
                break

    return primo


def main():
# Desafio 1:
    print '\n Desafio 1:'
# Lista em orden crescente com 300 elementos indo de 0 a 299
    lista_desf1 = [x for x in range(0, 300)]
# Número aleatório digitado pelo usuario para ser procurado na lista.
    numero = input('Digite um número: ')
# Pesquisa o numero escolhido na lista.
    pos = desafio_1(lista_desf1, numero)
    if (pos != -1):
        print ('O número ' + repr(numero) + ' se encontra na posição ' +
        repr(pos) + ' da lista.')
    else:
        print ('O número ' + repr(numero) + ' não se encontra na lista.')

# Desafio 2:
# Acha os números em comum entre as duas listas
    lista2_desf2 = [random.randint(0, 5000000) for x in range(500)]
    lista1_desf2 = [random.randint(0, 5000000) for x in range(50000)]
    lista_desf2 = desafio_2(lista1_desf2, lista2_desf2)
    print '\n Desafio 2:'
    print 'Lista de números que existem em ambas as listas: '
    print repr(lista_desf2)

# Desafio 3:
# Lista de números primos, incluindo o número de entrada caso ele seja primo.
    print '\n Desafio 3:'
    numero = input('Digite um número: ')
    lista_primos = desafio_3(numero)
    print 'Lista de números primos: '
    print repr(lista_primos)

#Desafio 4:
# Atribui valores númericos para os caracteres de uma string e verifica se a
# soma dos valores é um número primo
    print '\n Desafio 4:'
    palavra = input('Digite a palavra ser calculada: ')
    is_prime = desafio_4(palavra)
    msg = ''
    if(not(is_prime)):
        msg = ' não é prima.'
    else:
        msg = ' é prima.'

    print('A palavra ' + palavra + msg)

if __name__ == "__main__":
    main()