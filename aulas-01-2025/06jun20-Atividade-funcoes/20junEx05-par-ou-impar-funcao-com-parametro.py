'''

Exercício 5: Verificar se é Par ou Ímpar

    Descrição:
    1 - Crie uma função chamada eh_par que recebe um parâmetro numero e
    2 - retorna True se o número for par e False se for ímpar.

    Dica: Use o operador de módulo (%) para verificar o resto da divisão por 2. Se o resto for 0, é par.

'''

#cria funcao com parametro e retorna o calculo
def ehPar(num):
    return num % 2 == 0

while True:
    try:
        num = int(input('Digite um número inteiro qualquer: '))
        if ehPar(num): #se for verdade que o num está de acordo com o retorno, ele é par
            print(f'O número {num} é par!')
            break
        else:#caso contrário é impar
            print(f'O número {num} é impar!')
            break
    except:
        print('Opção INVALIDA! Digite SOMENTE NUMEROS INTEIROS!')

#inica a funcao
ehPar(num)