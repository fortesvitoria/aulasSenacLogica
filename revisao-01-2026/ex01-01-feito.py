# print('SEQÜÊNCIAS SIMPLES / CONDICIONAL')
# print('1. Ler dois números e imprimir as variáveis na mesma ordem que foram digitadas:')
# ns = []
# for i in range(2):
#     n = int(input("Digite: "))
#     ns.append(n)

# for n in ns:
#     print(n)


# print('----------------------------------------------')
# print('2. Escreva um algoritmo que leia dois números que deverão ser colocados, respectivamente nas variáveis vA e vB. ')
# vA = int(input("Digite: "))
# vB = int(input("Digite: "))

# print(vA)
# print(vB)



# print('----------------------------------------------')
# print('3. Ler dois valores numéricos e escrever a soma destes.')
# ns = []
# for i in range(2):
#     n = int(input("Digite: "))
#     ns.append(n)

# soma = sum(ns)
# print(soma)



# print('----------------------------------------------')
# print('4. Ler três valores numéricos e escrever a média aritmética.')
# ns = []
# for i in range(3):
#     n = int(input("Digite: "))
#     ns.append(n)
# divisor = len(ns)
# dividendo = sum(ns)
# media = dividendo/divisor
# print(f"{media:.2f}")


# print('----------------------------------------------')
# print('5. Ler um conjunto de 5 dados numéricos e imprimir sua soma e sua média.')
# ns = []
# for i in range(5):
#     n = int(input("Digite: "))
#     ns.append(n)
# divisor = len(ns)
# soma = sum(ns)
# media = soma/divisor
# print(f"Média: {media}; Soma: {soma}")


# print('----------------------------------------------')
# print('6. Faça um algoritmo que leia valores para as variáveis a, b e c e mostre o resultado da seguinte expressão: ( a – b ) * c')
# a = int(input("Digite: "))
# b = int(input("Digite: "))
# c = int(input("Digite: "))
# expressao = (a-b)*c
# print(expressao)


# print('----------------------------------------------')
# print('7. Faça um algoritmo que mostre o resultado da expressão abaixo:')
# print('(( x – 5) * y) – z')
# print('Obs: Ler valores para as variáveis x, y e z.')
# x = int(input("Digite: "))
# y = int(input("Digite: "))
# z = int(input("Digite: "))
# expressao = ((x-5)*y)-z
# print(expressao)


# print('----------------------------------------------')
# print('8. Fazer um algoritmo para ler duas notas, os pesos de cada nota e mostrar a média ponderada.')
# print('                               (nota 1 * peso da nota 1) + (nota 2 * peso da nota 2)')
# print('Cálculo da Média Ponderada = ------------------------------------------------------------------------')
# print('                                                    soma dos pesos')

# nota1 = int(input("Digite: "))
# pesonota1 = int(input("Digite: "))
# nota2 = int(input("Digite: "))
# pesonota2 = int(input("Digite: "))
# soma = pesonota1+pesonota2
# media = ((nota1*pesonota1) + (nota2 * pesonota2))/soma
# print(media)



# print('----------------------------------------------')
# print('9. Escrever um algoritmo para ler uma temperatura em Fahrenheit e apresentá-la convertida em graus Centígrados.')
# print('                           (Fahrenheit – 32) x 5')
# print('Fórmula: Centígrados = ----------------------------')
# print('                                    9')
# temp = int(input("Digite: "))
# celc = ((temp-32)*5)/9
# print(f"{celc:.2f}")



# print('----------------------------------------------')
# print('10. Maria quer saber quantos litros de gasolina precisa colocar em seu carro e quanto vai gastar para fazer uma viagem até a casa de sua irmã.')
# print('Dados extras:')
# print('- Distância da casa de Maria até sua irmã : 520 km - Seu carro consome 12 Km/litro de combustível.')
# print('- Ela abastece sempre no mesmo posto, onde o preço da gasolina é R$ 4,50 o litro.')
# print('Desenvolva um algoritmo onde o usuário digite a distância, o consumo e o valor do litro de combustível,')
# print('com estes dados o algoritmo deverá calcular a quantidade de litros de combustível para a viagem e o custo da viagem.')

# #distancia por litro: 
# litros= 520/12
# preco = litros * 4.5
# print(f"Distancia: 520km;\n Litros: {litros:.2f};\n Valor: {preco:.2f}")
