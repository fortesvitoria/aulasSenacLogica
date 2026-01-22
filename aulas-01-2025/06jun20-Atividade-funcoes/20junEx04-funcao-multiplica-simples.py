'''
Exercício 4: Multiplicação por Cinco

    Descrição:
    1 - Crie uma função chamada multiplicar_por_cinco que recebe um parâmetro numero e
    2 - retorna o resultado da multiplicação desse número por 5.

    Dica: O operador de multiplicação é *.

'''

#1 - cria funcao para multiplicar por 5
def multiplica(num):
    resultado = num * 5
    return resultado

#recebe numeros digitados na variavel
num = int(input('Digite o primeiro número para soma: '))

#coloca numero digitado no parametro
resultado = multiplica(num)

#2 - imprime resultado
print(f'A multiplicação de {num} por 5 é {resultado}')
