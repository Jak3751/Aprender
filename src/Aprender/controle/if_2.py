a = 'valor'  # Existe!!!
a = 0  # não existe ou zero ou vazio ...
a = -0.00001  # Existe!!!
a = ''  # não existe ou zero ou vazio ...
a = ' '  # Existe!!!
a = []  # não existe ou zero ou vazio ... Lista
a = {}  # não existe ou zero ou vazio ... Conjunto


if a:
    print('Existe!!!!')
else:
    print('não existe ou zero ou vazio ...')


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
nota = float(input('Informe a nota do aluno: '))
comportado = True if input('Comportado? (y/n): ') == 'y' else False

if nota >= 9 and comportado:
    print('Duas palavras: para bens! :p')
    print('Quadro de honra')
elif nota >= 7:
    print('Aprovado')
elif nota >= 5.5:
    print('Recuperação')
elif nota >= 3.5:
    print('Recuperação + Trabalho')
else:
    print('Reprovado')

print(nota)
