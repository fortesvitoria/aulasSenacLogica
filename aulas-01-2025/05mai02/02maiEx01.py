print('Exercícios com while e do-while')
print('1) Faça um programa que implemente um menu onde o usurário deverá selecionar 1 ou 0. Caso seja entrado')
print('um número diferente, o programa deverá solicitar uma nova opção.')

while True:
    n = int(input('Digite os números 1 ou 2: '))
    if n == 1 or n == 2:
        print(f'Você digitou o número {n}')
        break