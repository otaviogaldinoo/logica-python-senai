# Exercício 2 — Controle de preços
#      Solicite 5 preços e:
#      armazene em uma lista;
#      exiba o maior preço;
#      exiba o menor preço.

precos = []
for i in range(5):
    preco = input(f"Digite o preço {i + 1}: ")
    try:
        preco = float(preco)
        precos.append(preco)
    except ValueError:
        print("valor inválido.")
        continue
    

print(f"O maior preço é: R${max(precos)}")
print(f"O menor preço é: R${min(precos)}")
