# 4. Desenvolver um programa que leia um número de 1 a 7 e exiba o dia da semana:
#    1 - 'Domingo'
#    2 - 'Segunda'
#    3 - 'Terça'
#    4 - 'Quarta'
#    5 - 'Quinta'
#    6 - 'Sexta'
#    7 - 'Sábado'
# Qualquer outro numero exibir: 'Opção inválida!'

dia = int(input('digite um numero inteiro entre 1 a 7: '))

if dia == 1:
    print('domingo')
elif dia == 2:
    print('segunda')
elif dia == 3:
    print('terça')
elif dia == 4:
    print('quarta')
elif dia == 5:
    print('quinta')
elif dia == 6:
    print('sexta')
elif dia == 7:
    print('sabado')
else:
    print('por favor digite um numero entre 1 e 7')