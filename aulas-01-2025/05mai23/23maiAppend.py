#Rotina para entrada de dados do usuário para as listas
nomes = []
notas = []
nome=input('Digite o nome do aluno: (Enter - ENCERRA):')
while nome:
    # metodos append - insere o dado na última posição da lista - Add apply end
    nomes.append(nome)
    print(nome)
    nome = input('Digite o nome do aluno: (Enter - ENCERRA):')
print(nomes)
for nome in nomes:
    print(f'Nome no for: {nome}')

#função len() calcula tamanho da lista nomes
print('Tamanho da lista nomes é ', len(nomes))
for i in range(len(nomes)):
    print(f'[{i}] - {nomes[i]}')

#inserir um novo dado na lista em um determinado indice
nome = input('Digite o nome do aluno para inserir: ')
indice = int(input('Digite a posição de inserção: '))
nomes.insert(indice,nome) #posição, dado
nomes.insert(2,'Lucas')#insere e tranfere o dado que tinha para a próxima posição
nomes[1]='Carla' #insere novo dado e deleta o dado anterior
for i in range(len(nomes)):
    print(f'[{i}] - {nomes[i]}')