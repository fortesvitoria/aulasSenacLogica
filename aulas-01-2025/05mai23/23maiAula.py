################################################################################
# 23 / 05 / 2025    LISTAS  REVISÃO FRUTEIRA
teste = 'morango'
# criação da lista
frutas = ['maça', 'Abacate', 'Banana', 'Pera', teste]
print(frutas)  # imprime lista original
frutas[0] = 'melão'  # muda conteúdo de um elemento
print('-' * 20, 'for i in range (1,5,2):', '-' * 20)
# for com índice i Controlado pelo DEV
for i in range(1, 5, 2):
    # imprime o índice e o conteúdo do índice i
    print(f' {i} ==> {frutas[i]}')

print('-' * 20, 'for fruta in frutas:', '-' * 20)
# imprime todo conteúdo da lista colocando
#  na variável
# fruta a cada interação
for fruta in frutas:
    print(fruta)
print('-' * 20, 'for indice, fruta in enumerate(frutas):', '-' * 20)
# imprime todos conteúdo da lista demenbrando
# índice na variável indice e o conteúdo na variável
# fruta
for indice, fruta in enumerate(frutas):
    print(f'índice==> {indice} ==> {fruta}')
print('-' * 40)