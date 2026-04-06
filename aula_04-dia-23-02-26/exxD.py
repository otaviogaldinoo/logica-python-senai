# d) Efetuar o cálculo da quantidade de litros de combustível gasta em uma viagem, utilizando um automóvel que faz 12 quilômetros por litro. Para obter o cálculo, o usuário deve
# fornecer o tempo gasto (variável TEMPO) e a velocidade média (variável VELOCIDADE) durante a viagem. Dessa forma, será possível obter a distância percorrida com a fórmula DISTÂNCIA = TEMPO * VELOCIDADE. A partir do valor da distância, basta calcular a quantidade de litros de
# combustível utilizada na viagem com a fórmula LITROS_USADOS = DISTÂNCIA / 12. O programa deve
# apresentar os valores da velocidade média, tempo gasto na viagem, a distância percorrida e a quantidade de litros utilizada na viagem.

tempo = float(input("Digite o tempo gasto na viagem (em horas): "))
velocidade = float(input("Digite a velocidade média durante a viagem (em km/h): "))
distancia = tempo * velocidade
litros_usados = distancia / 12
print(f"Velocidade média: {velocidade} km/h")
print(f"Tempo gasto na viagem: {tempo} horas")
print(f"Distância percorrida: {distancia} km")
print(f"Quantidade de litros utilizada na viagem: {litros_usados} litros")
