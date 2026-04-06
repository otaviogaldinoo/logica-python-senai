# 3. Desenvolver um programa que leia o consumo de água para prédios comerciais e industriais e exiba o valor (R$) da conta baseado nos seguintes cálculos:
# Se o consumo for menor ou igual a 10m3, então R$ 44,95
# Se o consumo for menor ou igual a 20m3, então R$ 8,75 por m3
# Se o consumo for menor ou igual a 50m3, então R$ 16,76 por m3
# Se o consumo for acima dos 50m3, então R$ 17,46 por m3
# comercio_industria.py

consumo = float(input('digite o consumo em m3: '))

if consumo <= 10:
    print('conta: R$44,95')
elif consumo <= 20:
    print(f'R$8,75 por m3, conta: R${consumo * 8.75}')
elif consumo <= 50:
    print(f'R$16,76 por m3, conta: R${consumo * 16.76}')
elif consumo > 50:
    print(f'R$17,46 por m3, conta: R${consumo * 17.46}')