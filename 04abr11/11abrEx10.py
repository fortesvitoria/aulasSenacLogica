print('10. Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,')
print('e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:')

print('      Média de Aproveitamento  Conceito')
print('      Entre 9.0 e 10.0                      A')
print('      Entre 7.5 e 9.0                       B')
print('      Entre 6.0 e 7.5                       C')
print('      Entre 4.0 e 6.0                       D')
print('      Entre 4.0 e zero                      E')
print('O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for ')
print('A, B ou C ou “REPROVADO” se o conceito for D ou E.')

print('----------------------------------------------------------------')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1+nota2)/2

if media >=0 and media <=4:
    print(f'Sua primeira nota foi {nota1} e a segunda nota foi {nota2}')
    print(f'Sua média foi {media}')
    print('Conceito E. Reprovado!')
elif media >4 and media <=6:
    print(f'Sua primeira nota foi {nota1} e a segunda nota foi {nota2}')
    print(f'Sua média foi {media}')
    print('Conceito D. Reprovado!')
elif media >6 and media <=7.5:
    print(f'Sua primeira nota foi {nota1} e a segunda nota foi {nota2}')
    print(f'Sua média foi {media}')
    print('Conceito C. Aprovado!')
elif media >7.5 and media <= 9:
    print(f'Sua primeira nota foi {nota1} e a segunda nota foi {nota2}')
    print(f'Sua média foi {media}')
    print('Conceito B. Aprovado!')
elif media >9 and media <= 10:
    print(f'Sua primeira nota foi {nota1} e a segunda nota foi {nota2}')
    print(f'Sua média foi {media}')
    print('Conceito A. Aprovado!')