#Faça um programa que receba a idade do usuário e diga se ele é maior ou menor de idade.

idade = int(input('Informe sua idade :'))

if idade >= 18:
    print('Voce é maior de idade')
else:
    print('Voce é menor de idade')
    
#Faça um programa que receba duas notas digitadas pelo usuário. Se a nota for maior ou igual a seis, escreva aprovado, senão escreva reprovado.
    
nota1 = float(input('Informe a primeira nota :'))
nota2 = float(input('Informe a segunda nota :'))

media = (nota1 + nota2) / 2


if media >= 6:
    print('Aprovado!')
else:
    print('Reprovado!')
        
#Escreva um programa que ordene uma lista numérica com três elementos.  

nums = [3,2,1]
print(sorted(nums))

#Em Python, dicionários são arrays associativos, ou seja, um determinado valor passa a ser vinculado a uma chave. Exemplo:

#dicionarios em python
dicionario_sites = {"Diego": "diegomariano.com"}


#No dicionário acima, a chave "Diego" foi vinculado ao valor "diegomariano.com". Assim, para imprimir o valor chame:

print(dicionario_sites['Diego'])
# Sera impresso "diegomariano.com


#Se o dicionário tiver vários elementos, você pode usar laços para imprimi-los:

#dicionarios em python
dicionario_sites = {"Diego": "diegomariano.com", "Google": "google.com", "Udemy": "udemy.com"}
 
for chave in dicionario_sites:
    print(dicionario_sites[chave])
