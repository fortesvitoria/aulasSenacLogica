import math

print('Faça os programas individuais para calcular os perímetros e as áreas das figuras ')
print('geométricas abaixo. Alguns programas precisarão de vários valores de entrada.')
print('FIGURA G')
raio = float(input("Digite o raio do circulo: "))
area = math.pi * raio**2
perimetro = 2 * math.pi * raio
print(f"A area do circulo é de {area:.2f} cm^2 e seu perimetro é de {perimetro:.2f}cm")