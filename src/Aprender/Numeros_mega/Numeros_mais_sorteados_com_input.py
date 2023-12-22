from collections import Counter
import re

def extrair_numeros(frase):
    # Usando expressão regular para extrair números da frase
    return [int(numero) for numero in re.findall(r'\d+', frase)]

def encontrar_numeros_frequentes(frases, quantidade=5):
    todos_numeros = [numero for frase in frases for numero in extrair_numeros(frase)]
    
    contagem_numeros = Counter(todos_numeros)
    numeros_mais_frequentes = contagem_numeros.most_common(quantidade)

    return numeros_mais_frequentes

def main():
    frases = []
    
    for i in range(3):
        frase = input(f"Informe a {i+1}ª frase com os números sorteados da Mega-Sena: ")
        frases.append(frase)

    numeros_frequentes = encontrar_numeros_frequentes(frases)

    print("\nNúmeros mais frequentes:")
    for numero, frequencia in numeros_frequentes:
        print(f"Número {numero}: {frequencia} vezes")

if __name__ == "__main__":
    main()