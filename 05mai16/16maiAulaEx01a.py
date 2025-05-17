print('COM LISTA!!!')
print('Digite as 12 temperaturas médias de casa mês do ano')
print('Será calculada a média da temperatura do ano.')

#LISTA MESES
meses = ['','janeiro','feveiro','março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
#Varável acumuladora
soma = 0

for mes in range (1,13): #enquanto for menor de 13. varia de 1 a 12

#lopping para controlar o erro
    while True:
        #inicio do bloco de comando controlado
        try:
            temp = float(input(f'Digite a temperatura média do mês {meses[mes]}: '))
            #acumula todas as temperaturas
            soma+=temp
            #saida sem erro
            break
        #Tratamento de erro
        except:
            print('Digite somente numeros inteiros ou flutuantes!')
            #mensagem de erro, após retonar no looping
print(f'A temperatura média do ano é {(soma/12):.2f}')
#mensagem de saida sem