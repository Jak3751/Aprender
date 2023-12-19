nums = [0, 1, 2]                                                                #Gerando uma lista
print(type(nums))                                                               #Mostrando qual tipo da variavel "nums"

nums.append(3)
nums.append(4)
nums.append(5)                                                                  #Adicionando um numero a lista, pode ser repetido, sem problemas
print(len(nums))                                                                #Metodo "len", para ver o tamanho da lista

nums[3] = 100                                                                   #Atribuido valor 100 para a 3°posição da lista
nums.insert(0, -200)                                                            #Adicionado valor -200 para 0°posição da lista
print(nums[-1])                                                                 #Pegar ultimo elemento da lista
print(nums)