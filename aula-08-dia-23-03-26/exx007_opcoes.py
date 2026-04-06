# 7. Desenvolva um programa que exiba na tela um menu de opções:

#    1 - Opção 1
#    2 - Opção 2
#    3 - Opção 3
#    4 - Sair
#    Digite uma opção: 
# Se o usuário digitar 1, exibir na tela: 'Você selecionou a opção 1'
# Se o usuário digitar 2, exibir na tela: 'Você selecionou a opção 2'
# Se o usuário digitar 3, exibir na tela: 'Você selecionou a opção 3'
# Se o usuário digitar 4, exibir na tela: 'Você selecionou sair'
# Se o usuário digitar uma opção diferente das apresentadas no menu, exibir 'Opção inválida!!!'
# Exibir no final do processamento 'Fim do programa!'´

opcao = int(input('1 - Opção 1\n2 - Opção 2 \n3 - Opção 3 \n4 - Sair \nDigite uma opção: '))

if opcao == 1:
    print('Você selecionou a opção 1')
elif opcao == 2:
    print('Você selecionou a opção 2')
elif opcao == 3:
    print('Você selecionou a opção 3')
elif opcao == 4:
    print('Você selecionou sair')
else:
    print("opção inválida")
print('fim do programa')