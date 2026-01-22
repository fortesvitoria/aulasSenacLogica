print('2) Faça um programa que pede duas notas de um aluno. Em seguida ele deve calcular a média do '
      'aluno e dar o seguinte resultado:')
print('A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;')
print('A mensagem "Reprovado", se a média for menor do que sete;')
print('A mensagem "Aprovado com Distinção", se a média for igual a dez.')

aluno = input('Digite o nome do(a) Aluno(a): ')

while True:
    nota1 = int(input('Digite a primeira nota: '))
    if nota1 >=0 and nota1 <=10:
        break
    print('Nota inválida, digite novamente!')
while True:
    nota2 = int(input('Digite a segunda nota: '))
    if nota2 >=0 and nota2 <=10:
        break
    print('Nota inválida, digite novamente!')

media = (nota1 + nota2) / 2

if media == 10:
    print(f'A media do(a) aluno(a) foi {media}. Aprovado com Distinção!')
elif media >= 7:
    print(f'A media do(a) aluno(a) foi {media}. Aprovado!')
else:
    print(f'A media do(a) aluno(a) foi {media}. Reprovado!')
