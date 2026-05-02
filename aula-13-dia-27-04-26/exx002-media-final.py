# 2. Peça 4 notas (nota1, nota2, nota3, nota4) de  4 alunos (aluno1, aluno2, aluno3, aluno4), calcule a média final (mf) de cada um e exiba na tela a sua situação escolar:

# Média final >= 7 → Aprovado
# Média final entre 5 e 6.9 → Recuperação
# Média final < 5 → Reprovado

aluno1_nota1 = float(input('digite nota 1 do aluno 1: '))
aluno1_nota2 = float(input('digite nota 2 do aluno 1: '))
aluno1_nota3 = float(input('digite nota 3 do aluno 1: '))
aluno1_nota4 = float(input('digite nota 4 do aluno 1: '))

media_final_aluno1 = (aluno1_nota1 + aluno1_nota2 + aluno1_nota3 + aluno1_nota4) / 4
print(media_final_aluno1)
if media_final_aluno1 >= 7:
    print('aprovado')
elif media_final_aluno1 >= 5 and media_final_aluno1 <= 6.9:
    print('recuperação')
elif media_final_aluno1 < 5:
    print('reprovado')
print('-'*30)
# ------------------------------------------------------------------
aluno2_nota1 = float(input('digite nota 1 do aluno 2: '))
aluno2_nota2 = float(input('digite nota 2 do aluno 2: '))
aluno2_nota3 = float(input('digite nota 3 do aluno 2: '))
aluno2_nota4 = float(input('digite nota 4 do aluno 2: '))

media_final_aluno2 = (aluno2_nota1 + aluno2_nota2 + aluno2_nota3 + aluno2_nota4) / 4
print(media_final_aluno2)
if media_final_aluno2 >= 7:
    print('aprovado')
elif media_final_aluno2 >= 5 and media_final_aluno2 <= 6.9:
    print('recuperação')
elif media_final_aluno2 < 5:
    print('reprovado')
print('-'*30)
# ---------------------------------------------------------
aluno3_nota1 = float(input('digite nota 1 do aluno 3: '))
aluno3_nota2 = float(input('digite nota 2 do aluno 3: '))
aluno3_nota3 = float(input('digite nota 3 do aluno 3: '))
aluno3_nota4 = float(input('digite nota 4 do aluno 3: '))

media_final_aluno3 = (aluno3_nota1 + aluno3_nota2 + aluno3_nota3 + aluno3_nota4) / 4
print(media_final_aluno3)
if media_final_aluno3 >= 7:
    print('aprovado')
elif media_final_aluno3 >= 5 and media_final_aluno3 <= 6.9:
    print('recuperação')
elif media_final_aluno3 < 5:
    print('reprovado')
print('-'*30)
# ------------------------------------------------------------
aluno4_nota1 = float(input('digite nota 1 do aluno 4: '))
aluno4_nota2 = float(input('digite nota 2 do aluno 4: '))
aluno4_nota3 = float(input('digite nota 3 do aluno 4: '))
aluno4_nota4 = float(input('digite nota 4 do aluno 4: '))

media_final_aluno4 = (aluno4_nota1 + aluno4_nota2 + aluno4_nota3 + aluno4_nota4) / 4
print(media_final_aluno4)
if media_final_aluno4 >= 7:
    print('aprovado')
elif media_final_aluno4 >= 5 and media_final_aluno4 <= 6.9:
    print('recuperação')
elif media_final_aluno4 < 5:
    print('reprovado')
print('-'*30)
