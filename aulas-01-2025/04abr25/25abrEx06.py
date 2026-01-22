print('6. Média de uma Lista:')
print('Modifique o programa anterior para calcular a média aritmética dos elementos de uma lista.')

######FAZER
media = 0
soma = 0
for i in range (3):
    nota=int(input('Digite sua nota: '))
    soma +=nota
    media = soma/3
print(f'A sua média é de {media:.2f}')


print('--------------RESOL PROF')
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"
VERDE = "\033[92m"
RED = "\033[91m"
AZUL = "\033[94m"
WHITE = "\033[97m"

soma1 = 0
print(f'Soma= {soma1}')
for n in range(3):
    num = int(input(f"{VERDE}{i + 1}{RESET})Digite um numero: "))
    soma1 += num
    # print(f'Soma= {soma}')
print(f"\nA soma é igual a:{AZUL} {soma1} {RESET}")
print(f'A média é igual a {AZUL}{soma1 / 3}{RESET}')