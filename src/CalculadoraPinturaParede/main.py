from calculadora import Calculadora
from comodo import Comodo


calc = Calculadora()

largura: float = float(input("Informe largura do cômodo em metros: "))
altura: float = float(input("Informe altura do cômodo em metros: "))
profundidade: float = float(input("Informe profundidade do cômodo em metros: "))

comodo = Comodo(altura, largura, profundidade)

print("A área das paredes é: ",
    calc.calcular_area_paredes(comodo.largura, comodo.profundidade, comodo.altura), "metros")

print("A área do teto é: ",
    calc.calcular_area_teto(comodo.largura, comodo.profundidade), "metros")

print("Sabendo que a cada 1 litro de tinta rende 10 metros de pintura, a litragem de tinta necessária é: ", 
    calc.calcular_litragem_necessaria(), "litros")