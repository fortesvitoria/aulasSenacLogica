#função sem Parâmetro e sem retorno
def alo():
    print('Hello world!')
# função com parâmetro sem Retorno
def bemVindo(nome):
    print(f'{nome}, Seja Bem Vinda(o)!')
#função sem parâmetro com retorno
def menu():
    print('Digite a Opção desejada')
    print('1 - Somar:')
    print('2 - Subtrair')
    print('3 - FIM')
    while True:
        try:
            opcao = int(input('Digite Opção==>'))
            if opcao >= 1 and opcao <=3:
                break
            else:
                print('Opção INVÁLIDA')
        except:
            print('Digite Números')
    return opcao
#função com Parâmetros e retorno do cálculo
# para o programa principal
def somar(a,b):
    soma=a + b
    return soma

print('Início do Programa')
#chamada da função sem argumentos
alo()

nomeUsuario=input('Digite nome da Criatura:')
#chamda da função com argumento
# bemVindo(33) pode enviar valor não correspondente
# CUIDADADO
bemVindo(nomeUsuario)
opcaoMenu=menu()
print(f'Opção Escolhida foi {opcaoMenu} ')
if opcaoMenu ==1:
    n1=int(input('Digite um Número:'))
    n2=int(input('Digite Outro Número:'))
    # chamada função com argumentos e retorno
    # do cálculo efetuado na função somar(a,b)
    # para variável soma
    soma=somar(n1,n2)
    print(f'Soma de {n1} + {n2} = {soma}  ')
elif opcaoMenu == 2:
    print('subtrair')