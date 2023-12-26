import random

def escolher_palavra():
    palavras = ['python', 'programacao', 'computador', 'desenvolvimento', 'tecnologia']
    return random.choice(palavras)

def mostrar_forca(palavra, letras_corretas):
    for letra in palavra:
        if letra in letras_corretas:
            print(letra, end=' ')
        else:
            print('_', end=' ')
    print()

def jogar_forca():
    palavra_secreta = escolher_palavra()
    letras_corretas = []
    tentativas = 6  # Número máximo de tentativas

    print("Bem-vindo ao Jogo da Forca!")

    while tentativas > 0:
        mostrar_forca(palavra_secreta, letras_corretas)

        palpite = input("Digite uma letra: ").lower()

        if len(palpite) != 1 or not palpite.isalpha():
            print("Por favor, digite uma única letra válida.")
            continue

        if palpite in letras_corretas:
            print("Você já tentou essa letra. Tente outra.")
            continue

        if palpite in palavra_secreta:
            print("Letra correta!")
            letras_corretas.append(palpite)
        else:
            print("Letra incorreta. Você perdeu uma tentativa.")
            tentativas -= 1

        if set(letras_corretas) == set(palavra_secreta):
            print("Parabéns! Você acertou a palavra:", palavra_secreta)
            break

    if tentativas == 0:
        print("Você perdeu! A palavra correta era:", palavra_secreta)

if __name__ == "__main__":
    jogar_forca()