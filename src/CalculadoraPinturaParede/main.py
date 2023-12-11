from calculadora import Calculadora
from comodo import Comodo

calc = Calculadora()

comodo = Comodo(
    input('Qual altura do cômodo, em metros? '),
    input('Qual largura do cômodo, em metros? '),
    input('Qual profundidade do cômodo, em metros ? ')
)

print("A área das paredes é: ",
    calc.calcular_area_paredes(comodo.largura, comodo.profundidade, comodo.altura), "metros")

print("A área do teto é: ",
    calc.calcular_area_teto(comodo.largura, comodo.profundidade), "metros")

print("Sabendo que a cada 1 litro de tinta rende 10 metros de pintura, a litragem de tinta necessária é: ", 
    calc.calcular_litragem_necessaria(), "litros")