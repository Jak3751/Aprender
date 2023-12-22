import re

def extrair_numero_sete_digitos(texto):
    padrao = r'\b\d{7}\b'
    correspondencias = re.findall(padrao, texto)
    
    if correspondencias:
        return correspondencias[0]
    else:
        return None

# Exemplo de uso
texto_exemplo = "Este é um exemplo com o número 1234567 e outros números."
numero_sete_digitos = extrair_numero_sete_digitos(texto_exemplo)

if numero_sete_digitos:
    print(f"Número de 7 dígitos encontrado: {numero_sete_digitos}")
else:
    print("Nenhum número de 7 dígitos encontrado.")