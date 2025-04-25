print('8. Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, ')
print('que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do ')
print('Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto ')
print('menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.')

print('Desconto do IR:')
print('Salário Bruto até 2500 (inclusive) - isento')
print('Salário Bruto até 15000 (inclusive) - desconto de 5%')
print('Salário Bruto até 25000 (inclusive) - desconto de 10%')
print('Salário Bruto acima de 25000 - desconto de 27% Imprima na tela as informações, dispostas conforme o exemplo abaixo. ')
print('No exemplo o valor da hora é 50 e a quantidade de hora é 220.')

print('Salário Bruto: (50 * 220)          : R$ 11000,00')
print('(-) IR (5%)                                : R$     550,00')
print('(-) INSS ( 10%)                        : R$    1100,00')
print('FGTS (8%)                              : R$      880,00')
print('Total de descontos                  : R$    1650,00')
print('Salário Liquido                        : R$    9350,00')

print('-------------------------------------------------')

salarioHora = float(input('Digite o valor da hora do seu salário: '))
horas = float(input('Digite o total de horas trabalhadas no mes: '))

salarioBruto = salarioHora * horas
sindicato = (3/100)*salarioBruto
fgts = (11/100)*salarioBruto
ir = 0
descontos = 0
salarioLiq = 0

if salarioBruto > 0 and salarioBruto <= 2500:

    descontos = sindicato + fgts + ir
    salarioLiq = salarioBruto - descontos

    print(f'Salário Bruto: {salarioHora:.2f} * {horas:.2f}: R$ {salarioBruto:.2f}')
    print('(-) IR (0%): R$ 0,00')
    print(f'(-) Sindicato (3%): R$ -{sindicato:.2f}')
    print(f'FGTS (11%: R$ -{fgts:.2f}')
    print(f'Total de descontos: R$ {descontos:.2f}')
    print(f'Salário Liquido: R$ {salarioLiq:.2f}')

elif salarioBruto > 2500 and salarioBruto <= 15000:

    ir = (5/100)*salarioBruto
    descontos = sindicato + fgts + ir
    salarioLiq = salarioBruto - descontos

    print(ir)
    print(f'Salário Bruto: {salarioHora:.2f} * {horas:.2f}: R$ {salarioBruto:.2f}')
    print(f'(-) IR (5%): R$ -{ir:.2f}')
    print(f'(-) Sindicato (3%): R$ -{sindicato:.2f}')
    print(f'FGTS (11%: R$ -{fgts:.2f}')
    print(f'Total de descontos: R$ {descontos:.2f}')
    print(f'Salário Liquido: R$ {salarioLiq:.2f}')

elif salarioBruto > 15000 and salarioBruto <= 25000:

    ir = (10/100)*salarioBruto
    descontos = sindicato + fgts + ir
    salarioLiq = salarioBruto - descontos

    print(ir)
    print(f'Salário Bruto: {salarioHora:.2f} * {horas:.2f}: R$ {salarioBruto:.2f}')
    print(f'(-) IR (10%): R$ -{ir:.2f}')
    print(f'(-) Sindicato (3%): R$ -{sindicato:.2f}')
    print(f'FGTS (11%: R$ -{fgts:.2f}')
    print(f'Total de descontos: R$ {descontos:.2f}')
    print(f'Salário Liquido: R$ {salarioLiq:.2f}')

elif salarioBruto > 25000:

    ir = (27 / 100) * salarioBruto
    descontos = sindicato + fgts + ir
    salarioLiq = salarioBruto - descontos

    print(ir)
    print(f'Salário Bruto: {salarioHora:.2f} * {horas:.2f}: R$ {salarioBruto:.2f}')
    print(f'(-) IR (27%): R$ -{ir:.2f}')
    print(f'(-) Sindicato (3%): R$ -{sindicato:.2f}')
    print(f'FGTS (11%: R$ -{fgts:.2f}')
    print(f'Total de descontos: R$ {descontos:.2f}')
    print(f'Salário Liquido: R$ {salarioLiq:.2f}')