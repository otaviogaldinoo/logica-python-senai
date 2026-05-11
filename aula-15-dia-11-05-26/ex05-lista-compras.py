# Exercício 5: Lista de compras
#      Exibir um menu de opções para esta lista de compras: 

#              1 - Adicionar a lista 
#              2 - Pesquisar item 
#              3 - Remover item
#              4 - Alterar item
#              5 - Listar produtos
#              6 - Sair


lista_compras = []

while True:
    print('---------\nmenu de compras: ')
    print('1 - Adicionar a lista')
    print('2 - Pesquisar item')
    print('3 - Remover item')
    print('4 - Alterar item')
    print('5 - Listar produtos')
    print('6 - Sair')

    resposta_usuario = input('')
    if resposta_usuario == '1':
        adicionar_item = input('digite o item a ser adicionado: ')
        lista_compras.append(adicionar_item)
        print(f'{adicionar_item} adicionado a lista de compras.')
    elif resposta_usuario == '2':
        pesquisar_item = input('digite o item a ser pesquisado: ')
        if pesquisar_item in lista_compras:
            print(f'{pesquisar_item} consta na lista de compras')
        else:
            print(f'{pesquisar_item} NÂO consta na lista de compras')
    elif resposta_usuario == '3':
        print(lista_compras)
        remover_item = input('digite o item a ser removido: ')
        if remover_item in lista_compras:
            lista_compras.remove(remover_item)
            print(f'{remover_item} removido da lista de compras')
        else:
            print(f'{remover_item} não pode ser removido pois não consta na lista de compras')
    elif resposta_usuario == '4':
        print(lista_compras)
        alterar_item = input('qual item deseja alterar?: ')
        if alterar_item in lista_compras:
            lista_compras.remove(alterar_item)
            print(f'{alterar_item} removido, qual item deseja colocar no lugar?: ' )
            alterar_item = input('')
            lista_compras.append(alterar_item)
            print(f'{alterar_item} adicionado na lsta')
        else: 
            print(f'{alterar_item} não consta na lista')
    elif resposta_usuario == '5':
        print('lista de produtos: ')
        print(lista_compras)
    elif resposta_usuario == '6':
        print('programa finalizado.')
        break
    else:
        print('opção inválida.')