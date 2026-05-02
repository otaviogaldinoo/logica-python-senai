# 1. Um caixa eletrônico permite 3 tentativas para digitar a senha correta (4321). 
# Caso erre 3 vezes, a conta será bloqueada.

# Resultado Esperado:
# Se acertar exibir na tela 'acesso liberado'
# Se errar 3 vezes exibir na tela 'conta bloqueada'

senha_correta = '4321'
tentativa = 1
senha_digitada = ''

while senha_digitada != senha_correta:
    senha_digitada = input('digite a senha correta: ')
    tentativa += 1

    if tentativa > 3:
        print('conta bloqueada.')
        break
if senha_digitada == senha_correta:
    print('acesso liberado')