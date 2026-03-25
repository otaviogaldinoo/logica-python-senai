#  c) Calcular e apresentar o valor do volume de uma lata de óleo, utilizando a fórmula:
# #       VOLUME = 3.14159 * R ^ 2 * ALTURA.

raio = float(input("Digite o raio da lata de óleo: "))
altura = float(input("Digite a altura da lata de óleo: "))
volume = 3.14159 * (raio ** 2) * altura
print(f"O volume da lata de óleo é: {volume:.2f} unidades cúbicas.")
