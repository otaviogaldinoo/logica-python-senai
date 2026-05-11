# Exercício 1 — Lista de convidados
# Crie um programa que:
#      Cadastre 5 convidados;
#      Exiba todos os convidados;
#      Informe quantos convidados existem.

convidados = []
for i in range(5):
    nome = input(f'digite o nome do convidado {i +1}: ')
    convidados.append(nome)

print('------------ \nLista de convidados:')
for convidado in convidados:
    print(convidado)
print(f'Número total de convidados: {len(convidados)}')