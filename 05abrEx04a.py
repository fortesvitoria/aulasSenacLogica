print('Faça os programas individuais para calcular os perímetros e as áreas das figuras ')
print('geométricas abaixo. Alguns programas precisarão de vários valores de entrada.')
print('FIGURA A')
lado1 = float(input("Digite o primeiro lado do seu triangulo: "))
lado2 = float(input("Digite o segundo lado do seu triangulo: "))
lado3 = float(input("Digite o terceiro lado do seu triangulo: "))
peri = lado1 + lado2 + lado3
altura = float(input("Digite a altura do seu triangulo: "))
area = (lado1 * altura)/2

print(f"O seu perimetro é de {peri:.2f}cm e sua area pe de {area:.2f}cm^2")