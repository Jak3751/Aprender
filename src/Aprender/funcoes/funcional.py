def soma(a, b):
    return a + b

def sub(a, b):
    return a - b

somar = soma
print(somar(3, 4))

def operacao_aritimetica(fn, op1, op2):
    return fn(op1, op2)


resultado = operacao_aritimetica(soma, 13, 48)
print(f'O resultado da soma é {resultado}')
resultado = operacao_aritimetica(sub, 13, 48)
print(f'O resultado da subtração é {resultado}')


def soma_parcial(a):
    # processamento pesado 1 = 10s
    # processamento pesado 2 = 10s
    # processamento pesado 3 = 40s
    def concluir_soma(b):
        return a + b  # processamento 4 = 10s
    return concluir_soma

# r1 = soma_total(1, 2) => total processamento 1m 10s
# r2 = soma_total(1, 3) => total processamento 1m 10s
# r3 = soma_total(1, 4) => total processamento 1m 10s

#Exemplo para ficar mais rapido, usando soma_parcial
soma_1 = soma_parcial(1) # processamento = 1m
r1 = soma_1(2)
r2 = soma_1(3)
r3 = soma_1(4)

fn = soma_parcial(10)
resultado_final = fn(12)
print(f'A funcao parcial com o valor de "10" eh: {resultado_final, r1, r2, r3}')