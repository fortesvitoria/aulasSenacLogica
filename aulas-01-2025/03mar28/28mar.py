print ('Hello world!')
nome = 'Emanuel'
sobreNome = 'Fragoso'
print(nome, sobreNome)
nomeDoCliente = 'Gabriel'
print(nomeDoCliente)
print ('O nome do cliente é',nomeDoCliente)
print('O nome do cliente é' + nomeDoCliente)
print(f'Nome do cliente {nome}')
print(f'Nome do cliente{nome}')
idade = 29
ano = 1955
anoAtual = 2025
print (nome, 'tem', idade, 'anos de idade')
print(f'{nome} tem {idade} anos de idade')
print (nome + ' tem ' + str(idade) + ' anos de idade')
print ('Idade', anoAtual - ano)
print (f'Idade {anoAtual - ano}')
print('---------------')
produto = input('Digite o nome do produto:')
preco = float(input('Digite o preco do produto: '))
qtd = int(input('Digite a qtd de mercadorias: '))
print ('Produto     QTD     PRECO    TOTAL')
print (f'{produto} {qtd}  {(qtd * preco)}')
print (f'{produto, qtd, qtd * preco}')

