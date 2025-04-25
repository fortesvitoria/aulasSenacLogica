print('4. Tabuada:')
print('Escreva um programa que gere a tabuada de multiplicação de um número fornecido pelo usuário.')

n = int(input('Digite um número para criarmos a tabuada: '))
for i in range(1, 11):
    print(f"{n} * {i} = {n*i}")

