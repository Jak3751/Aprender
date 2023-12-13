from functools import reduce


def somar_nota(delta):
    def somar(nota):
        return nota + delta
    return somar



notas = [6.4, 7.2, 5.8, 8.4]

# for i, nota in enumerate(notas):
#    notas[i] = nota + 1.5
# Posso fazer com range tambem
# for i in range(len(notas)):
#    notas[i] = notas[i] + 1.5
# Posso fazer com Map tambem
notas_finais_1 = map(somar_nota(1.5), notas)
notas_finais_2 = map(somar_nota(1.6), notas)
print(notas_finais_1)
print(notas_finais_2)

#total = 0
#for n in notas:
#    total += n
#print(total)


def somar(a, b):
    return a+b

total = reduce(somar, notas, 0)
print(total)

