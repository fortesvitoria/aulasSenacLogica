print('Faça um programa que recebe um numero não determinado de duas notas de alunos.')
print('Informe se o aluno foi aprovado com média >= 7, conte quantos alunos foram digitados e ')
print('no final calcule a média da turma:')
print('--------------------------------------------------------------------------------------')

#variavel acumuladora
aluno = 0
#media da turma
soma = 0
#lopping para controlar o erro
while True:
    nome = input('Digite seu nome ou "FIM" para encerrar: ')
    if nome.upper() == "FIM":
        break
    while True:
        #inicio do primeiro bloco de comando controlado
        try:
            nota1 = float(input(f'{nome} digite sua primeira nota: '))
            nota2 = float(input(f'{nome} digite sua segunda nota: '))
            aluno += 1
            media = (nota1 + nota2)/2
            soma+=media
            if media >= 7:
                print(f'Media do aluno {nome} é {media}. APROVADO!')
            else:
                print(f'Media do aluno {nome} é {media}. REPROVADO!')
                break
        #Tratamento de erro
        except:
            print('Digite somente numeros inteiros ou flutuantes!')
        #mensagem de erro, após retonar no looping
print(f'Quantidade de alunos: {aluno}. Média da turma: {media}.2f')
# mensagem de saida sem erro

###VERIFICAR
