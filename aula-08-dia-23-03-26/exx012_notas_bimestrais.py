# 12. Desenvolva um programa que leia quatro notas bimestrais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média final. A atribuição de conceitos obedece à tabela abaixo:
#   Média de Aproveitamento  Conceito
#   Entre 9.0 e 10.0        A
#   Entre 7.5 e 8.9         B
#   Entre 6.0 e 7.4         C
#   Entre 4.0 e 5.9         D
#   Entre zero e 3.9        E
# O programa deve exibir na tela:
#   1. As quatro notas bimestrais,
#   2. A média final,
#   3. O conceito correspondente e,
#   4. A mensagem "APROVADO" ou "Reprovado" de acordo com a regra a seguir:
#      4.1. Se o conceito       for A, B ou C    exibir "APROVADO"
#      4.2. Senão se o conceito for D ou E       exibir "REPROVADO"

nota = float(input('Digite a nota do 1º bimestre: '))
nota2 = float(input('Digite a nota do 2º bimestre: '))
nota3 = float(input('Digite a nota do 3º bimestre: '))
nota4 = float(input('Digite a nota do 4º bimestre: '))
media = (nota + nota2 + nota3 + nota4) / 4

if media >= 9.0:
    conceito = 'A'
elif media >= 7.5:
    conceito = 'B'
elif media >= 6.0:
    conceito = 'C'
elif media >= 4.0:
    conceito = 'D'
else:
    conceito = 'E'

if conceito == 'A' or conceito == 'B' or conceito == 'C':
    mensagem = 'APROVADO'
else:
    mensagem = 'REPROVADO'

print(f'Notas bimestrais: {nota}, {nota2}, {nota3}, {nota4}')
print(f'Média final: {media:.2f}')
print(f'Conceito correspondente: {conceito}')
print(f'Mensagem: {mensagem}')