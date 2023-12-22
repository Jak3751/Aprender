import pandas as pd
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
    # Substitua o caminho do arquivo pelo caminho real do seu arquivo Excel
    caminho_arquivo_excel = "C:/Users/jakson.silva/Downloads/mega_sena_asloterias_ate_concurso_2669_sorteio.xlsx"

    # Lê o arquivo Excel usando o pandas
    df = pd.read_excel(caminho_arquivo_excel)

    # Extrai os números sorteados de todas as linhas
    numeros_sorteados = [numero for numeros_linha in df.values for numero in extrair_numeros(str(numeros_linha))]

    numeros_frequentes = encontrar_numeros_frequentes(numeros_sorteados)

    print("\nNúmeros mais frequentes:")
    for numero, frequencia in numeros_frequentes:
        print(f"Número {numero}: {frequencia} vezes")

if __name__ == "__main__":
    main()