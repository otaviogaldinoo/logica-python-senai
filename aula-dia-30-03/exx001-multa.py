# 1. Desenvolva um programa que pergunte a velocidade do carro de um usuário. 
# Se a velocidade ultrapassar 80km/h, exiba uma mensagem dizendo que o usuário foi multado. 
# Nesse caso, exiba o valor da multa, cobrando R$ 50,00 por cada km acima de 80 km/h.
# Exemplo: Digite a velocidade em Km/h: 85
# Limite = 80Km/h
# Excedeu 5Km/h
# multa = 5Km/h * R$ 50,00
# Valor da multa: R$ 250,00
# Salvar o código como: multa.py

velocidade_carro = float(input('digite a velocidade do seu carro: '))
usuario_multado = False

if velocidade_carro > 80:
    usuario_multado = True
    print('usuário tomou multa')
    kms_acima_do_permitido = velocidade_carro - 80 
    valor_multa = kms_acima_do_permitido * 50.00
    print(f'limite de velocidade: 80km/h \nexcedeu: {kms_acima_do_permitido}km/h \nvalor da multa: R${valor_multa:.2f}')
else:
    print('usuário não tomou multa')