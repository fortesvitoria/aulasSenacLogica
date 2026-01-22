print('5.Faça um Programa que leia três números e mostre-os em ordem decrescente.')
n01 = int(input('Digite um número: '))
n02 = int(input('Digite mais um numero: '))
n03 = int(input('Digite outro numero: '))
numeros = n01, n02, n03
ordem = sorted(numeros, reverse=True)
print(ordem)