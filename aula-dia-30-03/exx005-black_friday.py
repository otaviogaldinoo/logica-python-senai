# 5. Na última Black Friday, o gerente de uma loja de perfumes colocou todo o seu estoque em promoção, de acordo com a tabela a seguir:

# Código	Condição de Pagamento	Desconto (%)
# 1 	À vista (em espécie) 	10
# 2	Cartão de débito	5
# 3	Cartão de crédito	3
# 4	PIX			7.5

# Construa um programa que solicite ao operador do caixa o preço total da venda, bem como a forma de pagamento.
# Ao fim, o programa deve informar o valor final a ser pago.
# Salvar o código como: black_friday.py

produto = float(input("Digite o preço total da venda: "))
formato_pagamento = int(input("Digite a forma de pagamento (1 - À vista, 2 - Cartão de débito, 3 - Cartão de crédito, 4 - PIX): "))

if formato_pagamento == 1:
    desconto = produto * (10 / 100)
elif formato_pagamento == 2:
    desconto = produto * (5 / 100)
elif formato_pagamento == 3:
    desconto = produto * (3 / 100)
elif formato_pagamento == 4:
    desconto = produto * (7.5 / 100)

valor_final = produto - desconto
print(f"O valor final a ser pago é: R$ {valor_final:.2f}")          
