print('Exercícios com while e do-while')
print('Faça um programa que receba uma senha formada de quatro números inteiros,')
print('verifique se a senha está correta e, caso não esteja, solicite novamente a senha. Se a')
print('senha entrada for a correta, deverá ser apresentada a mensagem “Senha Correta”,')

senha = 'Ola123'

while True:
    senha = input('Digite sua senha: ')
    if senha != 'Ola123':
        print(f'Você digitou a senha incorreta: {senha}')
    elif senha == 'Ola123':
        print(f'Você digitou a senha correta: {senha}')
        break
