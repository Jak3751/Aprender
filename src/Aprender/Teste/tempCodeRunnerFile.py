from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


texto = "C.V PANUCCI CONFECCOES" 
listaURLs = [
"http://www.sefaz.mt.gov.br/nfce/consultanfce?p=51231234785310000180650010000001891858794600|2|1|1|957fa2258ba7a4b90dc63ed1db67120539be462a",
"http://www.sefaz.mt.gov.br/nfce/consultanfce?p=51231234785310000180650010000001901314036701|2|1|1|9946c4f44b36248441cf1a66c20c575dc4d072f3",
"http://www.sefaz.mt.gov.br/nfce/consultanfce?p=51231234785310000180650010000001911135251583|2|1|1|19b10af0ac970e14ba2f00594de2810295e3785a",
"http://www.sefaz.mt.gov.br/nfce/consultanfce?p=51231234785310000180650010000001921747843993|2|1|1|5dcef8952c317468cb387d07d5a3012fcf2b4b1a",
"http://www.sefaz.mt.gov.br/nfce/consultanfce?p=51231234785310000180650010000002051467639504|2|1|1|d91ef11c2f4b5b54570a1ebddfd8b01d81d00f5c",
"http://www.sefaz.mt.gov.br/nfce/consultanfce?p=51231234785310000180650010000001931752581982|2|1|1|0ce8eadeced03c9818f796d683582df8d8ac129e",
"http://www.sefaz.mt.gov.br/nfce/consultanfce?p=51231234785310000180650010000001941165316995|2|1|1|86c27597857b3ff6402a34308782fec233148882",
"http://www.sefaz.mt.gov.br/nfce/consultanfce?p=51231234785310000180650010000001951272397406|2|1|1|f5fdf9eee8a8e01adda431b2038583cabfbe9019",
"http://www.sefaz.mt.gov.br/nfce/consultanfce?p=51231234785310000180650010000001961278329477|2|1|1|eb687e82595020c0e2f5dfdeccc489d2ef25af4f",
"http://www.sefaz.mt.gov.br/nfce/consultanfce?p=51231234785310000180650010000001971852705330|2|1|1|2c500faed96664e3098386e4b1f5d55bfafbe465"
]

driver = webdriver.Firefox()
for url in listaURLs:
   driver.get(url)  
   paginaInfo = driver.page_source 
   if(texto in paginaInfo):
      print(url + " Nota existe")
   else:
      print(url + " Nota não existe") 

driver.quit()