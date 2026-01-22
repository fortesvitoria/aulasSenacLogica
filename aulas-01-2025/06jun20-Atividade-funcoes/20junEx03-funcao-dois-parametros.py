'''
Exercício 3: Soma de Dois Números

    Descrição:
    1- Crie uma função chamada somar que recebe dois parâmetros, num1 e num2, e
    2- retorna a soma deles.

    Dica: O operador de adição é +. Lembre-se de usar return para que a função entregue o resultado.

'''

#1 - cria funcao para soma com dois parametros
def soma(num1,num2):
    resultado = num1 + num2
    return resultado

#recebe numeros digitados nas variaveis
num1 = int(input('Digite o primeiro número para soma: '))
num2 = int(input('Digite o segundo número para soma: '))

#coloca numeros digitados nos parametros
resultado = soma(num1,num2)

#imprime resultado
print(f'A soma entre {num1} e {num2} é {resultado}')
