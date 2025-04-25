print('3. Imprimindo Números em Intervalo Personalizado:')
print('Crie um programa que peça ao usuário dois números como entrada e '
      ' todos os números ímpares no intervalo especificado (inclusive).')

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro número: '))

impar = [i for i in range(n1, n2) if i % 2 != 0]
print(f"O número é: {impar}")

print('----------------------------------------------')

nn1 = int(input('Digite um numero: '))
nn2 = int(input('Digite outro número: '))
for i in range(nn1,nn2):
    if i % 2 != 0:
        print(i)