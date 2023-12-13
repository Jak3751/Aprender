
#Fazendo for dentro de for

pessoas = ['Gui', 'Rebeca']
adjs = ['Sapeca','Inteligente']

for p in pessoas:
    for a in adjs:
        print(f'{p} é {a}!')


#Fazendo um laço vazio
for i in [1, 2, 3]:
    pass                                                   #Se vc gerou uma herança e não definir uma classe, informar = pass


#Fazendo um laço com continue
for i in range(1, 11):
    if i % 2 == 1:                                        #Modulo 2 irá retonar sempre 0 se for par e 1 se for impar
        continue                                          #Irá entrar no continue sempre que a expressão for 1
    print(i, end=' ')                                     #Só irá imprimir o valor de i se for par


#Fazendo laço com break
for i in range(1, 11):
    if i ==5:
        break
    print(i)

print('Fim!')