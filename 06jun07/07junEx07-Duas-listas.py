'''
Exercício 7: Produtos e Preços

Enunciado:
1. Crie duas listas: produtos = ["Monitor", "Teclado", "Mouse"] e precos = [500.00, 150.00, 75.00].
2. Peça ao usuário para digitar o nome de um produto.
3. Se o produto estiver na lista de produtos, imprima o nome do produto e seu preço correspondente.
4. Caso contrário, informe que o produto não foi encontrado.

Dicas e Sugestões:
• Use o método index() para encontrar a posição (índice) do produto digitado na lista
produtos.
• Com o índice em mãos, você pode acessar o preço na lista precos na mesma posição.
• Lembre-se de tratar o caso em que o produto não é encontrado (usando if/else ou um
bloco try-except se já tiverem visto).
'''

#Crie duas listas: produtos = ["Monitor", "Teclado", "Mouse"] e precos = [500.00, 150.00, 75.00].
produtos = ["Monitor", "Teclado", "Mouse"]
precos = [500.00, 150.00, 75.00]

#2. Peça ao usuário para digitar o nome de um produto.
produto = input('Digite o nome do produto: ')

#3. Se o produto estiver na lista de produtos, imprima o nome do produto e seu preço correspondente.
for i in range(len(produtos)):
    #pode digitar em maisuculo ou minusculo.
    if produtos[i].lower() == produto or produtos[i].upper() == produto :
            print(f'O produto {produtos[i]} foi encontrado. Seu valor é de R$ {precos[i]}.')
            break
#4. Caso contrário, informe que o produto não foi encontrado.
else:
    print(f'O produto {produto} não encontrado!')
