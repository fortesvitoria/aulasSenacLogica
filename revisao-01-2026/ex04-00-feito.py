# print('1. Faça um Programa que verifique se uma letra digitada é vogal ou consoante:')
# letra = input("Digite uma letra: ")
# if len(letra) > 1:
#     print("Digite somente uma letra!")

# elif letra.lower() == "a" or letra.lower() == "e" or letra.lower() == "i" or letra.lower() == "o" or letra.lower() == "u":
#     print(f"A letra {letra} é uma vogal")
# else: 
#     print(f"A letra {letra} é uma consoante")



# print("--------------------------------------")

# print('2. Faça um programa que pede duas notas de um aluno. Em seguida ele deve calcular a média do '
#       'aluno e dar o seguinte resultado:')
# print('A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;')
# print('A mensagem "Reprovado", se a média for menor do que sete;')
# print('A mensagem "Aprovado com Distinção", se a média for igual a dez.')

# notas = []
# for i in range(2):
#     n = float(input(f"Digite a nota {i}: "))
#     notas.append(n)
# media = sum(notas)/len(notas)

# if media >= 7:
#     print(f"Nota {media}. Aprovado!")
# if media < 7:
#     print(f"Nota {media}. Reprovado!")
# if media == 10:
#       print(f"Nota {media}. Aprovado com Distinção!")    



# print("--------------------------------------")

# print('3. Faça um Programa que leia três números inteiros e mostre o maiore o menor deles.')
# nums = []
# for i in range(3):
#     n = float(input("Digite um nº: "))
#     nums.append(n)

# print(max(nums))
# print(min(nums))


# print("--------------------------------------")

# print('4. Faça um Programa que leia três números e mostre-os em ordem decrescente.')
# nums = []
# for i in range(3):
#     n = float(input("Digite um nº: "))
#     nums.append(n)
# lista = sorted(nums, reverse=True)
# print(lista)


# print("--------------------------------------")

# print('5. Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.')

# print('Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.')

# while True:
#     turno = input("Digite qual seu turno: M-matutino ou V-Vespertino ou N- Noturno OU SAIR\n")
#     if turno.lower() == "sair":
#       print("Finalizando...")
#       break
#     elif turno.lower() == "m":
#       print("Bom dia!")
#     elif turno.lower() == "v":
#       print("Boa tarde!")
#     elif turno.lower() == "n":
#       print("Boa noite")  
#     else:
#       print("Valor inválido!")  


# print("--------------------------------------")

# print('6. As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e')
# print('lhe contrataram para desenvolver o programa que calculará os reajustes.')
# print('Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:')

# print('salários até R$ 2800,00 (incluindo) : aumento de 20%')
# print('salários entre R$ 2800,00 e R$ 7000,00 : aumento de 15%')
# print('salários entre R$ 7000,00 e R$ 15000,00 : aumento de 10%')
# print('salários de R$ 15000,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:')
# print('o salário antes do reajuste;')
# print('o percentual de aumento aplicado;')
# print('o valor do aumento;')
# print('o novo salário, após o aumento')

# salario = float(input("Digite o valor do seu salário: "))
# if salario <= 2800:
#     porcento = 20
#     aumento = salario*0.20
#     total = salario + aumento
# elif salario > 2800 and salario <= 7000:
#     porcento = 15
#     aumento = salario*0.15
#     total = salario + aumento
# elif salario > 7000 and salario <= 15000:
#     porcento = 10
#     aumento = salario*0.10
#     total = salario + aumento
# elif salario > 15000:
#     porcento = 5
#     aumento = salario*0.05
#     total = salario + aumento

# print(f"Seu salário é de {salario}, com o aumento de {porcento}% você receberá o montante de {total}.")



# print("--------------------------------------")

# print('7. Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, ')
# print('que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do ')
# print('Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto ')
# print('menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.')

# print('Desconto do IR:')
# print('Salário Bruto até 2500 (inclusive) - isento')
# print('Salário Bruto até 15000 (inclusive) - desconto de 5%')
# print('Salário Bruto até 25000 (inclusive) - desconto de 10%')
# print('Salário Bruto acima de 25000 - desconto de 27% Imprima na tela as informações, dispostas conforme o exemplo abaixo. ')
# print('No exemplo o valor da hora é 50 e a quantidade de hora é 220.')

# print('Salário Bruto: (50 * 220)          : R$ 11000,00')
# print('(-) IR (5%)                                : R$     550,00')
# print('(-) INSS ( 10%)                        : R$    1100,00')
# print('FGTS (8%)                              : R$      880,00')
# print('Total de descontos                  : R$    1650,00')
# print('Salário Liquido                        : R$    9350,00')

# horaTrabalho = float(input("Digite o valor da sua hora de trabalho: "))
# horasTrabalhadas = float(input("Digite a quantidade de horas trabalhadas: "))
# salarioBruto = horaTrabalho*horasTrabalhadas
# inss = salarioBruto*0.1
# fgts = salarioBruto*0.08

# if salarioBruto <= 2500:
#     porcentagemIr = 0
#     descontoIr = 0.00
# elif salarioBruto > 2500 and salarioBruto <= 15000:
#     porcentagemIr = 5
#     descontoIr = salarioBruto * 0.05
# elif salarioBruto > 15000 and salarioBruto <= 25000:
#     porcentagemIr = 10
#     descontoIr = salarioBruto * 0.10
# elif salarioBruto > 25000:
#     porcentagemIr = 27
#     descontoIr = salarioBruto * 0.27

