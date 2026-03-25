# 9 - Desenvolva um programa que leia o valor (R$) de um salário qualquer e calcule e exiba o desconto com IRRF e INSS;
# fonte: https://impostoderenda2023.com.br/tabela-do-imposto-de-renda-2023/

salario = float(input('Digite o valor do salário: R$ '))
if salario <= 1903.98:
    print('Isento de IRRF')
elif salario <= 2826.65:
    desconto_irrf = salario * 0.075 - 142.80
    print(f'Desconto IRRF: R$ {desconto_irrf:.2f}')
elif salario <= 3751.05:
    desconto_irrf = salario * 0.15 - 354.80
    print(f'Desconto IRRF: R$ {desconto_irrf:.2f}')
elif salario <= 4664.68:
    desconto_irrf = salario * 0.225 - 636.13
    print(f'Desconto IRRF: R$ {desconto_irrf:.2f}')
else:
    desconto_irrf = salario * 0.275 - 869.36
    print(f'Desconto IRRF: R$ {desconto_irrf:.2f}')