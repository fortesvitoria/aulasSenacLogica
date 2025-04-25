import math

print("Exercícios")
print("2. Faça um programa que recebe o raio de uma circunferência, calcular a área e o perímetro da mesma.")
raio = float(input("Digite o raio do circulo: "))
area = math.pi * raio**2
perimetro = 2 * math.pi * raio
print(f"A area do circulo é de {area:.2f} cm^2 e seu perimetro é de {perimetro:.2f}cm")