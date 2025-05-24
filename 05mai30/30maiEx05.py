from xml.sax import parse

print('5. Faça um Programa que leia 20 números inteiros e armazene-os numa lista. ')
print('Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.')
print('-' * 35)

#Cria listas
par = []
impar = []
lista = []

#lopping para entrar com os 20 numeros
for i in range (20):
    numero = int(input('Digite um número INTEIRO: '))
    #se for par
    if numero % 2 == 0:
        #metodos append - insere o dado na última posição da lista - Add apply end
        lista.append(numero)
        par.append(numero)
    else:
        lista.append(numero)
        impar.append(numero)
print(f'Os números inseridos na lista foram: {lista}')
print(f'Os números pares inseridos na lista foram: {par}')
print(f'Os números impar inseridos na lista foram: {impar}')
