# 1. Desenvolver um programa que leia o consumo de água para uma residência social e exiba o valor (R$) da conta baseado nos seguintes cálculos:
# Se o consumo for menor ou igual a 10m3, então R$ 7,59
# Se o consumo for menor ou igual a 20m3, então R$ 1,31 por m3
# Se o consumo for menor ou igual a 30m3, então R$ 4,64 por m3
# Se o consumo for menor ou igual a 50m3, então R$ 6,62 por m3
# Se o consumo for acima dos 50m3, então R$ 7,31 por m3
# residencia_social.py

consumo = input('digite o consumo em m3: ')

try:
    consumo = float(consumo)
    if consumo <= 10:
        print('R$7,59')
    elif consumo <= 20:
        print(f'R$1,31 por m3, conta: R${consumo * 1.31:.2f}')
    elif consumo <= 30:
        print(f'R$4,64 por m3, conta: R${consumo * 4.64:.2f}')
    elif consumo <= 50:
        print(f'R$6,62 por m3, conta: R${consumo * 6.62:.2f}')
    elif consumo > 50:
        print(f'R$7,31 por m3, conta: R${consumo * 7.31:.2f}')
except:
    print('por favor digite apenas numeros')