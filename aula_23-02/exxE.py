# e) Efetuar o cálculo e apresentar o valor de uma prestação de um bem em atraso, utilizando a fórmula:
#      PRESTAÇÃO = VALOR + (VALOR * (TAXA / 100) * TEMPO).

VALOR = float(input("Digite o valor da prestação: "))
TAXA = float(input("Digite a taxa de juros (em %): "))
TEMPO = float(input("Digite o tempo de atraso (em meses): "))
PRESTACAO = VALOR + (VALOR * (TAXA / 100) * TEMPO)
print(f"O valor da prestação em atraso é: R$ {PRESTACAO:.2f}")
