print('7. Encontrando o Maior Número em uma Lista:')
print('Escreva um programa que encontre o maior número em uma lista de números.')

maior = 0

for i in range (3):
    n=int(input('Digite um número: '))
    if n > maior:
        maior = n
        print(f'Maior = {maior}')

print(f'O maior número digitado foi: {maior}')