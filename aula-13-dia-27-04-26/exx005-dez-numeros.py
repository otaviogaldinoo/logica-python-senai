# 5. Ler dez números e exibir na tela:
#    a soma destes números;
#    o maior número lido;
#    o menor número lido;
#    a soma de todos os números pares lidos;
#    a soma de todos os números ímpares lidos;
#    o número de ímpares;
#    o número de pares.
#    a média destes números;


soma_total = 0
media = 0
maior_numero = 0
menor_numero = 0
soma_numeros_pares = 0
soma_numeros_impares = 0
total_de_numeros_impares = 0
total_de_numeros_pares = 0

for i in range(1, 11):
    try:
        numero_digitado = int(input(f'digite o {i}° número inteiro: '))
        soma_total += numero_digitado
        if numero_digitado > maior_numero:
            maior_numero = numero_digitado
        if i == 1:
            menor_numero = numero_digitado
        if numero_digitado < menor_numero:
            menor_numero = numero_digitado
        if numero_digitado % 2 == 0:
            soma_numeros_pares += numero_digitado
            total_de_numeros_pares += 1
        else:
            soma_numeros_impares += numero_digitado
            total_de_numeros_impares += 1
    except:
        print('valor inválido')
        break

media = soma_total / 10

print(f'a soma de todos os números digitados é: {soma_total}, \no maior número lido é: {maior_numero}, \no menor número lido é {menor_numero}, \nsomando apenas os numeros pares: {soma_numeros_pares}, \nsomando apenas números ímpares: {soma_numeros_impares}, \nforam digitados {total_de_numeros_impares} números ímpares,\nforam digitados {total_de_numeros_pares} números pares, \na média é {media}')