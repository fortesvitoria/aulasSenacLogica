print('7. As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e')
print('lhe contrataram para desenvolver o programa que calculará os reajustes.')
print('Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:')

print('salários até R$ 2800,00 (incluindo) : aumento de 20%')
print('salários entre R$ 2800,00 e R$ 7000,00 : aumento de 15%')
print('salários entre R$ 7000,00 e R$ 15000,00 : aumento de 10%')
print('salários de R$ 15000,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:')
print('o salário antes do reajuste;')
print('o percentual de aumento aplicado;')
print('o valor do aumento;')
print('o novo salário, após o aumento')
print('------------------------------------------------------------------------------------------------------')
salario = float(input('Digite seu salário: '))
total = 0

if salario <= 2800:
    aumento = (20/100)*salario
    total = salario + aumento
    print(f'O seu salário antes do reajuste era {salario}')
    print(f'o percentual de aumento aplicado foi de 20%')
    print(f'o valor do aumento foi de {aumento}')
    print(f'o novo salário, após o aumento é de {total}')
elif salario > 2800 and salario <= 7000:
    aumento = (15 / 100) * salario
    total = salario + aumento
    print(f'O seu salário antes do reajuste era {salario}')
    print(f'o percentual de aumento aplicado foi de 15%')
    print(f'o valor do aumento foi de {aumento}')
    print(f'o novo salário, após o aumento é de {total}')
elif salario > 7000 and salario <= 15000:
    aumento = (10 / 100) * salario
    total = salario + aumento
    print(f'O seu salário antes do reajuste era {salario}')
    print(f'o percentual de aumento aplicado foi de 10%')
    print(f'o valor do aumento foi de {aumento}')
    print(f'o novo salário, após o aumento é de {total}')
elif salario > 15000:
    aumento = (5 / 100) * salario
    total = salario + aumento
    print(f'O seu salário antes do reajuste era {salario}')
    print(f'o percentual de aumento aplicado foi de 5%')
    print(f'o valor do aumento foi de {aumento}')
    print(f'o novo salário, após o aumento é de {total}')