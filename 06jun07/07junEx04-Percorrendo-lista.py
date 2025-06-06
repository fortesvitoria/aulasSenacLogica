'''
Exercício 4: Verificando a Presença de um Elemento

Enunciado:
1. Crie uma lista de animais = ["cachorro", "gato", "pássaro","peixe"]
2. Peça ao usuário para digitar o nome de um animal
3. Verifique se o animal digitado está na lista
4. imprima uma mensagem informando se ele foi encontrado
5. imprime se não foi encontrado.

Dicas e Sugestões:
• Use a função input() para obter a entrada do usuário.
• O operador in é muito útil para verificar a existência de um elemento em uma lista.
• Considere usar if e else para as duas possibilidades.
'''

#1. Crie uma lista de animais = ["cachorro", "gato", "pássaro","peixe"]
lista = ['cachorro', 'gato', 'pássaro', 'peixe']

#2. Peça ao usuário para digitar o nome de um animal
animal = input('Digite o nome de um animal: ')

#3. Verifique se o animal digitado está na lista
#verificaçãu utilizando if para conserar acentos e textos digitados em caixa alta
#4. imprima uma mensagem informando se ele foi encontrado
if animal.upper() == 'PASSARO':
    print(f'O animal {animal} foi encontrado na lista na posição {lista.index('pássaro')}')
elif animal.upper() == 'PÁSSARO':
    print(f'O animal {animal} foi encontrado na lista na posição {lista.index('pássaro')}')
elif animal.upper() == 'CACHORRO':
    print(f'O animal {animal} foi encontrado na lista na posição {lista.index('cachorro')}')
elif animal.upper() == 'GATO':
    print(f'O animal {animal} foi encontrado na lista na posição {lista.index('gato')}')
elif animal.upper() == 'PEIXE':
    print(f'O animal {animal} foi encontrado na lista na posição {lista.index('peixe')}')
    #5. imprime se não foi encontrado.
else:
    print(f'O animal {animal} não está na lista!')


#VERSÃO SEM CONSIDERAR UPPER CASE UTILIZANDO "IN" PARA PERCORRER A LISTA
print('\n','-' * 10, 'VERSÃO SEM CONSIDERAR UPPER CASE', '-'*10)

#3. Verifique se o animal digitado está na lista
#verificaçãu utilizando if para conserar acentos e textos digitados em caixa alta
#4. imprima uma mensagem informando se ele foi encontrado
if animal.upper() == 'PASSARO':
    print(f'O animal {animal} foi encontrado na lista na posição {lista.index('pássaro')}')
elif animal in lista:
    print(f'O animal {animal} foi encontrado na lista na posição {lista.index(animal)}')
else:
    print(f'O animal {animal} não está na lista!')