print('11.Fazer um algoritmo para ler dois números e mostrar o maior deles.')
var01 = int(input('Digite um número: '))
var02 = int(input('Digite outro número: '))
if var01 > var02:
    print(f'O primeiro número é maior que o segundo!')
else:
    print('O segundo número é maior que o primeiro!')
print('----------------------------------')
print('12. Ler 3 números e imprimi-los em ordem crescente.')
num01 = int(input('Digite um numero: '))
num02 = int(input('Digite outro numero: '))
num03 = int(input('Digite outro numero: '))
if num01 < num02 and num01 < num03:
    menor = num01
#sobra 2 numeros
    if num02 < num03:
        meio = num02
        maior = num03
    else:
        meio = num03
        maior = num02
elif num02<num01 and num02<num03:
    if num01<num03:
        meio = num01
        maior = num03
    else:
        meio = num03
        maior = num01
else:
    menor = num03
    if num02<num01:
        meio = num02
        maior = num01
    else:
        meio = num01
        maior = num02
print(f'{menor} {meio} {maior}')
print(f'{maior} {meio} {menor}')



print('----------------------------------')
print('13. Ler um número n e imprimir MENSAGEM 1, MENSAGEM 2 ou MENSAGEM 3, conforme a condição:')
print('se n <= 10 imprima MENSAGEM 1,')
print('se n > 10 e <= 100 imprima MENSAGEM 2')
print('se n >100 imprima MENSAGEM 3')