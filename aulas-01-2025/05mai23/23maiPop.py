teste = 'Morango'
# criação da lista
frutas = ['Maça', 'Abacate', 'Banana', 'Pera', teste, 'Abacate', 'Pera']

print(frutas)
for i in range(len(frutas)):
    print(i, frutas[i])

print('-' * 30)

fruta = frutas.pop(4)
#pop remove e guarda o conteudo, nesse caso, salvo na variável fruta
print('POP FRUTA: ', fruta)
for i in range(len(frutas)):
    print(i, frutas[i])

print('-' * 30)
#imprime do 2 ao 4
print('Frutas do 2 ao 4: ', frutas[2:5])
