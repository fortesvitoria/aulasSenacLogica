print('2. Faça um Programa que leia uma lista de 10 números reais e mostre-os na ordem inversa.')
print('-' * 35)

# CRIA LISTA
n = [55,77,88,99,11]
print(n)  # imprime lista original
# FOR COM INDICE CONTROLADOR
for i in range (-1, -6, -1): #do -1 ao -6 pulando de -1 em -1
    #imprime o índice e o conteúdo do índice i
    print(f' No indice {i} existe o número {n[i]}')