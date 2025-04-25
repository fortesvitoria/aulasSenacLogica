print('9. Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), ')
print('se digitar outro valor deve aparecer valor inválido.')

numero = int(input('Digite um número de 1 a 7: '))

if numero == 1:
    print(f'Você digitou o número {numero}, que corresponde a Domingo!')
elif numero == 2:
    print(f'Você digitou o número {numero}, que corresponde a Segunda!')
elif numero == 3:
    print(f'Você digitou o número {numero}, que corresponde a Terça!')
elif numero == 4:
    print(f'Você digitou o número {numero}, que corresponde a Quarta!')
elif numero == 5:
    print(f'Você digitou o número {numero}, que corresponde a Quinta!')
elif numero == 6:
    print(f'Você digitou o número {numero}, que corresponde a Sexta!')
elif numero == 7:
    print(f'Você digitou o número {numero}, que corresponde a Sábado!')
else:
    print('O número digitado não está entre 1 e 7!')