'''
Exercício 6: Notas de Alunos

Enunciado:
Você tem duas listas: alunos = ["João", "Maria", "Pedro"] e notas = [8.5, 9.0, 7.5].
Usando um laço for e o índice, imprima o nome de cada aluno e sua respectiva nota.

Dicas e Sugestões:
• Lembre-se que o índice de um elemento é a sua posição na lista.
• Você pode usar range(len(lista)) para gerar índices que correspondem ao tamanho
das suas listas.
• Certifique-se de que ambas as listas têm o mesmo número de elementos para evitar
erros.
'''

#Você tem duas listas: alunos = ["João", "Maria", "Pedro"] e notas = [8.5, 9.0, 7.5].

alunos = ["João", "Maria", "Pedro"]
notas = [8.5, 9.0, 7.5]

#variável contadora
i = 0

#Usando um laço for e o índice, imprima o nome de cada aluno e sua respectiva nota.
for i in range(len(alunos)):
    print(f'O aluno {alunos[i]} tirou a nota {notas[i]}')