'''

Exercício 5: Verificar se é Par ou Ímpar

    Descrição:
    1 - Crie uma função chamada eh_par que recebe um parâmetro numero e
    2 - retorna True se o número for par e False se for ímpar.

    Dica: Use o operador de módulo (%) para verificar o resto da divisão por 2. Se o resto for 0, é par.

'''

#cria funcao sem parametro
def ehPar():
    # Verifica se é par ou impar e imprime a mensagem
    while True:
        try:
            num = int(input('Digite um número inteiro qualquer: '))
            if num % 2 == 0:
                print(f'O número {num} é par!')
                break
            else:
                print(f'O número {num} é impar!')
                break
        except:
            print('Opção INVALIDA! Digite SOMENTE NUMEROS INTEIROS!')
    return num
ehPar()