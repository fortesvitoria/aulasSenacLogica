print('12. Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax² + bx + c.')
print('O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:')

print('Se a = 0, Não é uma equação do segundo grau.')

print('Calular delta delta = b**2 - 4*a*c')
print('Se  delta < 0 A equação não possui raízes reais.')

print('Se delta == 0 Calcular  raiz = -b / (2*a) "A equação possui uma raiz real: x = {raiz:.2f}" ')
print('Senão calcular ')

print('raiz1 = (-b + delta**0.5) / (2*a)')
print('raiz2 = (-b - delta**0.5) / (2*a)')

print('A equação possui duas raízes reais:')
print('f"x1 = {raiz1:.2f}')
print('f"x2 = {raiz2:.2f}')
print('----------------------------------------------------------------')

a = float(input('Digite um valor: '))
b = float(input('Digite outro valor: '))
c = float(input('Digite mais um valor: '))
delta = (b**2) - (4*a*c)

if a == 0:
    print('Não é uma equação do segundo grau.')
elif delta < 0:
    print('A equação não possui raízes reais.')
elif delta == 0:
    raiz = -b / (2 * a)
    print(f'A equação possui uma raiz real: x = {raiz:.2f}')
else:
    raiz1 = (-b + delta ** 0.5) / (2 * a)
    raiz2 = (-b - delta ** 0.5) / (2 * a)
    print('A equação possui duas raízes reais:')
    print(f'x1 = {raiz1:.2f}')
    print(f'x2 = {raiz2:.2f}')
