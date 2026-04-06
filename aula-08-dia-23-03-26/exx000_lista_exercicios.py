# ********** ********** ** *******
# Exercícios Estruturas de Decisão I
# ********** ********** ** *******
# Obs.: m3 = metro(s) cúbico(s)

# 1. Desenvolver um programa que leia o consumo de água para uma residência social e exiba o valor (R$) da conta baseado nos seguintes cálculos:
# Se o consumo for menor ou igual a 10m3, então R$ 7,59
# Se o consumo for menor ou igual a 20m3, então R$ 1,31 por m3
# Se o consumo for menor ou igual a 30m3, então R$ 4,64 por m3
# Se o consumo for menor ou igual a 50m3, então R$ 6,62 por m3
# Se o consumo for acima dos 50m3, então R$ 7,31 por m3
# residencia_social.py

# consumo = int(input('digite o consumo em m3: '))

# if consumo <= 10:
#     print('R$7,59')
# elif consumo <= 20:
#     print(f'R$1,31 por m3, conta: R${consumo * 1.31:.2f}')
# elif consumo <= 30:
#     print(f'R$4,64 por m3, conta: R${consumo * 4.64:.2f}')
# elif consumo <= 50:
#     print(f'R$6,62 por m3, conta: R${consumo * 6.62:.2f}')
# elif consumo > 50:
#     print(f'R$7,31 por m3, conta: R${consumo * 7.31:.2f}')


    

# 2. Desenvolver um programa que leia o consumo de água para uma residência normal e exiba o valor (R$) da conta baseado nos seguintes cálculos:
# Se o consumo for menor ou igual a 10m3, então R$ 22,38
# Se o consumo for menor ou igual a 20m3, então R$ 3,50 por m3
# Se o consumo for menor ou igual a 50m3, então R$ 8,75 por m3
# Se o consumo for acima dos 50m3, então R$ 9,64 por m3
# residencia_normal.py


# 3. Desenvolver um programa que leia o consumo de água para prédios comerciais e industriais e exiba o valor (R$) da conta baseado nos seguintes cálculos:
# Se o consumo for menor ou igual a 10m3, então R$ 44,95
# Se o consumo for menor ou igual a 20m3, então R$ 8,75 por m3
# Se o consumo for menor ou igual a 50m3, então R$ 16,76 por m3
# Se o consumo for acima dos 50m3, então R$ 17,46 por m3
# comercio_industria.py

# ******************************
# fonte dos exercícios 1,2 e 3: 
# https://gujsp.com.br/apos-fim-de-multa-na-conta-sabesp-sobe-tarifa-da-agua-e-esgoto-em-84/#:~:text=Com%20o%20reajuste%2C%20o%20cliente,8%2C75%20o%20metro%20c%C3%BAbico.
# ******************************

# 4. Desenvolver um programa que leia um número de 1 a 7 e exiba o dia da semana:
#    1 - 'Domingo'
#    2 - 'Segunda'
#    3 - 'Terça'
#    4 - 'Quarta'
#    5 - 'Quinta'
#    6 - 'Sexta'
#    7 - 'Sábado'
# Qualquer outro numero exibir: 'Opção inválida!'

# 5. Desenvolver um programa que leia o peso e a altura de uma pessoa e calcule seu imc utilizando a fórmula: imc = peso / altura * altura
# Com o imc exiba para o usuário seu imc e a classificação:
# IMC		Classificação
# < 16		'Magreza grave'
# 16 a < 17	'Magreza moderada'
# 17 a < 18,5	'Magreza leve'
# 18,5 a < 25	'Saudável'
# 25 a < 30	'Sobrepeso'
# 30 a < 35	'Obesidade Grau I'
# 35 a < 40	'Obesidade Grau II (severa)'
# ≥ 40		'Obesidade Grau III (mórbida)'

# 6. Desenvolva um programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem formam um triângulo e se formarem exibir na tela se é equilátero, isósceles ou escaleno.

# Sabemos que:
# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes;

# 7. Desenvolva um programa que exiba na tela um menu de opções:

#    1 - Opção 1
#    2 - Opção 2
#    3 - Opção 3
#    4 - Sair
#    Digite uma opção: 
# Se o usuário digitar 1, exibir na tela: 'Você selecionou a opção 1'
# Se o usuário digitar 2, exibir na tela: 'Você selecionou a opção 2'
# Se o usuário digitar 3, exibir na tela: 'Você selecionou a opção 3'
# Se o usuário digitar 4, exibir na tela: 'Você selecionou sair'
# Se o usuário digitar uma opção diferente das apresentadas no menu, exibir 'Opção inválida!!!'
# Exibir no final do processamento 'Fim do programa!'

# 8. Desenvolva um calculadora que receba dois números e efetue uma das seguintes operações aritméticas:

#    1 - Adição
#    2 - Subtração
#    3 - Multiplicação
#    4 - Divisão
#    5 - Potência
#    6 - Raiz quadrada
#    7 - Número par
#    8 - Número ímpar

# 9 - Desenvolva um programa que leia o valor (R$) de um salário qualquer e calcule e exiba o desconto com IRRF e INSS;
# fonte: https://impostoderenda2023.com.br/tabela-do-imposto-de-renda-2023/

# 10 - Desenvolva um programa que pergunte em que turno você estuda. 
# Peça para digitar: M-Matutino ou V-Vespertino ou N- Noturno. 
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
# Obs.: Somente letras maiúsculas para M, V ou N.

# 11 - Desenvolva um programa que recebe o salário de um funcionário e determine o reajuste segundo o seguinte critério, baseado no salário atual:
#   salários até R$ 1000,00 (incluindo)     : aumento de 20%
#   salários até R$ 1.700,00                : aumento de 15%
#   salários até R$ 2.300,00                : aumento de 10%
#   salários acima de R$ 2.300,00 em diante : aumento de 5%

# Após o processamento exibir na tela:
#   o salário antes do reajuste;
#   o percentual de aumento aplicado;
#   o valor do aumento;
#   o novo salário, após o aumento.

# Exemplo:
# Salário digitado: R$ 1.900,00
# Aumento         : 10%
# Valor do aumento: R$ 190,00
# Novo salário    : R$ 2.090,00

# 12. Desenvolva um programa que leia quatro notas bimestrais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média final. A atribuição de conceitos obedece à tabela abaixo:
#   Média de Aproveitamento  Conceito
#   Entre 9.0 e 10.0        A
#   Entre 7.5 e 8.9         B
#   Entre 6.0 e 7.4         C
#   Entre 4.0 e 5.9         D
#   Entre zero e 3.9        E
# O programa deve exibir na tela:
#   1. As quatro notas bimestrais,
#   2. A média final,
#   3. O conceito correspondente e,
#   4. A mensagem "APROVADO" ou "Reprovado" de acordo com a regra a seguir:
#      4.1. Se o conceito       for A, B ou C    exibir "APROVADO"
#      4.2. Senão se o conceito for D ou E       exibir "REPROVADO"
