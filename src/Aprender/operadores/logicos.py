b1 = True
b2 = False
b3 = True
print(b1 and b2)                      #Só é verdadeiro se todas expressões forem verdadeiras, resultado = False
print(b1 and b2 and b3)               #Só é verdadeiro se todas expressões forem verdadeiras, resultado = False
print(b1 or b2 or b3)                 #Basta 1 deles ser True, que o resultado = True
print(b1 != b2)                       #Como em Python não tem "ou exclusivo = quando um deles é exclusivamente verdadeiro ou falso" podemos usar "diferença = !=" para este caso
print(not b1)                         #Negação, b1 era True, passou para False
print(not b2)                         #Negação, b2 era False, passou para True


print(b1 and not b2 and b3)           #Resultado será True

x = 3
y = 4
print(b1 and not b2 and x < y)         #Resultado será True