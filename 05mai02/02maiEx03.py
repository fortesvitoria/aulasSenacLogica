print('Exercícios com while e do-while')
print('3) Altere o seguinte programa para usar while ao invés de for.')

guarda_maior = None
guarda_menor = None
for i in range(10):
    if i == 0:
        numero = int(input("Entre com o 1o numero inteiro: "))
        guarda_maior = numero
        guarda_menor = numero
    else:
        numero = int(input(f"Entre com o {i+1}o numero inteiro: "))
        if numero > guarda_maior:
            guarda_maior = numero
        elif numero < guarda_menor:
            guarda_menor = numero


if guarda_menor is not None and guarda_maior is not None:
    print(f"\nO menor número entrado é: {guarda_menor}")
    print(f"O maior número entrado é: {guarda_maior}")

print('------------------------------------------')