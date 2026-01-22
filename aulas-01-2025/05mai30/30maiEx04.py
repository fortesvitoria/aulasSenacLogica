print('4. Faça um Programa que leia uma lista de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.')
print('-' * 35)

lista = ['A','B','C','D','E','F','O','I','N','U']
somaConso = 0 #contador

for i in range(len(lista)):
    if lista[i] != 'A' and lista[i] != 'E'and lista[i] != 'I'and lista[i] != 'O'and lista[i] != 'U':
        somaConso += 1
        print(f'A letra {lista[i]}, no indice {i}, é uma CONSOANTE!')

print(f'Existem {somaConso} consoantes nessa lista!')