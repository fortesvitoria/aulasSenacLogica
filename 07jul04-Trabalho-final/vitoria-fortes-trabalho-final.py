'''
GERENCIADOR DE AGENDA DE CONTATOS

Exercício: Gerenciador de Agenda de Contatos
Neste exercício, você desenvolverá um programa em Python para gerenciar uma agenda de contatos.
O programa deve ser executado no console e interagir com o usuário através de um menu de opções

------------------------------------
Estrutura de Dados:

Você precisará de duas listas para armazenar os dados dos contatos:
• nomes_contatos: Uma lista de strings para armazenar os nomes dos contatos.
• telefones_contatos: Uma lista de strings para armazenar os números de telefone dos
contatos (pois podem ter formatação especial como "(XX) XXXX-XXXX")


------------------------------------

Menu de Opções
O programa deve apresentar um menu com as seguintes opções:
1. Adicionar um novo contato: Permite ao usuário inserir um novo nome e número de
telefone na agenda.
2. Buscar o telefone de um contato pelo nome: O usuário informará um nome, e o
programa deverá exibir o telefone correspondente, se o contato existir.
3. Remover um contato pelo nome: O usuário informará um nome, e o programa deverá
remover o contato (nome e telefone) das listas, se ele existir.
4. Listar todos os contatos: Exibe todos os nomes e telefones cadastrados na agenda.
5. FIM: Encerra o programa.

------------------------------------
Requisitos Adicionais
• Utilize um laço de repetição para manter o menu ativo até que o usuário escolha a opção "FIM".
• Valide as entradas do usuário sempre que possível (por exemplo, não permitir que nomes ou telefones sejam
vazios ao adicionar um contato).
• Trate possíveis cenários onde um contato não é encontrado ao tentar buscar ou remover.
• Utilize funções (def) para organizar o código, separando cada funcionalidade do menu em uma função específica.

'''

#lista de cores e estilos para utilizar:
RESET = "\033[0m"
BOLD = "\033[1m"
GREEN = "\033[92m"
BLUE = "\033[94m"
WHITE = "\033[97m"
RED = "\033[91m"
BG_GREEN = "\033[42m"
SETA = "\u2794"

#listas
nome_contatos = ['Lucas','Michelle']
telefone_contatos = ['(51) 99516-7555','(51) 3025-5552']

#inicia menu de opções
def menu():
    print(f'''{BG_GREEN}{WHITE}{BOLD}{'-'*16} SELECIONE UMA OPÇÃO: {'-'*16}{RESET}
    1. Adicionar um novo contato
    2. Buscar o telefone de um contato pelo nome
    3. Remover um contato pelo nome
    4. Listar todos os contatos
    5. Finalizar programa''')
#finaliza funcao menu

#0 - incia funcao para formatar o telefone
def formatar_telefone(numero):
    if len(numero) == 11:  # Celular -  se tiver 11 numeros até a posição 2 vira DDD em (xx), da posição 2 a 7(xxxxx) fica a esquerda do '-' e a partir da posição 7 fica a direita do '-'
        return f"({numero[:2]}) {numero[2:7]}-{numero[7:]}"
    elif len(numero) == 10:  # Fixos - se tiver 01 numeros até a posição 2 vira DDD em (xx), da posição 2 a 6(xxxxx) fica a esquerda do '-' e a partir da posição 6 fica a direita do '-
        return f"({numero[:2]}) {numero[2:6]}-{numero[6:]}"
    else:#caso contrácrio devolve: numero inválido
        return "Número inválido"
#finaliza funcao para formatar o telefone

#1 - inicia funcao add contato
def adicionar():
    while True:
        print('')
        print(f'{BG_GREEN}{WHITE}{'-' * 14}   ADICIONE UM CONTATO:   {'-' * 14}{RESET}')
        nome=input('Digite o nome do contato. Para ENCERRAR digite "FIM": ')
        if nome.upper()=='FIM':
            break
        telefone = input('Digite o telefone do contato sem espaços ou sinais. Para ENCERRAR digite "FIM": ')
        if telefone.upper()=='FIM':
            break

        telefone_formatado = formatar_telefone(telefone) #se receber numeros validos formata
        if telefone_formatado == "Número inválido": #caso contrário recebe 'numero invalido' e mostra mensagem de erro
            print("Número inválido. Deve conter 10 ou 11 dígitos numéricos.")
        nome_contatos.append(nome)
        telefone_contatos.append(telefone_formatado)
#finaliza funcao add contato

#2 - inicia funcao buscar contato pelo nome
def buscar():
    while True:
        print('')
        print(f'{BG_GREEN}{WHITE}{'-' * 16}  BUSQUE UM CONTATO:  {'-' * 16}{RESET}')
        nome = input('Digite o nome do contato que deseja procurar. Para ENCERRAR digite "FIM": ')
        if nome.upper() == 'FIM':
            break
        if nome in nome_contatos:
            i = nome_contatos.index(nome)
            telefone = telefone_contatos[i]
            print(f'Contato encontrado: {nome} - Telefone: {telefone}')
        else:
            print('Contato inexistente!')
#finaliza funcao buscar contato pelo nome

#3 - inicia funcao remover contato utilizando pop
def remover():
    while True:
        print('')
        print(f'{BG_GREEN}{WHITE}{'-' * 16}  REMOVA UM CONTATO:  {'-' * 16}{RESET}')
        nome = input('Digite o nome do contato que deseja remover. Para ENCERRAR digite "FIM": ')
        if nome.upper() == 'FIM':
            break
        if nome in nome_contatos:
            i = nome_contatos.index(nome)
            telefone = telefone_contatos[i]
            nome_contatos.pop(i)
            telefone_contatos.pop(i)
            print(f'Contato encontrado: {nome} REMOVIDO!')
        else:
            print('Contato inexistente!')
#finaliza funcao remover contato

#4 - inicia funcao listar contatos
def listar():
    print('')
    print(f'{BG_GREEN}{WHITE}{BOLD}{'-' * 18} LISTA TELEFONICA {'-' * 18}{RESET}')
    print(f'{BG_GREEN}{WHITE}{BOLD}    CONTATO             |   TELEFONE                  {RESET}')
    print(f'{BG_GREEN}{WHITE}{BOLD}{'-' * 54}{RESET}')
    for i in range(0,len(nome_contatos),1):
        print(f'{GREEN}{i}.{RESET} {nome_contatos[i]}', f'        {GREEN}{SETA}{RESET}        ', telefone_contatos[i])
#finaliza funcao listar contatos

# inícia programa:
while True:
    menu()
    opcao=int(input(f'{GREEN}OPÇÃO ESCOLHIDA:{RESET} '))
    if opcao == 6:
        break
    elif opcao == 1:
        adicionar()
    elif opcao==2:
        buscar()
    elif opcao == 3:
        remover()
    elif opcao == 4:
        listar()
    elif opcao ==5:
        print(f'{RED}{BOLD}PROGRAMA ENCERRADO!')
        break

