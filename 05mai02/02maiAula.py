#Loops While em Python: Uma Explicação Detalhada
# O que é um loop While?
# Em Python, o loop while é uma estrutura de controle de fluxo que permite executar um bloco de
# código repetidamente enquanto uma determinada condição for verdadeira. É como dizer ao computador:
# "Faça isso enquanto isso for verdade".
#
# Sintaxe:
#
# while condição:
  # bloco de código a ser repetido
#
# Como funciona:
# Verificação da condição: No início de cada iteração, a condição é verificada.
# Execução do bloco: Se a condição for verdadeira, o bloco de código dentro do loop é executado.
# Repetição: Após a execução do bloco, a condição é verificada novamente, e o processo se repete.
# Encerramento: Quando a condição se torna falsa, o loop é encerrado e o programa continua a execução da
# próxima linha de código após o loop.



print('Exemplos:')
print('1. Contando até 10:')

contador = 0
while contador < 10:
  print(contador)
  contador += 1

#Neste exemplo:
#contador é inicializado com 0.
# A condição contador < 10 é verificada a cada iteração.
# O valor de contador é impresso e incrementado em 1.
# O loop continua até que contador seja igual a 10.

print('-----------------------------')
print('2. Calculando a soma dos números de 1 a 100:')

soma = 0
numero = 1
while numero <= 100:
  soma += numero
  numero += 1

print("A soma dos números de 1 a 100 é:", soma)

#Neste exemplo:
# soma é inicializada com 0 para armazenar o resultado.
# numero é inicializado com 1 para percorrer os números de 1 a 100.
# A cada iteração, numero é adicionado a soma e incrementado em 1.
# O loop continua até que numero seja maior que 100.

print('-----------------------------')

print('3. Pedindo ao usuário um número positivo:')

numero = 0
while numero <= 0:
  numero = int(input("Digite um número positivo: "))
  if numero <= 0:
    print("Número inválido. Tente novamente.")

print("Você digitou:", numero)

#Neste exemplo:
#O loop continua pedindo ao usuário um número até que um número positivo seja digitado.
# Se o número for negativo ou zero, uma mensagem de erro é exibida.
#
# Cuidados ao usar o loop While:
# Condição de parada: É fundamental garantir que a condição do loop eventualmente se torne falsa, evitando loops infinitos.
# Variáveis: As variáveis utilizadas na condição devem ser atualizadas dentro do loop para que a condição mude e o loop possa terminar.
#
# Quando usar o loop While:
# Quando você não sabe exatamente quantas vezes uma ação precisa ser repetida.
# Quando a condição de parada depende de um cálculo ou de uma entrada do usuário.
# Em resumo:
# O loop while é uma ferramenta poderosa em Python que permite automatizar tarefas repetitivas e
# criar programas mais dinâmicos. Compreender sua sintaxe e funcionamento é essencial para dominar a linguagem.
# Gostaria de ver mais exemplos ou tem alguma dúvida específica sobre o loop while?