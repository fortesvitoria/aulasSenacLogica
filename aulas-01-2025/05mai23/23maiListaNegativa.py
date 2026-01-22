teste = 'Morango'
# criação da lista
frutas = ['Maça', 'Abacate', 'Banana', 'Pera', teste, 'Abacate', 'Pera']

print(frutas)
frutas.remove('Abacate')

for i, valor in enumerate(frutas):
    print(i, valor)

print('-------------------------')

for i in range (len(frutas)):
    print(i,frutas[i])

print('-------------------------')
#se deletar aletrar range
for i in range (-1, -5, -1): #do -1 ao -6 pulando de -1 em -1
   print(i, frutas[i])

print('-------------------------')

#limite dos indices negativos deve ser
#tamanho da lista len(lista) +1
#transforma em negativo * -1
limite = (len(frutas)+1)*(-1)
print(f'O limite é: {limite}')

for i in range (-1, limite, -1):
    print(i, frutas[i])

print('-------------------------')