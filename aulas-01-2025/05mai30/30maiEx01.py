print('01. Faça um Programa que leia uma lista de 5 números inteiros e mostre-os.')
print('-' * 35)

# CRIA LISTA
n = [55,77,88,99,11]
print(n)  # imprime lista original
# FOR COM INDICE CONTROLADOR
for i in range(len(n)):
    # imprime o índice e o conteúdo do índice i
    print(f' No indice {i} existe o número {n[i]}')