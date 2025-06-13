'''
Exercício 10: Média de Notas de Várias Disciplinas

Enunciado:
1. Crie três listas: disciplinas = ["Matemática", "Português", "História"], notas_aluno1 = [7.0, 8.0, 6.5] e
notas_aluno2 = [9.0,7.5, 8.0].

2. Calcule e imprima a média das notas para cada aluno em todas as disciplinas.

Dicas e Sugestões:
• Para calcular a média, some todas as notas e divida pelo número de notas.
• Você pode usar a função sum() para somar os elementos de uma lista e len() para
obter o número de elementos.
• Faça o cálculo separadamente para cada aluno.
'''

#1. Crie três listas: disciplinas = ["Matemática", "Português", "História"], notas_aluno1 = [7.0, 8.0, 6.5] e notas_aluno2 = [9.0,7.5, 8.0].
disciplinas = ["Matemática", "Português", "História"]
notas_aluno1 = [7.0, 8.0, 6.5]
notas_aluno2 = [9.0,7.5, 8.0]

#2. Calcule e imprima a média das notas para cada aluno em todas as disciplinas.
media_aluno1 = sum(notas_aluno1) / len(notas_aluno1)
media_aluno2 = sum(notas_aluno2) / len(notas_aluno2)

print(f"A média das notas do aluno 1: {media_aluno1:.2f}")
print(f"A média das notas do aluno 2: {media_aluno2:.2f}")