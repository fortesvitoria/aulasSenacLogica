# 13. Ler um número n e imprimir MENSAGEM 1, MENSAGEM 2 ou MENSAGEM 3, conforme a condição:
# se n <= 10 imprima MENSAGEM 1,
# se n > 10 e <= 100 imprima MENSAGEM 2
# se n >100 imprima MENSAGEM 3,

numero = int(input("Digite um número: "))

if numero <= 10:
    print("Número menor ou igual a 10")
elif numero > 10 and numero <= 100:
    print("Número é maior que 10 ou igual ou menor a 100")
else:
    print("Numero maior que 100")