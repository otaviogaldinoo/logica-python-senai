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

salario = float(input("Digite o salário do funcionário: R$ "))
if salario <= 1000:
    percentual_aumento = 20
elif salario <= 1700:
    percentual_aumento = 15
elif salario <= 2300:
    percentual_aumento = 10
else:
    percentual_aumento = 5
valor_aumento = salario * percentual_aumento / 100
novo_salario = salario + valor_aumento
print(f"Salário antes do reajuste: R$ {salario:.2f}")
print(f"Percentual de aumento aplicado: {percentual_aumento}%")
print(f"Valor do aumento: R$ {valor_aumento:.2f}")
print(f"Novo salário, após o aumento: R$ {novo_salario:.2f}")

