# 3. Desenvolva um programa que pergunte a distância que um passageiro deseja percorrer em km.
# Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e R$
# 0,45 para viagens mais longas.
# Salvar o código como: viagens.py

distancia_em_km = float(input('digite a distância em km: '))
valor_passagem = 0
preco_km = 0

if distancia_em_km < 200:
    preco_km = 0.50
    valor_passagem = distancia_em_km * preco_km
    print(f'distância da sua viagem: {distancia_em_km}km \nvalor da passagem: R${valor_passagem}')

elif distancia_em_km > 200:
    preco_km = 0.45
    valor_passagem = distancia_em_km * preco_km
    print(f'distância da sua viagem: {distancia_em_km}km \nvalor da passagem: R${valor_passagem}')