nota = float(input('Informe a nota do aluno: '))

if nota >= 9:  # Se a nota informada for maior ou igual a 9, irá executar o bloco abaixo
    print('Duas palavras: para bens! :P')
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
