print('6. Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.')

print('Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.')

turno = input('Digite o turno em que estuda. Digite M-matutino ou V-Vespertino ou N- Noturno.')

if turno.lower() == 'm':
    print('Bom Dia!')
elif turno.lower() == 'v':
    print('Boa tarde!')
elif turno.lower() == 'n':
    print('Boa noite!')
else:
    print('Valor inválido')