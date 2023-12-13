nomes = ('Ana', 'Bia','Gui', 'Ana')                #Na tuple, os valores são indexados, posso fazer pesquisa direto pelo indice que desejo
print(type(nomes))
print(nomes)

print('bia' in nomes)                              #Irá buscar pelo nome 'bia' na variavel 'nomes', resultado será 'false' pois esta com letra minuscula
print(nomes[0])                                    #irá trazer o primeiro nome da lista
print(nomes[1:2])                                  #Irá acessar até o segundo nome da lista, porém irá trazer somente o primeiro
print(nomes[:-1])                                  #Irá trazer todos os nomes, menos o ultimo elemento
x = ('Bia',)
print(type(x))                                     #Type do x é tuple, pois tem a ',' depois do nome, se não tivesse, seria type str
