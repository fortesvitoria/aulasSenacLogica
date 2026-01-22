nome = input('Digite seu nome: ')

#looping para repetir enquanto tiver ERRO
while True:
    #inicio do bloco para controlar o ERRO
    try:
        idade = int(input(f'Qual a sua idade, {nome}? '))
        #digitou certo = break - sai quando não houver erro
        break
    #tratamento do ERRO
    except:
        print('Digite um numero INTEIRO!')
        #após o print acima, volta para pedir nova entrada

print(f'{nome} você tem {idade} anos de idade!')
#Finaliza o looping sem ERRO