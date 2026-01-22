print('Faça os programas individuais para calcular os perímetros e as áreas das figuras ')
print('geométricas abaixo. Alguns programas precisarão de vários valores de entrada.')
print('FIGURA D')
lado1 = float(input("Digite o primeiro lado do seu paralelogramo: "))
lado2 = float(input("Digite o segundo lado do seu paralelogramo: "))
peri = (2 * lado1) + (2 * lado2)
altura = float(input("Digite a altura do seu paralelogramo: "))
area = lado1 * altura

print(f"O seu perimetro é de {peri:.2f}cm e sua area pe de {area:.2f}cm^2")