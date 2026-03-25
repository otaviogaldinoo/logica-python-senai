# 2. Desenvolver um programa que leia o consumo de água para uma residência normal e exiba o valor (R$) da conta baseado nos seguintes cálculos:
# Se o consumo for menor ou igual a 10m3, então R$ 22,38
# Se o consumo for menor ou igual a 20m3, então R$ 3,50 por m3
# Se o consumo for menor ou igual a 50m3, então R$ 8,75 por m3
# Se o consumo for acima dos 50m3, então R$ 9,64 por m3
# residencia_normal.py

consumo = input('digite o consumo em m3 da residencia normal: ')

try:
    consumo = float(consumo)
    if consumo <= 10:
        print('conta: R$22,38')
    elif consumo <= 20:
        print(f'R$3,50 por m3, conta: R${consumo * 3.50:.2f}')
    elif consumo <= 50:
        print(f'R$8,75 por m3, conta: R${consumo * 8.75:.2f}')
    elif consumo > 50:
        print(f'R$9,64 pot m3, conta: R${consumo *9.64:.2f}')
except:
    print('por favor digite apenas numeros')