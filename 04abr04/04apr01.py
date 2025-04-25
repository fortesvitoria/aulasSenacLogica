print('Faça um programa que leia o nome de duas pessoas e suas idades e diga qual o mais velho:')
pessoa01 = input('Digite seu nome: ')
idade01= int(input(f'Digite a idade de {pessoa01}: '))
pessoa02 = input('Digite seu nome: ')
idade02 =int(input(f'Digite a idade de {pessoa02}: '))

if idade01 > idade02:
    print(f'O usuario {pessoa01} é mais velho que o usuário {pessoa02}')
elif idade01 < idade02:
    print(f' {pessoa02} e {pessoa01} possuem a mesma idade!')
else:
    print(f'O usuario {pessoa02} é mais velho que o usuário {pessoa01}')
