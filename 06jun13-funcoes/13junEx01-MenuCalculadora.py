#função sem parâmetro com retorno
def menu():
    print('Digite a Opção desejada')
    print('1 - Somar:')
    print('2 - Subtrair')
    print('3 - Multiplicar')
    print('4 - Dividir')
    print('5 - FIM')
    while True:
        try:
            opcao = int(input('Digite Opção==>'))
            if opcao >= 1 and opcao <=5:
                break
            else:
                print('Opção INVÁLIDA')
        except:
            print('Digite números!')
    return opcao

#função com Parâmetros e retorno do cálculo

# para o programa principal
def somar(a,b):
    soma=a + b
    return soma

def subtrair(a,b):
    subtrai = a - b
    return subtrai

def multiplicar(a,b):
    multiplica = a * b
    return multiplica

def dividir(a,b):
    divide = a/b
    return divide

#cria variavel para receber opcao
opcaoMenu=menu()

print(f'Opção Escolhida foi {opcaoMenu} ')

if opcaoMenu ==1:
    n1=int(input('Digite um Número:'))
    n2=int(input('Digite Outro Número:'))

    soma=somar(n1,n2)
    print(f'Soma de {n1} + {n2} = {soma}  ')

elif opcaoMenu == 2:
    n1 = int(input('Digite um Número:'))
    n2 = int(input('Digite Outro Número:'))

    subtrai = subtrair(n1, n2)
    print(f'Soma de {n1} - {n2} = {subtrai}  ')

elif opcaoMenu == 3:
    n1 = int(input('Digite um Número:'))
    n2 = int(input('Digite Outro Número:'))

    multiplica = multiplicar(n1, n2)
    print(f'Soma de {n1} * {n2} = {multiplica}  ')

elif opcaoMenu == 4:
    n1 = int(input('Digite um Número:'))
    n2 = int(input('Digite Outro Número:'))

    divide = dividir(n1, n2)
    print(f'Soma de {n1} / {n2} = {divide}  ')