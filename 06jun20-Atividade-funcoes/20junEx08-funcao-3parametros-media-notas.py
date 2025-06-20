'''
Exercício 8: Cálculo de Média Simples

    Descrição:
    1 - Crie uma função chamada calcular_media que recebe três parâmetros, nota1, nota2 e nota3, e
    2 - retorna a média aritmética dessas três notas.

    Dica: A média é a soma dos valores dividida pela quantidade de valores.
'''

#cria funcao para cacular a média
def calculaMedia(a,b,c):
    media = (a+b+c)/3
    return media

while True:
    try:
        #pede as notas
        n1 = float(input('Digite a primeira nota: '))
        n2 = float(input('Digite a segunda nota: '))
        n3 = float(input('Digite a terceira nota: '))

        #coloca os valores digitados dentro dos parametros para fazer o calculo através da funcao
        media = calculaMedia(n1, n2, n3)

        #imprime notas digitadas e informa o resultado da média
        print(f'As notas digitados foram: {n1}, {n2} e {n3}, a média das notas é {media:.2f}')
        break
    except:
        print('Opção INVALIDA! Digite SOMENTE NUMEROS INTEIROS!')