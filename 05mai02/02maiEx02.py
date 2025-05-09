print('Exercícios com while e do-while')
print('2) Faça um programa que leia número reais maiores que zero. Quando for entrado o número zero, o')
print('programa deverá apresentar quantos números foram entrados e a média destes. Resposta:')

#variavel contadora
cont = 0
#variuavel acumuladora
soma = 0
#while infinito
while True:
    n = int(input('Digite um  ou ZERO encerra: '))
    #controle para encerrar
    if n ==0:
          break
    soma = soma + n
    cont +=1
print(f'Quantidade de números {cont}, a soma é {soma} e média {soma/cont}')