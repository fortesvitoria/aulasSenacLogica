# print('11.Fazer um algoritmo para ler dois números e mostrar o maior deles.')
# nums = []
# for i in range(2):
#     n = int(input("Digite: "))
#     nums.append(n)

# print(max(nums))


# print('12. Ler 3 números e imprimi-los em ordem crescente.')
# nums = []
# for i in range(3):
#     n = int(input("Digite: "))
#     nums.append(n)

# numes = sorted(nums)

# print(numes)


# print('13. Faça um programa que leia o nome de duas pessoas e suas idades e diga qual o mais velho:')
# nome = []
# idade = []
# for i in range(2):
#     n = input("Digite o nome: ")
#     nome.append(n)

# for x in range(2):
#     id = int(input(f"Digite a idade de {nome[x]}: "))
#     idade.append(id)

# if idade[0] > idade[1]:
#     print(f"{nome[0]} é mais velho que {nome[1]}")
# elif idade[0] < idade[1]:
#     print(f"{nome[1]} é mais velho que {nome[0]}")
# else:
#     print(f"{nome[1]} e {nome[0]} possuem a mesma idade.")


# print('14. Ler um número n e imprimir MENSAGEM 1, MENSAGEM 2 ou MENSAGEM 3, conforme a condição:')
# print('se n <= 10 imprima MENSAGEM 1,')
# print('se n > 10 e <= 100 imprima MENSAGEM 2')
# print('se n >100 imprima MENSAGEM 3')

m1 = "Bom dia"
m2 = "Boa tarde"
m3 = "Boa noite"

while True:
    n = int(input("Digite um nº ou 999 para sair: "))
    
    if n == 999:
        print("Finalizando...")
        break
    elif n <= 10:
        print(m1)
    elif n > 10 and n <= 100:
        print(m2)
    else:
        print(m3)

