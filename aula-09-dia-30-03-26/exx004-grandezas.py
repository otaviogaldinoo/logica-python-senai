# 4. Uma empresa, que presta serviço à companhia de energia elétrica do estado, necessita de um programa que auxilie os seus eletricistas no cálculo das principais grandezas da Eletricidade
# que são Tensão, Resistência e Corrente. Sabe-se que:
# U = R * I, 


# Você foi contratado(a) pela empresa para atender a essa solicitação.
# Construa um programa que apresente o seguinte menu:

# ******************************
# CÁLCULO DE GRANDEZAS ELÉTRICAS
# ******************************
# 1. Tensão (em Volt)
# 2. Resistência (em Ohm)
# 3. Corrente (em Ampére)
# 4. Sair do programa
# ******************************
# Qual grandeza deseja calcular?

# Em seguida, o programa deve solicitar que o eletricista informe o valor das outras duas grandezas para realizar o cálculo.

# Quando o eletricista escolher:
# 1. Tensão, o programa deve solicitar que ele informe os valores da Resistência e da Corrente.
#    Utilizar a fórmula: U = R * I

# 2. Resistência, o programa deve solicitar que ele informe os valores da Tensão e da Corrente.
#    Utilizar a fórmula: R = U / I

# 3. Corrente, o programa deve solicitar que ele informe os valores da Tensão e da Resistência.
#    Utilizar a fórmula: I = U / R

# onde, 
# U é a Tensão      (em V), 
# R é a Resistência (em Ώ) e,
# I é a Corrente    (em A).

# Por fim, o programa deve calcular e apresentar o valor encontrado para a grandeza escolhida.
# Obs.: Qualquer opção diferente das apresentadas no menu (1 a 4) deverão ser informadas ao usuário como 'Opção inválida!'
# Salvar o código como: grandezas.py

opcao_digitada = input('******************************\nCÁLCULO DE GRANDEZAS ELÉTRICAS\n******************************\n1. Tensão (em Volt)\n2. Resistência (em Ohm)\n3. Corrente (em Ampére)\n4. Sair do programa\n******************************\nQual grandeza deseja calcular?: ')

tensao = 0
resistencia = 0
corrente = 0

if opcao_digitada == '1':
    resistencia = float(input('digite o valor da reistência: '))
    corrente = float(input('digite o valor da corrente: '))
    tensao = resistencia * corrente
    print(f'tensão = {tensao}Volt')
elif opcao_digitada == '2':
    tensao = float(input('digite o valor da tensão: '))
    corrente = float(input('digite o valor da corrente: '))
    resistencia = tensao / corrente
    print(f'resistencia = {resistencia}Ohm')
elif opcao_digitada == '3':
    tensao = float(input('digite o valor da tensão: '))
    resistencia = float(input('digite o valor da reistência: '))
    corrente = tensao / resistencia
    print(f'corrente = {corrente}Ampere')
elif opcao_digitada == '4':
    print('programa finalizado')
else:
    print('opção inválida')