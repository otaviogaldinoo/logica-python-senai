# 3. O sistema de um caixa eletrônico de uma loja recebe produtos até digitar 0 para finalizar a compra. 
# Durante a compra: somar os valores do produtos
# Após ser finalizada: Exibir na tela o valor total da compra.

valor_final = 0 

while True:
    valor_produto = float(input('digite o valor do produto: R$'))
    valor_final += valor_produto

    resposta_usuario = input('digite 0 para finalizar a compra, ou digite enter para continuar comprando...\n')
    if resposta_usuario == '0':
        break
print(f'valor final: R$', valor_final) 