'''
Exercício 8: Combinando Listas com zip

Enunciado:
1. Dadas as listas cidades = ["São Paulo", "Rio de Janeiro","Belo Horizonte"] e estados = ["SP", "RJ", "MG"]
2. use a função zip() para iterar sobre ambas as listas simultaneamente.
3. Para cada par de cidade e estado, imprima uma frase como: "São Paulo fica em SP."

Dicas e Sugestões:
• A função zip() é perfeita para combinar elementos de múltiplas listas em pares.
• Ela retorna um objeto que pode ser iterado em um laço for.
'''

#1. Dadas as listas cidades = ["São Paulo", "Rio de Janeiro","Belo Horizonte"] e estados = ["SP", "RJ", "MG"]
cidades = ["São Paulo", "Rio de Janeiro","Belo Horizonte"]
estados = ["SP", "RJ", "MG"]

#2. use a função zip() para iterar sobre ambas as listas simultaneamente.
for cidade, estado in zip(cidades, estados):
    #3. Para cada par de cidade e estado, imprima uma frase como: "São Paulo fica em SP."
    print(f"{cidade} fica no estado de {estado}.")