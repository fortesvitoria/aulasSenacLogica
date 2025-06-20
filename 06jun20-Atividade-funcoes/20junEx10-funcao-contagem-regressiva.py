'''

Exercício 10: Contagem Regressiva Simples

    Descrição:
    1 - Crie uma função chamada contagem_regressiva que recebe um parâmetro inicio (um número inteiro positivo) e
    2 - imprime uma contagem regressiva de inicio até 1, e depois imprime "Fim!".
    Dica: Use um loop for ou while. Neste caso, a função não precisa retornar um valor, apenas imprimir.

'''
while True:
    try:
        tempo = int(input('Digite um número inteiro:')) #pede o número inteiro
        break
    except:
        print('Digite somente NUMEROS INTEIROS')

def contagem_regressiva(num):
    for i in range(num,0, -1): #realiza contagem regressiva, numero iniciando a partir do 1 (0), pulando de 1 em 1 (-1)
        print(i) #imprime contagem regressiva

#chama a funcao
contagem_regressiva(tempo)