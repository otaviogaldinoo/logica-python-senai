# 7. Desenvolver um aplicativo para um caixa eletrônico com saldo inicial de R$ 500,00 com as seguintes opções:

# 1 Saque
# 2 Depósito
# 3 Saldo
# 0 Sair

# Repetir até sair.

# Regras do negócio:
#   Não sacar valor maior que saldo
#   Valor inválido não permitido

saldo = 500.00
valor_saque = 0
valor_deposito = 0

while True:
    print('-'*20)
    resposta_usuario = input(f'| digite 1 para sacar\n| digite 2 para depósito\n| digite 3 para ver o saldo disponível\n| digite 0 para sair \n: ')
    if resposta_usuario == '1':
        valor_saque = input('digite o valor a ser sacado: R$')
        try:
            valor_saque = float(valor_saque)
            if valor_saque > saldo:
                print(f'você não pode sacar um valor maior do que o saldo disponível: R${saldo}')
            elif valor_saque <= saldo:
                saldo -= valor_saque
                print(f'> você sacou R${valor_saque}, saldo disponível: R${saldo}')
        except ValueError:
            print('valor inválido')
    elif resposta_usuario == '2':
        valor_deposito = input('digite o valor a ser depositado: R$')
        try:
            valor_deposito = float(valor_deposito)
            saldo += valor_deposito
            print(f'você depositou R${valor_deposito}, saldo disponível: R${saldo}')
        except ValueError:
            print('valor inválido')
    elif resposta_usuario == '3':
        print(f'saldo disponível: R${saldo}')
    elif resposta_usuario == '0':
        print('caixa eletrônico finalizado.')
        break
    else:
        print('opção inválida')