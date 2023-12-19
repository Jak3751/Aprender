#Faça um algoritmo que solicite o nome do usuário e depois escreva o nome da pessoa no console.
#nome = input("Informe seu nome :")
#print(nome)


#Faça um algoritmo que pergunte ao usuário quantos anos ele tem, depois disso, escreva True no console, caso ele já tenha alcançado a maioridade (18 anos), caso contrário escreva False.
#idade = int(input("Quantos anos você tem ? "))
#maioridade = idade >= 18
#print(maioridade)


#Faça um algoritmo que solicite um número ao usuário, depois disso, escreva True no console, caso o número tenha dois dígitos (Esteja entre 10 e 99), caso contrário escreva False.
#numero = int(input("Informe um numero :"))
#dois_digitos = numero >= 10 and numero <=99
#print(dois_digitos)


#Faça um algoritmo que solicite 3 notas para o usuário, calcule a média e indique se o aluno foi aprovado ou reprovado (nota precisar ser maior ou igual à sete para o aluno ser aprovado).
#nota1 = float(input("Informe a primeira nota: "))
#nota2 = float(input("informe a segunda nota: "))
#nota3 = float(input("informe a terceira nota: "))

#media = (nota1 + nota2 + nota3) / 3

#if media >= 7:
#    print("Aprovado")
#else:
#    print("Reprovado")


#Faça um algoritmo que solicite o ano que o usuário nasceu, depois disso, faça o programa descrever se o usuário fará ou já fez 18 anos neste ano.
#ano_nascimento = int(input("Informe o ano que você nasceu: "))

#maior_menor = (2023 - ano_nascimento)

#if maior_menor == 18:
#    print("Você fará ou já fez 18 anos")
#else:
#    print("menor de idade") 


#Faça um programa que solicite ao usuário sua idade, depois disso, exiba a classificação etária de acordo com as faixas de valores:
#Criança para 0 até 11 anos;
#Adolescente para 12 até 18 anos;
#Jovem para 19 até 24 anos;
#Adulto para 25 até 40 anos;
#Meia Idade para 41 até 60 anos;
#Idoso acima de 60 anos.

#idade = int(input("informe sua idade: "))

#if idade >= 0 and idade <= 11:
#    print("Você é criança")
#elif idade >= 12 and idade <= 18:
#    print("Você é adolescente")
#elif idade >= 19 and idade <= 24:
#    print("Você é jovem")
#elif idade >= 25 and idade <= 40:
#    print("Você é adulto")
#elif idade >= 41 and idade <= 60:
#    print("Você esta na meia idade")
#else:
#    print("seu velho")


#Faça um programa que solicite ao usuário 2 valores, utilize uma condição ternária para escrever qual o maior valor: o primeiro ou o segundo (caso os valores sejam iguais, considere o segundo).

#primeiro_valor = int( input("Digite um valor: "))
#segundo_valor = int( input("Digite um valor: "))
#print( "Primeiro" if primeiro_valor > segundo_valor else "Segundo")

#Faça um programa que solicite o nome do usuário e depois disso faça uma saudação no formato: "Olá {nome digitado pelo usuário}".
#nome = input("informe seu nome: ")
#print("nome digitado pelo usuário: ",nome)


#Faça um programa que solicite uma mensagem qualquer para o usuário e exiba esta mensagem com todas as letras em maiúsculo.
#frase = input("Digite uma frase qualquer: ")
#print(frase.upper)


#Faça um programa que solicite a idade do usuário, verifique se o texto informado só contém números. Caso contenha somente números exiba a mensagem: "Você tem {idade digitada} anos.", caso contrário exiba a mensagem: "Você digitou uma idade inválida".

#if idade.isdigit():
#    print(f"Você tem {idade} anos.")
#else:
#    print("Você digitou uma idade inválida")

#Faça um programa que solicite o nome completo do usuário e exiba somente o seu segundo nome/primeiro sobrenome.
#nome_completo = input("Digite seu nome completo: ")
#nome_completo_dividido = nome_completo.split(" ")
#print(nome_completo_dividido[1])



#Faça um programa que inicialize uma lista com o nome das pessoas da sua família.
#familia = ["Jakson", "Aline", "Lola", "Maggie"]
#print(familia)


#Faça um programa que inicialize uma lista vazia e solicite ao usuário 3 nomes de cidades, um por vez, cada vez que o usuário digitar um nome, o programa deve incluir este nome na lista de cidades.
cidades = []

#cidade = input("Digite o nome da primeira cidade: ")
#cidades.append(cidade)
#cidades.append(input("Digite o nome da segunda cidade: "))
#cidades.append(input("Digite o nome da terceira cidade: "))
#print(cidades)

#Faça um programa que inicialize uma lista com vários números diferentes, depois disso, solicite ao usuário um número, verifique se o número está ou não na lista e exiba uma mensagem notificando o usuário do resultado.
#numeros = [1,2,3]
#numero = int(input("informe um numero: "))

#if numero in numeros:
#    print("Esta na lista")
#else:
#    print("Não esta na lista")
    

#Faça um programa que inicialize uma lista vazia e a preencha com 5 nomes diferentes digitados pelo usuário, depois disso solicite um número de 0 até 4 e remova o elemento desta posição.
#nomes = []
#nomes.append(input("Digite o primeiro nome: "))
#nomes.append(input("Digite o segundo nome: "))
#nomes.append(input("Digite o terceiro nome: "))
#nomes.append(input("Digite o quarto nome: "))
#nomes.append(input("Digite o quinto nome: "))

#posicao_para_excluir = int( input("Escolha uma posição de 0(zero) até quatro para excluir da lista: "))
#del nomes[posicao_para_excluir]
#print(nomes)



#Faça um programa que solicite o nome do usuário e a idade do usuário, depois disso exiba a mensagem: "{nome} possui {idade} anos.". Esta mensagem deve ser escrita em uma função.
#def escrever_nome_idade(nome, idade):
#    print(nome, "possui",idade,"anos.")

#nome_digitado = str(input("Digite seu nome: "))
#idade_digitada = int(input("Digite sua idade: "))

#escrever_nome_idade(nome_digitado, idade_digitada)


#Faça um programa que solicite dois números ao usuário e exiba a multiplicação deles. A multiplicação deve ser calculada em uma função.
#def multiplicar(numero1, numero2):
#    return numero1 * numero2

#numero = int(input("Digite o primeiro número: "))
#numero2 = int(input("Digite o segundo número: "))
#resultado = multiplicar(numero, numero2)
#print(resultado)


