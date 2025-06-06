'''
Exercício 3: Iterando sobre uma Lista

Enunciado:
1. Dada a lista cores = ["vermelho", "azul", "verde", "amarelo"]
2. Use um laço for para imprimir cada cor na lista, uma por linha

---> Dicas e Sugestões:
• O laço for é ideal para percorrer todos os itens de uma lista.
• A sintaxe básica de um for para listas é for item in lista:.

'''

#criando variaveis com cores
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m"

#1. Dada a lista cores = ["vermelho", "azul", "verde", "amarelo"]
lista = ['vermelho', 'azul', 'verde', 'amarelo']

#2. Use um laço for para imprimir cada cor na lista, uma por linha
for i in range(len(lista)):
    #usando if para imprimir os itens coloridos
    if lista[i] == 'vermelho' :
        print(f'{red} O item {1+i} da lista é {lista[i]}')
    elif lista [i] == 'azul':
        print(f'{blue} O item {1 + i} da lista é {lista[i]}')
    elif lista [i] == 'amarelo':
        print(f'{yellow} O item {1 + i} da lista é {lista[i]}')
    elif lista [i] == 'verde':
        print(f'{green} O item {1 + i} da lista é {lista[i]}')
