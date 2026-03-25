# 8. Desenvolva um calculadora que receba dois números e efetue uma das seguintes operações aritméticas:

#    1 - Adição
#    2 - Subtração
#    3 - Multiplicação
#    4 - Divisão
#    5 - Potência
#    6 - Raiz quadrada
#    7 - Número par
#    8 - Número ímpar

numero1 = float(input('digite o primeiro valor: '))
numero2 = float(input('digite o segundo valor: '))
operacao = input('digite a operação a ser feita, as opções são adição, subtração, multiplicação, divisão, potência, raiz quadrada, número par, número ímpar: ')

if operacao == 'adição':
    print(numero1 + numero2)
elif operacao == 'subtração':
    print(numero1 - numero2)
elif operacao == 'multiplicação':
    print(numero1 * numero2)
elif operacao == 'divisão':
    print(numero1 / numero2)
elif operacao == 'potência': 
    print(numero1 ^ numero2)
# elif operacao == 'raiz quadrada':
#     raiz quadrada dos dois numeros???????
elif operacao == 'número par' or operacao == 'número ímpar':
    if numero1 % numero2 == 0:
        print('número par')
    else:
        print('número ímpar')