# totalDescontos = inss + descontoIr
# valorLiquido = salarioBruto - totalDescontos

# print(f'Salário Bruto: ({horasTrabalhadas} * {horaTrabalho})          : R$ {salarioBruto}')
# print(f'(-) IR ({porcentagemIr}%)                                : R$ {descontoIr}')
# print(f'(-) INSS ( 10%)                        : R$ {inss}')
# print(f'FGTS (8%)                              : R$ {fgts}')
# print(f'Total de descontos                  : R$ {totalDescontos}')
# print(f'Salário Liquido                        : R$ {valorLiquido}')
 

# print("--------------------------------------")

# print('8. Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), ')
# print('se digitar outro valor deve aparecer valor inválido.')

# while True:
#     entrada = int(input("Digite um nº de 1 a 7 ou 8 para sair: "))
#     if entrada == 8:
#         print("Finalizando...")
#         break
#     elif entrada == 1:
#         print("Domingo")
#     elif entrada == 2:
#         print("Segunda")
#     elif entrada == 3:
#         print("Terça")
#     elif entrada == 4:
#         print("Quarta")
#     elif entrada == 5:
#         print("Quinta")
#     elif entrada == 6:
#         print("Sexta")
#     elif entrada == 7:
#         print("Sábado")
#     else:
#         print("Entrada inválida. Tente novamente.")



# print("--------------------------------------")

# print('9. Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,')
# print('e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:')

# print('      Média de Aproveitamento  Conceito')
# print('      Entre 9.0 e 10.0                      A')
# print('      Entre 7.5 e 9.0                       B')
# print('      Entre 6.0 e 7.5                       C')
# print('      Entre 4.0 e 6.0                       D')
# print('      Entre 4.0 e zero                      E')
# print('O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for ')
# print('A, B ou C ou “REPROVADO” se o conceito for D ou E.')

# notas = []
# for i in range(2):
#     nota = float(input(f"Digite sua nota {i+1}: "))
#     notas.append(nota)
# soma = sum(notas)
# media = soma/len(notas)

# if 9 <= media <= 10:
#     info = "Entre 9.0 e 10.0"
#     conceito = "A"
# elif 7.5 <= media < 9:
#     info = "Entre 7.5 e 9.0"
#     conceito = "B"
# elif 6 <= media < 7.5:
#     info = "Entre 6.0 e 7.5"
#     conceito = "C"
# elif 4 <= media < 6:
#     info = "Entre 4.0 e 6.0"
#     conceito = "D"
# elif media < 4:
#     info = "Entre 4.0 e zero"
#     conceito = "E"

# if conceito.lower() == "a" or conceito.lower() == "b" or conceito.lower() == "c":
#     resultado = "APROVADO"
# else:
#     resultado = "REPROVADO"

# print("----------------------------------")
# print('Média de Aproveitamento  Conceito')
# print(f'Nota 1: {notas[0]} - Nota 2: {notas[1]} - Média: {media}')
# print(f"Conceito: {conceito}  -  Status: {resultado}")


# print("--------------------------------------")

# print('10. Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo.')
# print('Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.')

# print('Dicas:')
# print('Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;')
# print('Triângulo Equilátero: três lados iguais;')
# print('Triângulo Isósceles: quaisquer dois lados iguais;')
# print('Triângulo Escaleno: três lados diferentes;')

# lados = []
# for i in range(3):
#     lado = int(input(f"Digite o valor do lado {i+1} do triangulo: "))
#     lados.append(lado)

# if lados[0] == lados[1] == lados[2]:
#     print('Triângulo Equilátero: três lados iguais;')
# elif lados[0] == lados[1] or lados[0] == lados[2] or lados[1] == lados[2]:
#     print('Triângulo Isósceles: quaisquer dois lados iguais;')
# else:
#     print('Triângulo Escaleno: três lados diferentes;')



# print("--------------------------------------")

# print('11. Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax² + bx + c.')
# print('O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:')

# print('Se a = 0, Não é uma equação do segundo grau.')

# print('Calular delta delta = b**2 - 4*a*c')
# print('Se  delta < 0 A equação não possui raízes reais.')

# print('Se delta == 0 Calcular  raiz = -b / (2*a) "A equação possui uma raiz real: x = {raiz:.2f}" ')
# print('Senão calcular ')

# print('raiz1 = (-b + delta**0.5) / (2*a)')
# print('raiz2 = (-b - delta**0.5) / (2*a)')

# print('A equação possui duas raízes reais:')
# print('f"x1 = {raiz1:.2f}')
# print('f"x2 = {raiz2:.2f}')

a = float(input("Digite o valor de a: "))
if a == 0:
    print("Não é uma equação do segundo grau.")
else:
      b = float(input("Digite o valor de b: "))
      c = float(input("Digite o valor de c: "))
      delta = b**2 - 4*a*c
      if delta < 0:
            print("A equação não possui raízes reais.")
      elif delta == 0:
            raiz = -b / (2*a)
            print(f"A equação possui uma raiz real: x = {raiz:.2f}")
      else:
            raiz1 = (-b + delta**0.5)/(2*a)
            raiz2 = (-b - delta**0.5)/(2*a)
            print("A equação possui duas raízes reais:")
            print(f"x1 = {raiz1:.2f}")
            print(f"x2 = {raiz2:.2f}")

