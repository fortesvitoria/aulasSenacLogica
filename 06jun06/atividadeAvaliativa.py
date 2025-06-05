'''
Desafio do Professor de Educação Física: Calculadora de IMC da Turma

Situação Temática:

O Professor Carlos, de Educação Física da Escola Pitágoras, está montando o perfil de saúde dos seus
alunos. Para isso, ele precisa calcular o Índice de Massa Corporal (IMC) de cada um e identificar a
situação nutricional da turma. Ele pediu sua ajuda para desenvolver um programa simples que o auxilie
nessa tarefa, usando apenas o terminal do computador.

Seu Programa deve:

1. Perguntar ao Professor Carlos quantos alunos ele deseja cadastrar inicialmente.---------ok

2. Para cada aluno:
o Coletar o nome do aluno. ---------ok
o Coletar o peso do aluno (em quilogramas).---------ok
o Coletar a altura do aluno (em metros).---------ok
o Calcular o IMC usando a fórmula: IMC=peso/(altura×altura).---------ok
o Armazenar os dados (nome, peso, altura, IMC) de cada aluno em listas.---------ok

3. Ao final do cadastro, o programa deve exibir uma tabela organizada com o nome de
cada aluno e seu respectivo IMC.---------ok

4. Após a tabela, o programa deve apresentar um resumo da turma, indicando:---------ok
o A média de IMC da turma.---------ok
o O aluno com o maior IMC e seu valor.---------ok
o O aluno com o menor IMC e seu valor.---------ok

Requisitos:
• Não utilize funções (def) neste exercício, concentre-se em entender o fluxo do
programa.
• Use listas para armazenar os dados dos alunos (nomes, pesos, alturas, IMCs).
• Utilize o laço de repetição while para controlar o número de alunos a serem
cadastrados, permitindo que o professor digite um número válido.
• Utilize o laço de repetição for para coletar os dados de cada aluno e para exibir os
resultados.
• Certifique-se de que o programa lide com entradas inválidas para peso e altura (por
exemplo, se o usuário digitar texto em vez de números), solicitando a informação
novamente até que seja válida.
'''

#1. Perguntar ao Professor Carlos quantos alunos ele deseja cadastrar inicialmente.
while True:
    try:
        qtdAluno = int(input('Digite quantos alunos deseja cadastrar: '))
        break
    except:
        print('Digite somente NUMEROS!')

#Variavel para calcular imc
calcIMC = 0

#Variável para somar imc da turma
soma = 0

#Variável para armazenar maior imc
maior = 0

#Varialvel para armazenar menor imc
menor = 0

#variável contadora
i = 0

#cria lista para armazenar dados
nomeLista = []
pesoLista = []
alturaLista = []
IMCLista = []

for i in range (qtdAluno):
    #Coletar o nome do aluno.
    nome = input(f'Digite nome do aluno {i + 1}: ')
    while True:
        try:
            #Coletar o peso do aluno (em quilogramas).
            peso = float(input(f'Digite o peso de {nome} em kg: '))

            #Coletar a altura do aluno (em metros).
            altura = float(input(f'Digite a altura em metros de {nome}: '))

            #Calcular o IMC usando a fórmula: IMC=peso/(altura×altura)
            calcIMC = peso / (altura**2)

            # Armazenar os dados (nome, peso, altura, IMC) de cada aluno em listas.
            nomeLista.append(nome)
            pesoLista.append(peso)
            alturaLista.append(altura)
            IMCLista.append(calcIMC)

            #calcula imc
            soma += calcIMC

            #inicia looping e variaveis para verificar maior e menor
            if i == 0:
                maior = calcIMC
                menor = calcIMC
                nomeMaior = nome
                nomeMenor = nome
            else:
                #Indica aluno com o maior IMC e seu valor.
                if calcIMC > maior:
                    maior = calcIMC
                    nomeMaior = nome
                #Inidica aluno com o menor IMC e seu valor.
                elif calcIMC < menor:
                    menor = calcIMC
                    nomeMenor = nome
            break
        except:
            print('Digite somente NUMEROS')

# 3. Ao final do cadastro, o programa deve exibir uma tabela organizada com o nome de
# cada aluno e seu respectivo IMC.
print('\nLista de alunos e seus dados:')
print('-' * 30)
for i in range(qtdAluno):
    print(f'Aluno {i + 1}: {nomeLista[i]}')
    print(f'Peso: {pesoLista[i]} kg')
    print(f'Altura: {alturaLista[i]} cm')
    print(f'IMC: {IMCLista[i]:.2f}')
    print('-' * 30)

#4. Após a tabela, o programa deve apresentar um resumo da turma, indicando:
print('\nResumo da turma: ')
#A média de IMC da turma.
print(f'A média de IMC da turma é {soma/qtdAluno:.2f} ')
#O aluno com o maior IMC e seu valor.
print(f'O aluno com maior IMC da turma é {nomeMaior}, com um IMC de {maior:.2f} ')
#O aluno com o menor IMC e seu valor.
print(f'O aluno com menor IMC da turma é {nomeMenor}, com um IMC de {menor:.2f} ')