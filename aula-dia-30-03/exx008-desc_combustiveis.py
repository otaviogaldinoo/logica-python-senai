# 8. Um posto está vendendo combustíveis com a seguinte tabela de descontos: 
#    Álcool:
#       até 20 litros, desconto de 3% por litro
#       acima de 20 litros, desconto de 5% por litro 
#    Gasolina:
#       até 20 litros, desconto de 4% por litro
#       acima de 20 litros, desconto de 6% por litro 

# O programa deverá ler o número de litros vendidos, o tipo de combustível codificado da seguinte forma: 
#    A - Álcool, 
#    G - Gasolina, 
# Calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 4,95 o preço do litro do álcool é R$ 2,89.
# Salvar o código como: desc_combustiveis.py

preco_alcool = 2.89
preco_gasolina = 4.95

litros = float(input("Digite a quantidade de litros abastecido: "))
combustivel = input("Digite o tipo de combustível (A para Álcool, G para Gasolina): ").upper()

if combustivel == 'A':
    if litros <= 20:
        desconto = (3 / 100)
    else:
        desconto = (5 / 100)
    valor_total = litros * preco_alcool * (1 - desconto)
    print(f'combustível: Álcool')
    print(f'litros: {litros}')
    print(f'desconto: {desconto * 100:.0f}%')
    print(f'valor total: R$ {valor_total:.2f}')
elif combustivel == 'G':
    if litros <= 20:
        desconto = (4 / 100)
    else:
        desconto = (6 / 100)
    valor_total = litros * preco_gasolina * (1 - desconto)
    print(f'combustível: Gasolina')
    print(f'litros: {litros}')
    print(f'desconto: {desconto * 100:.0f}%')
    print(f'valor total: R$ {valor_total:.2f}')