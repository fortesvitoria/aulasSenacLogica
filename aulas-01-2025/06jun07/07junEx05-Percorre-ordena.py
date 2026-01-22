'''
Exercício 5: Contando Elementos e Ordenando

Enunciado:
1. Crie uma lista de letras = ["a", "b", "a", "c", "b", "a"]
2. Conte quantas vezes a letra "a" aparece na lista.
3. Depois, ordene a lista em ordem alfabética e
4. imprima a lista ordenada.

---> Dicas e Sugestões:
• Explore os métodos de lista que ajudam a contar (count()) e ordenar (sort()).
• O método sort() modifica a lista diretamente.
'''

#1. Crie uma lista de letras = ["a", "b", "a", "c", "b", "a"]
letras = ["a", "b", "a", "c", "b", "a"]

#2. Conte quantas vezes a letra "a" aparece na lista.
#variável para armazenar contagem da letra 'a'
conta = letras.count('a')

print(f'A letra "a" aparece {conta} vezes na listra "letras"!')

#4. imprima a lista ordenada.
#usando sorted para ordenar
print(f'Imprimindo lista de forma ordenada: {sorted(letras)}')

