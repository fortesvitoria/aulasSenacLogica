print('6.Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene numa lista a média de cada aluno, ')
print('imprima o número de alunos com média maior ou igual a 7.0.')
print('-' * 35)

#cria lista
lista = []
soma = 0
i = 0

for i in range (2):
    nome = input(f'Digite nome do aluno {i + 1}: ')
    while True:
        try:
            nota1 = float(input('Digite sua nota 1: '))
            nota2 = float(input('Digite sua nota 2: '))
            nota3 = float(input('Digite sua nota 3: '))
            nota4 = float(input('Digite sua nota 4: '))
            soma = nota1 + nota2 + nota3 + nota4
            break
        except:
            print('Digite somente NUMEROS')

lista.append(soma/4)
print(lista, soma)


