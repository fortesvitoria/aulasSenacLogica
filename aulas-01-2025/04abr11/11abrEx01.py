print('Faça um Programa que verifique se uma letra digitada é vogal ou consoante:')

letra = input('Digite uma letra: ')

if letra == 'a' or letra == 'A':
    print(f"A letra digitada é {letra}, ou seja, uma VOGAL")
elif letra == 'e' or letra == 'E':
    print(f"A letra digitada é {letra}, ou seja, uma VOGAL")
elif letra == 'i' or letra == 'I':
    print(f"A letra digitada é {letra}, ou seja, uma VOGAL")
elif letra == 'o'or letra == 'O':
    print(f"A letra digitada é {letra}, ou seja, uma VOGAL")
elif letra == 'u' or letra == 'U':
    print(f"A letra digitada é {letra}, ou seja, uma VOGAL")
else:
    print(f"A letra digitada é {letra}, ou seja, uma CONSOANTE")

print("------------------------------------------------------------")

letra2 = input('Digite uma letra: ')
print(letra2)
print(letra2.upper())
print(letra2.lower())
letra2=letra2.upper()
print(letra2)

print("------------------------------------------------------------")

print('2) Faça um Programa que verifique se uma letra digitada é vogal ou consoante:')

letraX = input('Digite uma letra: ')

if letraX.lower() == 'a' or letraX.lower() == 'á' or letraX.lower() == 'à' or letraX.lower() == 'â' or letraX.lower() == 'ä':
    print(f"A letra digitada é {letra}, ou seja, uma VOGAL")
elif letraX == 'e'  or letraX.lower() == 'é' or letraX.lower() == 'è' or letraX.lower() == 'ê' or letraX.lower() == 'ë':
    print(f"A letra digitada é {letra}, ou seja, uma VOGAL")
elif letraX == 'i'  or letraX.lower() == 'í' or letraX.lower() == 'ì' or letraX.lower() == 'î' or letraX.lower() == 'ï':
    print(f"A letra digitada é {letra}, ou seja, uma VOGAL")
elif letraX == 'o' or letraX.lower() == 'õ' or letraX.lower() == 'ô' or letraX.lower() == 'ö' or letraX.lower() == 'ó' or letraX.lower() == 'ò':
    print(f"A letra digitada é {letra}, ou seja, uma VOGAL")
elif letraX == 'u' or letraX.lower() == 'ü' or letraX.lower() == 'û' or letraX.lower() == 'ù' or letraX.lower() == 'ú':
    print(f"A letra digitada é {letraX}, ou seja, uma VOGAL")
else:
    print(f"A letra digitada é {letraX}, ou seja, uma CONSOANTE")

print("------------------------------------------------------------")

print('3) Faça um Programa que verifique se uma letra digitada é vogal ou consoante:')

while True:
    letraY = input('Digite uma letra ou \'0\' - zero para finalizar: ')
    if letraY == '0':
        break
    vogais ='aáâãäàeëêéèiíìîïoôõòóöuüúùû'
    if letraY.lower() in vogais:
        print('VOGAL!')
    else:
        print('CONSOANTE!')

