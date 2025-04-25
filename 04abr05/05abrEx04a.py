print('Faça os programas individuais para calcular os perímetros e as áreas das figuras ')
print('geométricas abaixo. Alguns programas precisarão de vários valores de entrada.')
print('FIGURA A')
ladoA = float(input("Digite o primeiro lado do seu triangulo: "))
ladoB = float(input("Digite o segundo lado do seu triangulo: "))
ladoC = float(input("Digite o terceiro lado do seu triangulo: "))
peri = ladoA + ladoB + ladoC
altura = float(input("Digite a altura do seu triangulo: "))
area = (ladoB * altura)/2

print (f"O lado A é {ladoA}, o lado B é {ladoB}, o lado C é {ladoC} e o a altura é {altura}")
print(f"O seu perimetro é de {peri:.2f}cm e sua area é de {area:.2f}cm^2")