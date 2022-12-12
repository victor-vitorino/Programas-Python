a = int(input('Entre com o primeiro valor'))
b = int(input('Entre com o segundo valor'))

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
print('Soma: {soma}.'
      '\nSubtração: {subtracao}.' 
      '\nMultiplicação: {multiplicacao}'
      '\nDivisão: {divisao}'
      '\nResto: {resto}'.format(soma=soma,
              subtracao=subtracao,
              resto=resto,
              multiplicacao=multiplicacao,
              divisao=divisao))