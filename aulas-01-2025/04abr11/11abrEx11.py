print('11. Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo.')
print('Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.')

print('Dicas:')
print('Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;')
print('Triângulo Equilátero: três lados iguais;')
print('Triângulo Isósceles: quaisquer dois lados iguais;')
print('Triângulo Escaleno: três lados diferentes;')

print('----------------------------------------------------------------')

lado1 = float(input('Digite o primeiro lado do trinagulo: '))
lado2 = float(input('Digite o segundo lado do trinagulo: '))
lado3 = float(input('Digite o terceiro lado do trinagulo: '))

if lado1 == lado2 and lado1 == lado3:
    print(f'Lado1 = {lado1}, lado2 = {lado2} e lado3 = {lado3}.')
    print('Triângulo Equilátero: três lados iguais!')
elif lado1 == lado2 or lado1 == lado3:
    print(f'Lado1 = {lado1}, lado2 = {lado2} e lado3 = {lado3}.')
    print('Triângulo Isósceles: quaisquer dois lados iguais!')
elif lado1 != lado2 and lado1 != lado3:
    print(f'Lado1 = {lado1}, lado2 = {lado2} e lado3 = {lado3}.')
    print('Triângulo Escaleno: três lados diferentes!')
