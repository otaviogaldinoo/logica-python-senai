# Exercício 3 — Lista de tarefas
#      Crie um programa que:
#      permita cadastrar tarefas;
#      finalize quando o usuário digitar “fim”;
#     #  exiba todas as tarefas.

tarefas = []

while True:
    tarefa = input('digite a sua próxima tarefa ou digite "fim" para finalizar o programa: ')
    tarefa = tarefa.lower()
    if tarefa == 'fim':
        print('programa finalizado.')
        break
    else:
        tarefas.append(tarefa)
print(f'--------------\nlista de tarefas:\n{tarefas}')