#começa por 1
cont=0
while cont <25:
    print(cont)
    #soma de 5 em 5
    cont+=5

print('--------------------------------------')

nome = input('Digite um nome ou "FIM" para encerrar: ')
while nome.upper() !='FIM':
    print (f'Ola {nome}')
    nome = input('Digite um nome ou "FIM" para encerrar: ')
else:
    print("Encerrado")

print('--------------------------------------')

while True:
    nome = input('Digite um nome ou "FIM" para encerrar: ')
    if nome.upper() == 'FIM':
        break
    print(f'Oiii {nome}')
