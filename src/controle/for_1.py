for i in range(10):  # Irá mostrar de 0 até 9
    print(i)

for i in range(1, 11):  # Irá mostrar de 1 até 10
    print(i)

for i in range(1, 100, 7):  # Irá mostrar de 1 até 100 em 7 em 7.
    print(i)

for i in range(20, 0, -3):  # Irá mostrar de 20 até 0 em 3 em 3.
    print(i)

nums = [2, 4, 6, 8]

for n in nums:
    # Usado end=',' para mostrar o resultado em 1 unica linha separados por virgula
    print(n, end=',')

texto = 'Python é muito massa!'

for letra in texto:
    print(letra, end=' ')
    print('')


for n in {1, 2, 3, 4, 4, 4}:
    print(n, end=' ')
    print('')

produto = {  # Percorrer uma lista, dicionario
    'nome': 'Caneta',
    'preco': 8.80,
    'desc': 0.5
}

for atrib in produto:
    print(atrib, '>>', produto[atrib])
    print('')

for atrib, valor in produto.items():
    print(atrib, '>>', valor)
    print('')

for atrib in produto.keys():
    print(atrib, end=' ')
    print('')
