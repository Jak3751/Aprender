import requests
from collections import Counter

def obter_ultimos_resultados():
    url = "https://apiloterias.com.br/app/v2/resultado?loteria=megasena&token=kJdfLjd38Jai2ek"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro ao obter os resultados da Mega-Sena. Código de status: {response.status_code}")
        return None

def encontrar_numeros_frequentes(resultados, quantidade=5):
    numeros = [resultado["dezenas"] for resultado in resultados]
    numeros_flat = [numero for sublist in numeros for numero in sublist]
    
    contagem_numeros = Counter(numeros_flat)
    numeros_mais_frequentes = contagem_numeros.most_common(quantidade)

    return numeros_mais_frequentes

def main():
    ultimos_resultados = obter_ultimos_resultados()

    if ultimos_resultados:
        print("Últimos resultados da Mega-Sena:")
        for resultado in ultimos_resultados:
            print(f"Concurso {resultado['concurso']}: {resultado['dezenas']}")

        numeros_frequentes = encontrar_numeros_frequentes(ultimos_resultados)
        print("\nNúmeros mais frequentes:")
        for numero, frequencia in numeros_frequentes:
            print(f"Número {numero}: {frequencia} vezes")

if __name__ == "__main__":
    main()