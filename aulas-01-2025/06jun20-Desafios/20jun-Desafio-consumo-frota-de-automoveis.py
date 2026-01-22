'''
Exemplo: Gerenciador de Tarefas Simples
Neste exercício, você desenvolverá um programa em Python para gerenciar uma lista de tarefas.
O programa deve ser executado no console e interagir com o usuário através de um menu de opções.
---------------------------------------------
Estrutura de Dados:
1 - Você precisará de duas listas para armazenar os dados das tarefas:

tarefas:
    1.0 - Uma lista de strings para armazenar a descrição de cada tarefa.
    1.1 - status_tarefas: Uma lista de valores booleanos (True ou False) para indicar o status de cada tarefa, correspondendo ao índice da lista tarefas.
        1.1.0 - True significará que a tarefa está concluída, e False que está pendente.
----------------------------------------------
2 - Menu de Opções
    O programa deve apresentar um menu com as seguintes opções:
        2.0 - Adicionar uma nova tarefa: Permite ao usuário inserir a descrição de uma nova tarefa.
            A tarefa deve ser adicionada como pendente (False) por padrão.
        2.1 - Marcar uma tarefa como concluída:
            O usuário informará o número (índice ou um identificador que você definir para exibir ao usuário) da tarefa que deseja marcar como concluída.
            O programa deverá alterar o status dessa tarefa para True.
        3. Listar todas as tarefas, indicando seu status:
            Exibe todas as tarefas cadastradas, mostrando sua descrição e se estão "Concluída" ou "Pendente".
        4. Listar apenas as tarefas pendentes: Exibe somente as tarefas que ainda não foram concluídas.
        5. Listar apenas as tarefas concluídas: Exibe somente as tarefas que já foram marcadas como concluídas.
        6. FIM: Encerra o programa.
---------------------------------------------------
Requisitos Adicionais
    Utilize um laço de repetição para manter o menu ativo até que o usuário escolha a opção "FIM".
    Valide as entradas do usuário sempre que possível (por exemplo, ao adicionar uma tarefa, não permitir descrição vazia;
    ao marcar como concluída, verificar se o número da tarefa é válido)

    Trate possíveis erros, como tentar marcar uma tarefa como concluída que não existe na lista.
    Utilize funções (def) para organizar o código, separando cada funcionalidade do menu em uma função específica.
'''
#cria lista string
lista = ['Ir ao mercado','Passear com os cães']

#cria lista booleanos
status_tarefas = [False, True]

#cria funcao do menu
def menu():
    print(f'{('-' * 10)} Gerenciador de tarefas {('-' * 10)}')
    print('1. Adicionar uma nova tarefa')
    print('2. Marcar uma tarefa como concluída')
    print('3. Listar todas as tarefas, indicando seu status')
    print('4. Listar apenas as tarefas pendentes')
    print('5. Listar apenas as tarefas concluídas')
    print('6. FIM ')

while True:
    try:
        #chama funcao menu
        menu()
        while True:
            try:
                opcaoMenu = int(input('Escolha uma opção: ')) #escolhe a opção
                print(f'A opção escolhida foi "{opcaoMenu}"!')
                if opcaoMenu >= 1 and opcaoMenu <= 6:
                    #opcao adicionar item na lista
                    if opcaoMenu == 1:
                        tarefa = input('Digite a nova tarefa: ')
                        lista.append(tarefa)  # append para incluir nova tarefa na lista
                        status_tarefas.append(False)  # append para incluir status de pendente 'false' na lista
                        print(f'Tarefa {tarefa} adicionada à lista!')

                    #opcao marcar tarefa como conlcuida
                    elif opcaoMenu ==2:
                        indice = int(input('Digite número da tarefa que deseja ser marcada como concluida: '))
                        status_tarefas[indice] = True
                        print(f'Tarefa {lista[indice]} aletarada para CONCLUÍDA!')

                    # opcao listar itens
                    elif opcaoMenu == 3:
                        for i in range(len(lista)):
                            if status_tarefas[i] == False:
                                status = 'Pendente'
                            elif status_tarefas[i] == True:
                                status = 'Concluido'
                            print(f'Item {i + 1} da lista é {lista[i]}. Status:  {status}')
                else:
                    print('Opção inválida')
                    break
            except:
                ('Digite SOMENTE NUMEROS INTEIROS:')
    except:
        print('ERRO!')


