x = 0


while x != -1:                                             #Diferente do for, quando utilizamos while, ele irá repetir até que a expressão seja verdadeira
    x = float(input('Informe o numero ou -1 para sair: '))

print('Fim!')




#- - - - - - - - - - - -- #
total = 0.0
qtde = 0
nota = 0

while nota != -1:
    nota = float(input('Informe a nota ou digite -1 para sair: '))
    if nota != -1:
        qtde += 1
        total += nota
        media = total / qtde

print(f'A média da turma é: {media}')


#- - - - - - - - - - - - - #
x = 10

while x:
    print(x)
    x -= 1
print('Fim!')