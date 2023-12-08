largura: float = float(input("Informe largura do cômodo em metros: "))
altura: float = float(input("Informe altura do cômodo em metros: "))
profundidade: float = float(input("Informe profundidade do cômodo em metros: "))

area_paredes: float = 2 * (largura + profundidade) * altura

print("A área das paredes é: ", area_paredes , "metros")

area_teto: float = largura * profundidade

print("A área do teto é: ", area_teto , "metros")

print("Sabendo que a cada 1 litro de tinta rende 10 metros de pintura, a litragem de tinta necessária é: ", (area_paredes + area_teto) / 10 , "litros")