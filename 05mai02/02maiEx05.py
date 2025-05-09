print('Exercícios com while e do-while')
print('5) Faça um programa que simule a urna eletrônica.')
print('A tela a ser apresentada deverá ser da seguinte forma:')
print('As opcoes sao:')
print('1. Candidato Rodrigues')
print('2. Candidato Carlos')
print('3. Candidato Neves')
print('4. Nulo')
print('5. Branco')
print('Entre com o seu voto:')
print('O programa deverá ler os votos dos eleitores e, quando for entrado o número 6, apresentar as seguintes')
print('informações:')
print('a) O número de votos de cada candidato;')
print('b) A porcentagem de votos nulos;')
print('c) A porcentagem de votos brancos;')
print('d) O candidato vencedor.')
# MENU
c1 = 0
c2 = 0
c3 = 0
c4 = 0
c5 = 0

print("Menu")
print("1) Opção Rodrgiues")
print("2) Opção Carlos")
print("3) Opção Neves")
print("4) Opção Branco")
print("5) Opção Nulo")
print("6) Opção ENCERRAR")

while True:
    opcao=int(input('Opcao:'))
    if opcao == 1:
        print('Você votou em Rodrigues')
        c1 += 1
    elif opcao == 2:
        print('Você votou em Carlos')
        c2 += 1
    elif opcao == 3:
        print('Você votou em Neves')
        c3 += 1
    elif opcao == 4:
        print('Você votou em branco')
        c4 += 1
    elif opcao == 5:
        print('Você votou nule')
        c5 += 1
    elif opcao == 6:
        print('ENCERRADO!')
        break
    else:
        print("Opção inválida!")

soma = c1+c2+c3+c4+c5

print(f"Votos em Rodrigues {c1}")
print(f"Votos em Carlos {c2}")
print(f"Votos em Neves {c3}")
print(f"Votos em branco {c4}")
print(f"Votos em nulo {c5}")
print(f'A soma dos votos é de {soma}')
print(f'1 - {(c1/soma)*100}%')
print(f'2 - {(c2/soma)*100}%')
print(f'3 - {(c3/soma)*100}%')
print(f'4 - {(c4/soma)*100}%')
print(f'5 - {(c5/soma)*100}%')