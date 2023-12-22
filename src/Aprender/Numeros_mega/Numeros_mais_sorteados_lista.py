from collections import Counter
import re

def extrair_numeros(frase):
    # Usando expressão regular para extrair números da frase
    return [int(numero) for numero in re.findall(r'\d+', frase)]

def encontrar_numeros_frequentes(numeros_sorteados, quantidade=6):
    contagem_numeros = Counter(numeros_sorteados)
    numeros_mais_frequentes = contagem_numeros.most_common(quantidade)

    return numeros_mais_frequentes

def main():
    # Substitua esta lista pelos números sorteados da Mega-Sena
    numeros_sorteados = [
        4,7,16,35,46,54,
        1,27,30,41,46,57,
        1,4,8,21,46,51
    ]

    # Você também pode ler essa lista de um arquivo, banco de dados, etc.

    numeros_frequentes = encontrar_numeros_frequentes(numeros_sorteados)

    print("\nNúmeros mais frequentes:")
    for numero, frequencia in numeros_frequentes:
        print(f"Número {numero}: {frequencia} vezes")

if __name__ == "__main__":
    main()