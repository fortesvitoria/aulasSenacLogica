print('3) Faça um Programa que leia três números inteiros e mostre o maior deles.')
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite um terceiro número: '))
maior = 0
menor = 0
x = 0

if n1 > n2 and n1 > n3:
    maior = n1
    print(f'O maior número digitado foi: {maior}')
elif n2 > n1 and n2 > n3:
    maior = n2
    print(f'O maior número digitado foi: {maior}')
elif n3 > n1 and n3 > n2:
    maior = n3
    print(f'O maior número digitado foi: {maior}')

if n1 < n2 and n1 < n3:
    menor = n1
    print(f'O menor número digitado foi: {menor}')
elif n2 < n1 and n2 < n3:
    menor = n2
    print(f'O menor número digitado foi: {menor}')
elif n3 < n1 and n3 < n2:
    menor = n3
    print(f'O menor número digitado foi: {menor}')