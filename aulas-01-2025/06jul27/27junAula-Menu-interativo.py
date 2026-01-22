tarefas=['café','Trabalho','ALmoço','academia','curso Inglês']
status_tarefas=[True,False,False,True,False]
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"
GREEN = "\033[92m"
RED = "\033[91m"
BLUE = "\033[94m"
WHITE = "\033[97m"
YELLOW= "\033[33m"
def menu():
    print(f'''  {BLUE}{BOLD}  --- Gerenciador de Tarefas ------{RESET} 
    {CYAN}1. Adicionar uma nova tarefa 
    2. Marcar uma tarefa como concluída 
    3. Listar todas as tarefas, indicando seu status 
    4. Listar apenas as tarefas pendentes 
    5. Listar apenas as tarefas concluídas 
    6. FIM{RESET} 
    {BLUE}{BOLD}------------------------------- {RESET} 
    ''')
def inserir_tarefas():
    while True:
        tarefa=input('Digite uma Tarefa (FIM==>Encerra):')
        if tarefa.upper()=='FIM':
            break
        tarefas.append(tarefa)
        status_tarefas.append(False)
def listar():
    print('Tarefas     |  Situação')
    print('-----------------------')
    for i in range(0,len(tarefas),1):
        print(i, ')', tarefas[i], '   |   ', f'{RED}Pendente{RESET}' if status_tarefas[i]==False else f'{GREEN}Concluído{RESET}')
def altera_status():
    ind_validos=[]
    for i in range(0,len(status_tarefas),1):
        if status_tarefas[i] == False:
            ind_validos.append(i)
            print(i, ')', tarefas[i], '   |   ', f'{RED}Pendente{RESET}')
    while True: # controla se números estão dentro do conjunto
        while True: # controla se Digitou diferente de inteiro
            try:
                ind=(input(f'Digite índice da tarefa para Concluir ou {YELLOW}(VOLTAR){RESET}:'))
                sair=ind.upper()
                if sair =='VOLTAR':
                    break
                ind=int(ind)
                break
            except:
                print(f'{RED} Digite número INTEIRO {RESET}')
        if sair == 'VOLTAR':
            break
        if ind in ind_validos:
            break
        else:
            print(f'{RED}Digite um índice dentro da lista{RESET}')
    if sair != 'VOLTAR':
        status_tarefas[ind]=True

def tarefas_pendentes():
    for i in range(0,len(status_tarefas),1):
        if status_tarefas[i] == False:
            print(i, ')', tarefas[i], '   |   ', f'{RED}Pendente{RESET}')

def tarefas_concluidas():
    for i, valor in enumerate(status_tarefas):
        if valor == True:
            print(i, ')', tarefas[i], '   |   ', f'{GREEN}Concluído {valor}{RESET}')
### início do Programa
while True:
    menu()
    opcao=int(input('Opção:'))
    if opcao == 6:
        break
    elif opcao == 1:
        inserir_tarefas()
    elif opcao==2:
        altera_status()
    elif opcao == 3:
        listar()
        input('[ENTER] => Continua')
    elif opcao == n:
        tarefas_pendentes()
        input('[ENTER] => Continua')
    elif opcao == 5:
        tarefas_concluidas()
        input('[ENTER] => Continua')


print(f"{GREEN}FIM do Programa - Tchau{RESET}")
