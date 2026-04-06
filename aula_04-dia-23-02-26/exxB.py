# b) Ler uma temperatura em graus Fahrenheit e apresentá-la convertida em graus Celsius. A fórmula de conversão é:
#       C = ((F – 32) * 5) / 9,
# sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.

temperatura_fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
temperatura_celsius = ((temperatura_fahrenheit - 32) * 5) / 9
print(f"A temperatura em Celsius é: {temperatura_celsius:.2f} °C")