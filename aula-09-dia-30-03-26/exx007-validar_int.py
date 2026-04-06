# 7. Desenvolva um programa que receba um inteiro e exiba o mesmo na tela. Se o valor digitado for em branco exibir 'Dado inválido'
# Salvar o código como: validar_int.py

num = input("Digite um número inteiro: ")
try:
    num_int = int(num)
    print(f"O número digitado foi: {num_int}")
except:
    if num == "":
        print("Dado inválido")
