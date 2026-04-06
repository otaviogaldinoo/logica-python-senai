# 2. Desenvolva um programa que leia três números e que imprima:
#    2.1. o maior,
#    2.2. o menor,
#    2.3. a soma,
#    2.4. a média.
# Exemplo:
# num1 = 5	num2 = 3	num3 = 10
# **********
# maior = 10
# menor = 3
# soma = 18
# media = 6
# Salvar o código como: maior_menor.py

numero1 = float(input('digite o primeiro número: '))
numero2 = float(input('digite o segundo número: '))
numero3 = float(input('digite o terceiro número: '))
maior_numero = 0
menor_numero = 0

print(f'------------\nnumero 1: {numero1}, \nnumero 2: {numero2}, \nnumero 3: {numero3} \n--------------------')

if numero1 > numero2 and numero1 > numero3:
    maior_numero = numero1
elif numero2 > numero1 and numero2 > numero3:
    maior_numero = numero2
elif numero3 > numero1 and numero3 > numero2:
    maior_numero = numero3
print(f'maior = {maior_numero}')

if numero1 < numero2 and numero1 < numero3:
    menor_numero = numero1
elif numero2 < numero1 and numero2 < numero3:
    menor_numero = numero2
elif numero3 < numero1 and numero3 < numero2:
    menor_numero = numero3
print(f'menor = {menor_numero}')

print(f'soma = {numero1 + numero2 + numero3}')
print(f'media = {(numero1 + numero2 + numero3) / 3}')