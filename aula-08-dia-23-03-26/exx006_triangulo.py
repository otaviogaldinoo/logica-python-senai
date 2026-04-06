# 6. Desenvolva um programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem formam um triângulo e se formarem exibir na tela se é equilátero, isósceles ou escaleno.

# Sabemos que:
# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes;

lado1 = float(input('digite o valor do primeiro lado do triangulo: '))
lado2 = float(input('digite o valor do segudno lado do triangulo: '))
lado3 = float(input('digite o valor do terceiro lado do triangulo: '))

if lado1 == lado2 and lado2 == lado3 and lado1 == lado3:
    print('Triângulo Equilátero')
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print('Triângulo Isósceles')
elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
    print('Triângulo Escaleno')
else:
    print('por algum motivo deu erro')