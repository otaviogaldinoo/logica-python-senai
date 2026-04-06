# 9. Desenvolver um programa que leia cinco números e os exiba na tela.
# Salvar o código como: cinco_num.py

numeros = []

for i in range(5):
    num = float(input(f"Digite o {i+1}º número: "))
    numeros.append(num)
print(f"Os números digitados foram:\n{numeros}")