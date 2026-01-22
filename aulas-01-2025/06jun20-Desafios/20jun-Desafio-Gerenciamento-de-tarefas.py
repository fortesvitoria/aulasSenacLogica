'''
Exercício: Controle de Consumo de Combustível
Neste exercício, você desenvolverá um programa em Python para gerenciar o consumo
de combustível de uma frota de veículos. O programa deve ser executado no console e
interagir com o usuário através de um menu de opções
---------------------------------------------------------------------------
Estrutura de Dados:

1. Você precisará de três listas para armazenar os dados dos veículos:
    1.0 - modelos: Uma lista de strings para armazenar os nomes dos modelos dos automóveis (ex: "Palio", "Onix", "Civic").
    1.1 - kms_percorridos: Uma lista de números (inteiros ou flutuantes) para armazenar a  quilometragem percorrida por cada veículo,
    na mesma ordem dos modelos.
    1.2 - litros_consumidos: Uma lista de números (inteiros ou flutuantes) para armazenar a quantidade de litros de combustível consumidos
    por cada veículo, na mesma ordem dos modelos.

---------------------------------------------------------------------------

Menu de Opções
O programa deve apresentar um menu com as seguintes opções:
    1. Inserir Dados de Veículo: Permite ao usuário adicionar um novo veículo às listas. O
        programa deve solicitar o modelo, a quilometragem percorrida e os litros consumidos.
    2. Listar Veículos e Consumo: Exibe todos os veículos cadastrados, suas respectivas
        quilometragens percorridas, litros consumidos e o consumo médio (Km/L) de cada um.
    3. Veículo Mais Econômico: Identifica e exibe o modelo do veículo que possui o maior
        consumo médio (Km/L).
    4. Veículo Menos Econômico: Identifica e exibe o modelo do veículo que possui o menor
        consumo médio (Km/L).
    5. Média de Consumo do Grupo: Calcula e exibe a média de consumo (Km/L) de todos
        os veículos cadastrados na frota.
    6. FIM: Encerra o programa.
-----------------------------------------------------------------------------
Requisitos Adicionais
Utilize um laço de repetição para manter o menu ativo até que o usuário escolha a opção
"FIM".
Valide as entradas do usuário sempre que possível (por exemplo, garanta que
quilometragem e litros sejam números positivos).
Trate possíveis erros, como tentar calcular a média de consumo quando não há veículos
cadastrados.
O consumo médio deve ser calculado como
Km/L=quilometragem percorrida/litros consumidos.

'''

#Criando listas
modelos = ['Gol']
kms_percorridos = [500]
litros_consumidos = [40]

#cria funcao do menu
def menu():
    print(f'{('-' * 10)} Menu de Controle de Consumo {('-' * 10)}')
    print('1. Inserir Dados de Veículo ')
    print('2. Listar Veículos e Consumo ')
    print('3. Veículo Mais Econômico')
    print('4. Veículo Menos Econômico')
    print('5. Média de Consumo do Grupo ')
    print('6. FIM ')

while True:
    try:
        opcaoMenu = int(input('Escolha uma opção: '))  # escolhe a opção
        print(f'A opção escolhida foi "{opcaoMenu}"!')
        if opcaoMenu >=1 and opcaoMenu <=6:
            menu()
            while True:
                try:
                    if opcaoMenu == 1:
                        print(f'Opção (1) Inserir Dados de Veículo')

                        modelo = input('Digite o modelo: ')
                        modelos.append(modelo)

                        kms = float(input('Digite os kms percorridos: '))
                        kms_percorridos.append(kms)

                        litros = float(input('Digite os litros consumidos: '))
                        litros_consumidos.append(litros)
                        break
                    elif opcaoMenu == 2:
                        for i in range(len(modelo)):
                            print(f'Veículo {i + 1} da lista é {modelos[i]} - KMS percorridos:  {kms_percorridos[i]} - litros consumidos: {litros_consumidos[i]}')
                        break

                    elif opcaoMenu == 6:
                        print('FIM')
                        break
                except:
                    print('ERRO!')
                    break
        else:
            print('OPÇÃO INVALIDA! Digite numeros entre 1 e 6')
    except:
        print('Digite somente NUMEROS!')
