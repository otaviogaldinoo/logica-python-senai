# 10 - Desenvolva um programa que pergunte em que turno você estuda. 
# Peça para digitar: M-Matutino ou V-Vespertino ou N- Noturno. 
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
# Obs.: Somente letras maiúsculas para M, V ou N.

turno = input("Digite o turno que você estuda (M-Matutino, V-Vespertino ou N-Noturno): ")

if turno == "M":
    print("Bom Dia!")
elif turno == "V":
    print("Boa Tarde!")
elif turno == "N":
    print("Boa Noite!")
else:
    print("Valor Inválido!")