# 6. Ler dez votos e exibir na tela o resultado da eleição para os seguintes candidatos: 

# 1 = João
# 2 = Maria
# outro = nulo

# Exibir na tela quem venceu a eleição.

votos_joao = 0
votos_maria = 0
votos_outros = 0
contagem_votos = 1

while contagem_votos <= 10:
    print('-'*15)
    voto_digitado = input(f'rodada {contagem_votos}\ndigite 1 para votar no João,\ndigite 2 para votar na Maria,\ndigite 3 se o seu voto for nulo:\n')
    if voto_digitado == '1':
        votos_joao += 1
    elif voto_digitado == '2':
        votos_maria += 1
    elif voto_digitado == '3':
        votos_outros += 1
    else:
        print('>>>voto inválido<<<')
    contagem_votos += 1
print('-'*15)
print(f'> João recebeu {votos_joao} votos,\n> Maria recebeu {votos_maria},\n> votos nulos: {votos_outros}')
if votos_joao > votos_maria and votos_joao > votos_outros:
    print('---Jõao venceu eleição!---')
elif votos_maria > votos_joao and votos_maria > votos_outros:
    print('---Maria venceu eleição!---')
elif votos_joao == votos_maria:
    print('---Jõao e Maria empataram a eleição---')
