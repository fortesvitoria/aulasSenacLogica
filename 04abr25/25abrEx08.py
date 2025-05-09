print('8. Encontrando o Menor Número em uma Lista:')
print('Crie um programa que encontre o menor número em uma lista de números.')

menor = 10000000

for i in range (3):
    n=int(input('Digite um número: '))
    if n < menor:
        menor = n
        print(f'Menor = {menor}')

print(f'O menor número digitado foi: {menor}')