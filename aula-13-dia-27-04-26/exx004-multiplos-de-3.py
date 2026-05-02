# 4. Somar e exibir todos os múltiplos de 3 entre 1 e 100.

contagem = 1
soma = 0

while contagem <= 100:
    numero = contagem 
    if numero % 3 == 0:
        print(numero)
        soma += numero
    contagem += 1

print(f'soma final = {soma}')