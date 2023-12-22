import re

def extrair_numero_sete_digitos(texto):
    padrao = r'\b\d{7}\b'
    correspondencias = re.findall(padrao, texto)
    
    if correspondencias:
        return correspondencias[0]
    else:
        return None

# Exemplo de uso
texto_exemplo = """INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0524331) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (007197) na receita difere da quantidade movimentada nos lotes do pedido (0507007) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0507008) empresa (01). (Qtde receita: 800, Qtde pedido 40)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (004907) na receita difere da quantidade movimentada nos lotes do pedido (0504904) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (007124) na receita difere da quantidade movimentada nos lotes do pedido (0564488) empresa (01). (Qtde receita: 50, Qtde pedido 10)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (004907) na receita difere da quantidade movimentada nos lotes do pedido (0564339) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (003310) na receita difere da quantidade movimentada nos lotes do pedido (0551788) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (000400) na receita difere da quantidade movimentada nos lotes do pedido (0406285) empresa (01). (Qtde receita: 1, Qtde pedido 2)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (000400) na receita difere da quantidade movimentada nos lotes do pedido (0406285) empresa (01). (Qtde receita: 1, Qtde pedido 2)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (003822) na receita difere da quantidade movimentada nos lotes do pedido (0524181) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (007206) na receita difere da quantidade movimentada nos lotes do pedido (0478378) empresa (01). (Qtde receita: 1000, Qtde pedido 50)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (003822) na receita difere da quantidade movimentada nos lotes do pedido (0504656) empresa (01). (Qtde receita: 800, Qtde pedido 40)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (004907) na receita difere da quantidade movimentada nos lotes do pedido (0524185) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0504925) empresa (01). (Qtde receita: 2000, Qtde pedido 100)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0524206) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (007124) na receita difere da quantidade movimentada nos lotes do pedido (0461406) empresa (01). (Qtde receita: 5, Qtde pedido 1)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0524037) empresa (01). (Qtde receita: 1200, Qtde pedido 60)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (006353) na receita difere da quantidade movimentada nos lotes do pedido (0524049) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (007186) na receita difere da quantidade movimentada nos lotes do pedido (0475582) empresa (01). (Qtde receita: 20, Qtde pedido 1)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0475584) empresa (01). (Qtde receita: 20, Qtde pedido 1)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (007197) na receita difere da quantidade movimentada nos lotes do pedido (0478379) empresa (01). (Qtde receita: 5, Qtde pedido 1)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0475721) empresa (01). (Qtde receita: 60, Qtde pedido 3)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (003822) na receita difere da quantidade movimentada nos lotes do pedido (0504785) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (004907) na receita difere da quantidade movimentada nos lotes do pedido (0505059) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0504839) empresa (01). (Qtde receita: 800, Qtde pedido 40)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (007410) na receita difere da quantidade movimentada nos lotes do pedido (0524342) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0524213) empresa (01). (Qtde receita: 800, Qtde pedido 40)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0524226) empresa (01). (Qtde receita: 800, Qtde pedido 40)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0505121) empresa (01). (Qtde receita: 3200, Qtde pedido 160)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (007331) na receita difere da quantidade movimentada nos lotes do pedido (0505123) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (007177) na receita difere da quantidade movimentada nos lotes do pedido (0505163) empresa (01). (Qtde receita: 2000, Qtde pedido 100)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0524242) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0524245) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (003822) na receita difere da quantidade movimentada nos lotes do pedido (0524247) empresa (01). (Qtde receita: 1200, Qtde pedido 60)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0507286) empresa (01). (Qtde receita: 800, Qtde pedido 40)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0501741) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (003822) na receita difere da quantidade movimentada nos lotes do pedido (0524248) empresa (01). (Qtde receita: 1200, Qtde pedido 60)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0507102) empresa (01). (Qtde receita: 800, Qtde pedido 40)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0524249) empresa (01). (Qtde receita: 5600, Qtde pedido 280)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (007053) na receita difere da quantidade movimentada nos lotes do pedido (0524252) empresa (01). (Qtde receita: 800, Qtde pedido 40)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0524063) empresa (01). (Qtde receita: 800, Qtde pedido 40)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0524359) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (007206) na receita difere da quantidade movimentada nos lotes do pedido (0524273) empresa (01). (Qtde receita: 1200, Qtde pedido 60)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (006353) na receita difere da quantidade movimentada nos lotes do pedido (0524278) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (007436) na receita difere da quantidade movimentada nos lotes do pedido (0524303) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0524371) empresa (01). (Qtde receita: 4000, Qtde pedido 200)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0524594) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (006353) na receita difere da quantidade movimentada nos lotes do pedido (0524375) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0524391) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (003903) na receita difere da quantidade movimentada nos lotes do pedido (0524627) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (006353) na receita difere da quantidade movimentada nos lotes do pedido (0524496) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (003310) na receita difere da quantidade movimentada nos lotes do pedido (0507346) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0507380) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0524507) empresa (01). (Qtde receita: 1600, Qtde pedido 80)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (006353) na receita difere da quantidade movimentada nos lotes do pedido (0524545) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (004907) na receita difere da quantidade movimentada nos lotes do pedido (0524680) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (003822) na receita difere da quantidade movimentada nos lotes do pedido (0524776) empresa (01). (Qtde receita: 4000, Qtde pedido 200)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0525026) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0507487) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (007436) na receita difere da quantidade movimentada nos lotes do pedido (0524729) empresa (01). (Qtde receita: 50, Qtde pedido 10)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0524778) empresa (01). (Qtde receita: 1200, Qtde pedido 60)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0507897) empresa (01). (Qtde receita: 800, Qtde pedido 40)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0507699) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (007197) na receita difere da quantidade movimentada nos lotes do pedido (0507717) empresa (01). (Qtde receita: 50, Qtde pedido 10)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0507729) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0507789) empresa (01). (Qtde receita: 800, Qtde pedido 40)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (003822) na receita difere da quantidade movimentada nos lotes do pedido (0524823) empresa (01). (Qtde receita: 800, Qtde pedido 40)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0512995) empresa (01). (Qtde receita: 4400, Qtde pedido 220)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0518199) empresa (01). (Qtde receita: 800, Qtde pedido 40)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0524843) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0525029) empresa (01). (Qtde receita: 2400, Qtde pedido 120)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0524852) empresa (01). (Qtde receita: 800, Qtde pedido 40)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (006353) na receita difere da quantidade movimentada nos lotes do pedido (0525031) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (004907) na receita difere da quantidade movimentada nos lotes do pedido (0524854) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (006705) na receita difere da quantidade movimentada nos lotes do pedido (0508390) empresa (01). (Qtde receita: 50, Qtde pedido 10)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0524856) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0507979) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0508401) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (006705) na receita difere da quantidade movimentada nos lotes do pedido (0508036) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (006705) na receita difere da quantidade movimentada nos lotes do pedido (0508239) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0508264) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0508448) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0508454) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (007436) na receita difere da quantidade movimentada nos lotes do pedido (0524858) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0508556) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0508570) empresa (01). (Qtde receita: 2800, Qtde pedido 140)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (007174) na receita difere da quantidade movimentada nos lotes do pedido (0508607) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0524868) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0524899) empresa (01). (Qtde receita: 3200, Qtde pedido 160)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (006353) na receita difere da quantidade movimentada nos lotes do pedido (0525036) empresa (01). (Qtde receita: 100, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0525249) empresa (01). (Qtde receita: 1600, Qtde pedido 80)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (004907) na receita difere da quantidade movimentada nos lotes do pedido (0524904) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0525043) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (006353) na receita difere da quantidade movimentada nos lotes do pedido (0524912) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0524920) empresa (01). (Qtde receita: 800, Qtde pedido 40)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0524937) empresa (01). (Qtde receita: 2000, Qtde pedido 100)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0525052) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (007436) na receita difere da quantidade movimentada nos lotes do pedido (0525077) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (003822) na receita difere da quantidade movimentada nos lotes do pedido (0513664) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (003822) na receita difere da quantidade movimentada nos lotes do pedido (0524967) empresa (01). (Qtde receita: 1200, Qtde pedido 60)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (003822) na receita difere da quantidade movimentada nos lotes do pedido (0525009) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0525271) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0525100) empresa (01). (Qtde receita: 800, Qtde pedido 40)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (003822) na receita difere da quantidade movimentada nos lotes do pedido (0525491) empresa (01). (Qtde receita: 6000, Qtde pedido 300)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0525292) empresa (01). (Qtde receita: 1200, Qtde pedido 60)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (003822) na receita difere da quantidade movimentada nos lotes do pedido (0525131) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (007177) na receita difere da quantidade movimentada nos lotes do pedido (0525154) empresa (01). (Qtde receita: 800, Qtde pedido 40)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (003822) na receita difere da quantidade movimentada nos lotes do pedido (0525493) empresa (01). (Qtde receita: 1200, Qtde pedido 60)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0525300) empresa (01). (Qtde receita: 800, Qtde pedido 40)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0525168) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (007436) na receita difere da quantidade movimentada nos lotes do pedido (0525325) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0525215) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (003822) na receita difere da quantidade movimentada nos lotes do pedido (0525216) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0525334) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0525499) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0525841) empresa (01). (Qtde receita: 800, Qtde pedido 40)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0525345) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (006705) na receita difere da quantidade movimentada nos lotes do pedido (0525363) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (007177) na receita difere da quantidade movimentada nos lotes do pedido (0525390) empresa (01). (Qtde receita: 1200, Qtde pedido 60)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0525392) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (007436) na receita difere da quantidade movimentada nos lotes do pedido (0525393) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0525508) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (004907) na receita difere da quantidade movimentada nos lotes do pedido (0525405) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (004907) na receita difere da quantidade movimentada nos lotes do pedido (0525423) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (003822) na receita difere da quantidade movimentada nos lotes do pedido (0525432) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0525447) empresa (01). (Qtde receita: 1200, Qtde pedido 60)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (007410) na receita difere da quantidade movimentada nos lotes do pedido (0525455) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (003822) na receita difere da quantidade movimentada nos lotes do pedido (0525538) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0525727) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (003822) na receita difere da quantidade movimentada nos lotes do pedido (0525547) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (004907) na receita difere da quantidade movimentada nos lotes do pedido (0525548) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0525558) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (007174) na receita difere da quantidade movimentada nos lotes do pedido (0525572) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005875) na receita difere da quantidade movimentada nos lotes do pedido (0525596) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0525601) empresa (01). (Qtde receita: 1200, Qtde pedido 60)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (004907) na receita difere da quantidade movimentada nos lotes do pedido (0525602) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0525615) empresa (01). (Qtde receita: 800, Qtde pedido 40)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (003903) na receita difere da quantidade movimentada nos lotes do pedido (0525864) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0525630) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0525648) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (003310) na receita difere da quantidade movimentada nos lotes do pedido (0525760) empresa (01). (Qtde receita: 50, Qtde pedido 10)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0526096) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0525792) empresa (01). (Qtde receita: 800, Qtde pedido 40)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (006353) na receita difere da quantidade movimentada nos lotes do pedido (0525883) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (003310) na receita difere da quantidade movimentada nos lotes do pedido (0525938) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (003822) na receita difere da quantidade movimentada nos lotes do pedido (0525939) empresa (01). (Qtde receita: 14000, Qtde pedido 700)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0526102) empresa (01). (Qtde receita: 800, Qtde pedido 40)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (003822) na receita difere da quantidade movimentada nos lotes do pedido (0526117) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0526146) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0525987) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (007206) na receita difere da quantidade movimentada nos lotes do pedido (0525994) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (003903) na receita difere da quantidade movimentada nos lotes do pedido (0526006) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0526023) empresa (01). (Qtde receita: 1600, Qtde pedido 80)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0526024) empresa (01). (Qtde receita: 1200, Qtde pedido 60)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0513955) empresa (01). (Qtde receita: 2000, Qtde pedido 100)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (003310) na receita difere da quantidade movimentada nos lotes do pedido (0526062) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (007177) na receita difere da quantidade movimentada nos lotes do pedido (0526074) empresa (01). (Qtde receita: 800, Qtde pedido 40)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0526154) empresa (01). (Qtde receita: 1200, Qtde pedido 60)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (003822) na receita difere da quantidade movimentada nos lotes do pedido (0526155) empresa (01). (Qtde receita: 800, Qtde pedido 40)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (007436) na receita difere da quantidade movimentada nos lotes do pedido (0526384) empresa (01). (Qtde receita: 100, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (006353) na receita difere da quantidade movimentada nos lotes do pedido (0526167) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (004907) na receita difere da quantidade movimentada nos lotes do pedido (0526171) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0526187) empresa (01). (Qtde receita: 2000, Qtde pedido 100)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (007436) na receita difere da quantidade movimentada nos lotes do pedido (0526189) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0526261) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0526265) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0526748) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005875) na receita difere da quantidade movimentada nos lotes do pedido (0526749) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005875) na receita difere da quantidade movimentada nos lotes do pedido (0526750) empresa (01). (Qtde receita: 50, Qtde pedido 10)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0526504) empresa (01). (Qtde receita: 2000, Qtde pedido 100)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (004907) na receita difere da quantidade movimentada nos lotes do pedido (0526549) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (004907) na receita difere da quantidade movimentada nos lotes do pedido (0526555) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0518114) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0526575) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0526584) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0522635) empresa (01). (Qtde receita: 800, Qtde pedido 40)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (003310) na receita difere da quantidade movimentada nos lotes do pedido (0526589) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005875) na receita difere da quantidade movimentada nos lotes do pedido (0526752) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0522801) empresa (01). (Qtde receita: 1600, Qtde pedido 80)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (007436) na receita difere da quantidade movimentada nos lotes do pedido (0526600) empresa (01). (Qtde receita: 50, Qtde pedido 10)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (007436) na receita difere da quantidade movimentada nos lotes do pedido (0521103) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0530413) empresa (01). (Qtde receita: 800, Qtde pedido 40)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (006353) na receita difere da quantidade movimentada nos lotes do pedido (0526607) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (004907) na receita difere da quantidade movimentada nos lotes do pedido (0526656) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (007331) na receita difere da quantidade movimentada nos lotes do pedido (0526660) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (004907) na receita difere da quantidade movimentada nos lotes do pedido (0526661) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (004907) na receita difere da quantidade movimentada nos lotes do pedido (0526669) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (006353) na receita difere da quantidade movimentada nos lotes do pedido (0526670) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (003822) na receita difere da quantidade movimentada nos lotes do pedido (0526695) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (004907) na receita difere da quantidade movimentada nos lotes do pedido (0521346) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0526698) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0526820) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0526839) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0526840) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (004907) na receita difere da quantidade movimentada nos lotes do pedido (0526854) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (007436) na receita difere da quantidade movimentada nos lotes do pedido (0526861) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0527001) empresa (01). (Qtde receita: 1200, Qtde pedido 60)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (007174) na receita difere da quantidade movimentada nos lotes do pedido (0527005) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0527145) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (003822) na receita difere da quantidade movimentada nos lotes do pedido (0530137) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0527146) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0526893) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0526906) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (006705) na receita difere da quantidade movimentada nos lotes do pedido (0526909) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0527413) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (006353) na receita difere da quantidade movimentada nos lotes do pedido (0527640) empresa (01). (Qtde receita: 50, Qtde pedido 10)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0527175) empresa (01). (Qtde receita: 800, Qtde pedido 40)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (006705) na receita difere da quantidade movimentada nos lotes do pedido (0527177) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0521878) empresa (01). (Qtde receita: 2000, Qtde pedido 100)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (004907) na receita difere da quantidade movimentada nos lotes do pedido (0527428) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (003822) na receita difere da quantidade movimentada nos lotes do pedido (0527196) empresa (01). (Qtde receita: 800, Qtde pedido 40)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (004907) na receita difere da quantidade movimentada nos lotes do pedido (0527448) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (004907) na receita difere da quantidade movimentada nos lotes do pedido (0527214) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (004907) na receita difere da quantidade movimentada nos lotes do pedido (0527248) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0527253) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0527276) empresa (01). (Qtde receita: 1200, Qtde pedido 60)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0527296) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (004907) na receita difere da quantidade movimentada nos lotes do pedido (0527336) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (004907) na receita difere da quantidade movimentada nos lotes do pedido (0527358) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0527473) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (004907) na receita difere da quantidade movimentada nos lotes do pedido (0527480) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (003822) na receita difere da quantidade movimentada nos lotes do pedido (0527490) empresa (01). (Qtde receita: 800, Qtde pedido 40)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0527491) empresa (01). (Qtde receita: 1600, Qtde pedido 80)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0527646) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (003822) na receita difere da quantidade movimentada nos lotes do pedido (0527675) empresa (01). (Qtde receita: 8000, Qtde pedido 400)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0527562) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0518860) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (004907) na receita difere da quantidade movimentada nos lotes do pedido (0527575) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (007436) na receita difere da quantidade movimentada nos lotes do pedido (0527581) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0524075) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (004907) na receita difere da quantidade movimentada nos lotes do pedido (0524090) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (004907) na receita difere da quantidade movimentada nos lotes do pedido (0524099) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (003310) na receita difere da quantidade movimentada nos lotes do pedido (0524104) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0524130) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (004907) na receita difere da quantidade movimentada nos lotes do pedido (0527588) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (006353) na receita difere da quantidade movimentada nos lotes do pedido (0524136) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0527598) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (007436) na receita difere da quantidade movimentada nos lotes do pedido (0527621) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (006353) na receita difere da quantidade movimentada nos lotes do pedido (0529907) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (006353) na receita difere da quantidade movimentada nos lotes do pedido (0527923) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0527993) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0527994) empresa (01). (Qtde receita: 1600, Qtde pedido 80)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (004907) na receita difere da quantidade movimentada nos lotes do pedido (0527782) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (004907) na receita difere da quantidade movimentada nos lotes do pedido (0527950) empresa (01). (Qtde receita: 50, Qtde pedido 10)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (004907) na receita difere da quantidade movimentada nos lotes do pedido (0527803) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (007436) na receita difere da quantidade movimentada nos lotes do pedido (0527814) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (004907) na receita difere da quantidade movimentada nos lotes do pedido (0527973) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (003822) na receita difere da quantidade movimentada nos lotes do pedido (0528512) empresa (01). (Qtde receita: 2400, Qtde pedido 120)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (003822) na receita difere da quantidade movimentada nos lotes do pedido (0528040) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (007436) na receita difere da quantidade movimentada nos lotes do pedido (0527830) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (003822) na receita difere da quantidade movimentada nos lotes do pedido (0528515) empresa (01). (Qtde receita: 1600, Qtde pedido 80)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0527867) empresa (01). (Qtde receita: 1200, Qtde pedido 60)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0528059) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (007436) na receita difere da quantidade movimentada nos lotes do pedido (0527870) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (007436) na receita difere da quantidade movimentada nos lotes do pedido (0527873) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (006353) na receita difere da quantidade movimentada nos lotes do pedido (0528341) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (004907) na receita difere da quantidade movimentada nos lotes do pedido (0528084) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0528095) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (007436) na receita difere da quantidade movimentada nos lotes do pedido (0528117) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (003310) na receita difere da quantidade movimentada nos lotes do pedido (0528132) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0528154) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (007436) na receita difere da quantidade movimentada nos lotes do pedido (0522813) empresa (01). (Qtde receita: 50, Qtde pedido 10)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (007333) na receita difere da quantidade movimentada nos lotes do pedido (0528390) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0528529) empresa (01). (Qtde receita: 1200, Qtde pedido 60)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0528167) empresa (01). (Qtde receita: 800, Qtde pedido 40)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (004907) na receita difere da quantidade movimentada nos lotes do pedido (0528707) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0528407) empresa (01). (Qtde receita: 800, Qtde pedido 40)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (003822) na receita difere da quantidade movimentada nos lotes do pedido (0528200) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0528428) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0528431) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (003310) na receita difere da quantidade movimentada nos lotes do pedido (0528219) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (004907) na receita difere da quantidade movimentada nos lotes do pedido (0528786) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (007436) na receita difere da quantidade movimentada nos lotes do pedido (0529126) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005875) na receita difere da quantidade movimentada nos lotes do pedido (0528476) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (007174) na receita difere da quantidade movimentada nos lotes do pedido (0528238) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (004907) na receita difere da quantidade movimentada nos lotes do pedido (0528807) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0528262) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0528488) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0528489) empresa (01). (Qtde receita: 800, Qtde pedido 40)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0528583) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0528293) empresa (01). (Qtde receita: 2000, Qtde pedido 100)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0528852) empresa (01). (Qtde receita: 800, Qtde pedido 40)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (007124) na receita difere da quantidade movimentada nos lotes do pedido (0528637) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (003822) na receita difere da quantidade movimentada nos lotes do pedido (0528860) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0528651) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (006353) na receita difere da quantidade movimentada nos lotes do pedido (0528652) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0528665) empresa (01). (Qtde receita: 800, Qtde pedido 40)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (003822) na receita difere da quantidade movimentada nos lotes do pedido (0528673) empresa (01). (Qtde receita: 800, Qtde pedido 40)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0528693) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (006353) na receita difere da quantidade movimentada nos lotes do pedido (0522824) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0529147) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (004907) na receita difere da quantidade movimentada nos lotes do pedido (0528878) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (006705) na receita difere da quantidade movimentada nos lotes do pedido (0528880) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0529329) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (003822) na receita difere da quantidade movimentada nos lotes do pedido (0529708) empresa (01). (Qtde receita: 6000, Qtde pedido 300)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0529155) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (006353) na receita difere da quantidade movimentada nos lotes do pedido (0529161) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0528956) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0529549) empresa (01). (Qtde receita: 800, Qtde pedido 40)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (004901) na receita difere da quantidade movimentada nos lotes do pedido (0528991) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0529001) empresa (01). (Qtde receita: 800, Qtde pedido 40)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0529185) empresa (01). (Qtde receita: 1600, Qtde pedido 80)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0529007) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0529388) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0529010) empresa (01). (Qtde receita: 1600, Qtde pedido 80)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (003310) na receita difere da quantidade movimentada nos lotes do pedido (0529019) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (007174) na receita difere da quantidade movimentada nos lotes do pedido (0529026) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (004907) na receita difere da quantidade movimentada nos lotes do pedido (0529199) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0529033) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (004907) na receita difere da quantidade movimentada nos lotes do pedido (0529050) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (006705) na receita difere da quantidade movimentada nos lotes do pedido (0529233) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (004907) na receita difere da quantidade movimentada nos lotes do pedido (0529058) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (004907) na receita difere da quantidade movimentada nos lotes do pedido (0529081) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0529236) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005875) na receita difere da quantidade movimentada nos lotes do pedido (0529093) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0529113) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0529509) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (007436) na receita difere da quantidade movimentada nos lotes do pedido (0529254) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0529267) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0529559) empresa (01). (Qtde receita: 800, Qtde pedido 40)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (007177) na receita difere da quantidade movimentada nos lotes do pedido (0529730) empresa (01). (Qtde receita: 800, Qtde pedido 40)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (004901) na receita difere da quantidade movimentada nos lotes do pedido (0529792) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0529870) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0530145) empresa (01). (Qtde receita: 800, Qtde pedido 40)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (003822) na receita difere da quantidade movimentada nos lotes do pedido (0529891) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0529854) empresa (01). (Qtde receita: 2400, Qtde pedido 120)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0529629) empresa (01). (Qtde receita: 1200, Qtde pedido 60)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005875) na receita difere da quantidade movimentada nos lotes do pedido (0529948) empresa (01). (Qtde receita: 150, Qtde pedido 30)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (004907) na receita difere da quantidade movimentada nos lotes do pedido (0529661) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (004907) na receita difere da quantidade movimentada nos lotes do pedido (0530606) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (007177) na receita difere da quantidade movimentada nos lotes do pedido (0529962) empresa (01). (Qtde receita: 1200, Qtde pedido 60)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (007174) na receita difere da quantidade movimentada nos lotes do pedido (0529670) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (007331) na receita difere da quantidade movimentada nos lotes do pedido (0530189) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (004907) na receita difere da quantidade movimentada nos lotes do pedido (0529964) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (004907) na receita difere da quantidade movimentada nos lotes do pedido (0529690) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0530311) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (003822) na receita difere da quantidade movimentada nos lotes do pedido (0530219) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (006353) na receita difere da quantidade movimentada nos lotes do pedido (0530610) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (003822) na receita difere da quantidade movimentada nos lotes do pedido (0530019) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (003310) na receita difere da quantidade movimentada nos lotes do pedido (0530436) empresa (01). (Qtde receita: 50, Qtde pedido 10)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (006634) na receita difere da quantidade movimentada nos lotes do pedido (0530358) empresa (01). (Qtde receita: 200, Qtde pedido 40)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0530375) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0530467) empresa (01). (Qtde receita: 2000, Qtde pedido 100)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0530566) empresa (01). (Qtde receita: 1600, Qtde pedido 80)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (006353) na receita difere da quantidade movimentada nos lotes do pedido (0530639) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (004907) na receita difere da quantidade movimentada nos lotes do pedido (0530584) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (003903) na receita difere da quantidade movimentada nos lotes do pedido (0530793) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0530689) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (006353) na receita difere da quantidade movimentada nos lotes do pedido (0531011) empresa (01). (Qtde receita: 75, Qtde pedido 15)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (006705) na receita difere da quantidade movimentada nos lotes do pedido (0531160) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0530597) empresa (01). (Qtde receita: 800, Qtde pedido 40)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0530698) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (007177) na receita difere da quantidade movimentada nos lotes do pedido (0530601) empresa (01). (Qtde receita: 1200, Qtde pedido 60)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (004907) na receita difere da quantidade movimentada nos lotes do pedido (0530719) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (007174) na receita difere da quantidade movimentada nos lotes do pedido (0530812) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0531031) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (007436) na receita difere da quantidade movimentada nos lotes do pedido (0531035) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0530818) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (006353) na receita difere da quantidade movimentada nos lotes do pedido (0530819) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (007436) na receita difere da quantidade movimentada nos lotes do pedido (0531183) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (004901) na receita difere da quantidade movimentada nos lotes do pedido (0530831) empresa (01). (Qtde receita: 50, Qtde pedido 10)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (004907) na receita difere da quantidade movimentada nos lotes do pedido (0531041) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0530836) empresa (01). (Qtde receita: 800, Qtde pedido 40)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0531187) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0530893) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005875) na receita difere da quantidade movimentada nos lotes do pedido (0530927) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (007174) na receita difere da quantidade movimentada nos lotes do pedido (0531098) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0530941) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (007436) na receita difere da quantidade movimentada nos lotes do pedido (0531100) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005875) na receita difere da quantidade movimentada nos lotes do pedido (0530954) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (006353) na receita difere da quantidade movimentada nos lotes do pedido (0531188) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (003822) na receita difere da quantidade movimentada nos lotes do pedido (0531469) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005875) na receita difere da quantidade movimentada nos lotes do pedido (0531216) empresa (01). (Qtde receita: 50, Qtde pedido 10)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0531348) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (007174) na receita difere da quantidade movimentada nos lotes do pedido (0531490) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (004907) na receita difere da quantidade movimentada nos lotes do pedido (0531360) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0531385) empresa (01). (Qtde receita: 800, Qtde pedido 40)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (007436) na receita difere da quantidade movimentada nos lotes do pedido (0531509) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (007177) na receita difere da quantidade movimentada nos lotes do pedido (0531404) empresa (01). (Qtde receita: 1200, Qtde pedido 60)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (004907) na receita difere da quantidade movimentada nos lotes do pedido (0531545) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0531416) empresa (01). (Qtde receita: 1600, Qtde pedido 80)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0531442) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0531592) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (004907) na receita difere da quantidade movimentada nos lotes do pedido (0531459) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (007436) na receita difere da quantidade movimentada nos lotes do pedido (0531610) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (003822) na receita difere da quantidade movimentada nos lotes do pedido (0532014) empresa (01). (Qtde receita: 6000, Qtde pedido 300)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (003822) na receita difere da quantidade movimentada nos lotes do pedido (0532239) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0531622) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0532063) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (006353) na receita difere da quantidade movimentada nos lotes do pedido (0531981) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0532246) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0532099) empresa (01). (Qtde receita: 800, Qtde pedido 40)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (007436) na receita difere da quantidade movimentada nos lotes do pedido (0532109) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0532149) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0532183) empresa (01). (Qtde receita: 800, Qtde pedido 40)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0532187) empresa (01). (Qtde receita: 14400, Qtde pedido 720)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0532218) empresa (01). (Qtde receita: 800, Qtde pedido 40)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (006353) na receita difere da quantidade movimentada nos lotes do pedido (0532265) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (004907) na receita difere da quantidade movimentada nos lotes do pedido (0532469) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (006353) na receita difere da quantidade movimentada nos lotes do pedido (0532311) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (004907) na receita difere da quantidade movimentada nos lotes do pedido (0532331) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0533052) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (006353) na receita difere da quantidade movimentada nos lotes do pedido (0532365) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0532507) empresa (01). (Qtde receita: 800, Qtde pedido 40)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (006353) na receita difere da quantidade movimentada nos lotes do pedido (0532508) empresa (01). (Qtde receita: 50, Qtde pedido 10)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (006353) na receita difere da quantidade movimentada nos lotes do pedido (0532729) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (006705) na receita difere da quantidade movimentada nos lotes do pedido (0523976) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0564382) empresa (01). (Qtde receita: 400, Qtde pedido 20)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (007537) na receita difere da quantidade movimentada nos lotes do pedido (0564406) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (007552) na receita difere da quantidade movimentada nos lotes do pedido (0564425) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (007174) na receita difere da quantidade movimentada nos lotes do pedido (0564429) empresa (01). (Qtde receita: 25, Qtde pedido 5)');
INSERT INTO TAGRINDEATAREFASPENDENTES (MOTIVO)
                               VALUES ('A quantidade do produto (005609) na receita difere da quantidade movimentada nos lotes do pedido (0564432) empresa (01). (Qtde receita: 400, Qtde pedido 20)');

COMMIT WORK;
"""
numero_sete_digitos = extrair_numero_sete_digitos(texto_exemplo)

if numero_sete_digitos:
    print(f"Número de 7 dígitos encontrado: {numero_sete_digitos}")
else:
    print("Nenhum número de 7 dígitos encontrado.")