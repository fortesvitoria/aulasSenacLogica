'''
Exercício 9: Converter Celsius para Fahrenheit

    Descrição:
    1 - Crie uma função chamada celsius_para_fahrenheit que recebe um parâmetro celsius e
    2 - retorna a temperatura equivalente em Fahrenheit.

    A fórmula é: F = (C * 9/5) + 32.

    Dica: Preste atenção na ordem das operações.
'''

#cria funcao para converter C em F
def celsius_para_fahrenheit(c):
    f = (c * 9/5) + 32
    return f

while True:
    try:
        celsius = float(input('Digite a temperatura em Celsius: ')) #pede o valor em C
        f = celsius_para_fahrenheit(celsius) #coloca o valor como parametro na funcao
        print(f'A temperatura digitada foi {celsius} C que é equivalente a {f} F') #imprime na tela resultado
    except:
        print('Opção INVALIDA! Digite SOMENTE NUMEROS!')