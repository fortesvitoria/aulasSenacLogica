'''
Exercício 2: Saudação Personalizada

    Descrição:
    1 - Crie uma função chamada saudar_nome que recebe um parâmetro nome (uma string) e
    2 - imprime a mensagem "Olá, [nome]!".
    Dica: Use f-strings ou a concatenação de strings para incluir o nome na mensagem.
'''

#cria variavel para chamar como parametro
nome = input('Digite seu nome: ')

#1 - cria funcao com um parametro
def saudacao(nome):
    print(f'Olá, {nome}!')

#2 - chama a funcao e imprime o nome
saudacao(nome)