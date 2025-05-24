print('3. Faça um Programa que leia 4 notas, mostre as notas e a média na tela')
print('-' * 35)

soma = 0 #VARIÁVEL ACUMULADORA

for i in range(0,4):
    while True: #loop para controlar o ERRO
        try:#inicio bloco de comando controlado
            nota=float(input(f'Digite sua nota: '))
            soma+=nota # acumula todas as notas
            break # saida sem ERRO
        except: # Tratamento do ERRO
            print(f'Digite somente valores NUMERICOS!')
            #Mensagem de ERRO e RETORNO para nova leitura
#Continua Programa sem ERROS
print(f'Sua média é {(soma/4):.2f}')