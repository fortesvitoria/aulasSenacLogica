'''
Exercício 7: Retornar o Quadrado de um Número

    Descrição:
    1 - Crie uma função chamada quadrado que recebe um parâmetro numero e
    2- retorna o quadrado desse número.

    Dica: O quadrado de um número é ele mesmo multiplicado por ele mesmo (numero * numero) ou numero ** 2.
'''

#cria funcao para definir o quadrado retornando o resultado
def quadrado(n):
    resultado = n**2
    return resultado

#se for digitado um numero inteiro, imprime o numero e quadrado dele(chamando a funcao), caso contrario receber um alerta para digitar novamente
while True:
    try:
        n = int(input('Digite um número: '))
        print(f'O número digitado foi {n} e seu quadrado é {quadrado(n)}')
        break
    except:
        print('Opção INVALIDA! Digite SOMENTE NUMEROS INTEIROS!')
