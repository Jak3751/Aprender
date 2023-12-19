def adicionar_aspas(frases):
    frases_modificadas = []

    for frase in frases:
        # Adicionar aspas no início e no final
        nova_frase = f'"{frase}"'
        frases_modificadas.append(nova_frase)

    return frases_modificadas

# Exemplo de uso
frases_originais = [
    "alguma coisa aqui",
    "outra coisa ali",
    # Adicione mais frases conforme necessário
]

frases_modificadas = adicionar_aspas(frases_originais)

# Imprimir frases originais e modificadas
for original, modificada in zip(frases_originais, frases_modificadas):
    print(f"Original: {original}")
    print(f"Modificada: {modificada}")
    print("-----")