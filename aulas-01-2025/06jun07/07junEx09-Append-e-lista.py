'''
Exercício 9: Adicionando Novos Dados

Enunciado:
1. Você tem as listas nomes = ["Ana", "Bruno"] e idades = [25, 30].
2. Peça ao usuário para digitar um novo nome e uma nova idade.
3. Adicione esses novos dados às suas respectivas listas.
4. Em seguida, imprima todas as duplas nome-idade atualizadas.

Dicas e Sugestões:
• Use o método append() para adicionar elementos ao final de cada lista.
• Converta a idade digitada pelo usuário para um número inteiro (int()).
• Depois de adicionar, você pode usar um laço for (com range(len()) ou zip()) para
imprimir o resultado.

'''

#1. Você tem as listas nomes = ["Ana", "Bruno"] e idades = [25, 30].
nomes = ["Ana", "Bruno"]
idades = [25, 30]

#2. Peça ao usuário para digitar um novo nome e uma nova idade.
novoNome = input('Digite seu nome: ')
novaIdade = int(input('Digite sua idade: '))

#3. Adicione esses novos dados às suas respectivas listas.
nomes.append(novoNome)
idades.append(novaIdade)

#4. Em seguida, imprima todas as duplas nome-idade atualizadas.
for i in range(len(nomes)):
    print(f'O usuário {nomes[i]} possui {idades[i]} anos de idade.')