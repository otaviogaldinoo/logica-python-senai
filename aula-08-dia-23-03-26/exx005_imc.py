# 5. Desenvolver um programa que leia o peso e a altura de uma pessoa e calcule seu imc utilizando a fórmula: 
# imc = peso / (altura * altura)
# Com o imc exiba para o usuário seu imc e a classificação:
# IMC		Classificação
# < 16		'Magreza grave' --
# 16 a < 17	'Magreza moderada' --
# 17 a < 18,5	'Magreza leve' --
# 18,5 a < 25	'Saudável' --
# 25 a < 30	'Sobrepeso' --
# 30 a < 35	'Obesidade Grau I' --
# 35 a < 40	'Obesidade Grau II (severa)' --
# ≥ 40		'Obesidade Grau III (mórbida)'

peso = float(input('digite seu peso em kg: '))
altura = float(input('digite sua altura: '))

imc = peso / altura ^ 2

if imc < 16:
    print('magreza grave')
elif imc >= 16 and imc < 17:
    print('magreza moderada')
elif imc >= 17 and imc < 18.5:
    print('magreza leve')
elif imc >= 18.5 and imc < 25:
    print('saudável')
elif imc >= 25 and imc < 30:
    print('sobrepeso')
elif imc >= 30 and imc < 35:
    print('obesidade grau 1')
elif imc >= 35 and imc < 40:
    print('obesidade grau 2 (severa)')
elif imc > 40:
    print('obesidade grau 3 (mórbida)')
else:
    print('por algum motivo deu erro')