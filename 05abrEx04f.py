print('Faça os programas individuais para calcular os perímetros e as áreas das figuras ')
print('geométricas abaixo. Alguns programas precisarão de vários valores de entrada.')
print('FIGURA F')
lado1 = float(input("Digite o lado do seu trapezio: "))
lado2 = float(input("Digite o lado do seu trapezio: "))
base1 = float(input("Digite a menor base do seu trapezio: "))
base2 = float(input("Digite a maior base do seu trapezio: "))
altura = float(input("Digite a altura do seu trapezio: "))
peri = lado1 + lado2 + base1 + base2
area = ((base2 + base1)/2)*altura

print(f"O seu perimetro é de {peri:.2f}cm e sua area pe de {area:.2f}cm^2")