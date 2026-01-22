print('Faça os programas individuais para calcular os perímetros e as áreas das figuras ')
print('geométricas abaixo. Alguns programas precisarão de vários valores de entrada.')
print('FIGURA E')
lado1 = float(input("Digite o lado do seu losango: "))
diagonal1 = float(input("Digite a menor diagonal do seu losango: "))
diagonal2 = float(input("Digite a maior diagonal do seu losango: "))
peri = 4 * lado1
area = (diagonal2 * diagonal1)/2

print(f"O seu perimetro é de {peri:.2f}cm e sua area pe de {area:.2f}cm^2")