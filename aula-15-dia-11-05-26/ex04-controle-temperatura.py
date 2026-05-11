# Exercício 4 - Controle de temperaturas
#      Solicite temperaturas em graus Celsius até o usuário digitar "sair";
#      Converta as temperaturas da lista em graus Celsius para uma nova lista de temperaturas em graus Fahrenheit;
#      Calcule e exiba as médias de ambas as temperaturas.

temperaturas_celsius = []
while True:
    temperatura = input("Digite uma temperatura em graus Celsius (ou 'sair' para encerrar): ")
    if temperatura.lower() == "sair":
        break
    try:
        temperaturas_celsius.append(float(temperatura))
    except ValueError:
        print("Por favor, digite um número válido ou 'sair' para encerrar.")
temperaturas_fahrenheit = [(temp * 9/5) + 32 for temp in temperaturas_celsius]
media_celsius = sum(temperaturas_celsius) / len(temperaturas_celsius)
media_fahrenheit = sum(temperaturas_fahrenheit) / len(temperaturas_fahrenheit)
print(f"Temperaturas em Celsius: {temperaturas_celsius}")
print(f"Temperaturas em Fahrenheit: {temperaturas_fahrenheit}")
print(f"Média das temperaturas em Celsius: {media_celsius:.2f}°C")
print(f"Média das temperaturas em Fahrenheit: {media_fahrenheit:.2f}°F")