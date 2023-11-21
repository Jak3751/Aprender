a = 3                                                                           #Declarando variavel numerico
b = 4.4


print(+a+b)

texto = 'Sua idade e...'                                                        #Declarando variavel texto
idade = 23


#print(texto + str (idade))                                                     #Sua idade e...23
#print(f'{texto} {idade}')                                                      #Sua idade e... 23
print(3 * texto)                                                                #Sua idade e...Sua idade e...Sua idade e...

PI = 3.14
raio = float(input('Informe o raio da circ? '))                                 #Converter STR "String" em numero usa o float
#area = PI * raio * raio
area = PI * pow(raio, 2)                                                        #Para utilizar função de potencia quando o numero é elevado a x valor, utiliza o pow
#print(type(raio))                                                              #Usa o type para mostrar qual é o tipo da variavel "raio"
#print(area)                                                                    #Mostra apenas o resultado
print(f'A área da circ é {area} m2.')