'''

Exercício 6: Maior de Dois Números

    Descrição:
    1 - Crie uma função chamada maior_numero que recebe dois parâmetros, a e b, e
    2- retorna o maior deles.

    Dica: Use uma estrutura condicional (if/else) para comparar os dois números.

'''
#cria funcao com dois parametros
def maiorNumero(a,b):
    #verifica se B é maior que a e se for verdade, imprime mensagem, retorna resultado
    if a < b:
        print(f'O número maior é {b}!')
        return b
    # verifica se A é maior que a e se for verdade, imprime mensagem, retorna resultado
    else:
        print(f'O número maior é {a}!')
        return a

#pede que entre um numero inteiro
while True:
    try:
        #pede numeros
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
        break
    except:
        print('Opção INVALIDA! Digite SOMENTE NUMEROS INTEIROS!')

#chama a funcao com parametros
maiorNumero(n1,n2)