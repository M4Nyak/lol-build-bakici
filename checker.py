import requests
from bs4 import BeautifulSoup
import re
from colorama import init
from termcolor import colored
def itemleri_cek(dom):
 f= requests.get(f"https://www.mobafire.com"+dom).content
 soup= BeautifulSoup(f,"html.parser")
 uzunluk = len(soup.find_all("img",{'height':'64'}))
 for i in range(uzunluk):
  kuk=soup.find_all("img",{'height':'64'})[i]['data-original']
  kuk= re.split("/",kuk)
  print(colored(kuk[3].replace('-64x.png',''),"light_yellow"))
while True:
 init()
 print(colored("eger karakterin adi boslukluysa bosluk kullanmadan yaz ornek: kogmaw, reksai",'red'))
 karakter= str(input(colored('buildi bakilacak karakterin ismi: ','light_blue')))
 a= requests.get(f"https://www.mobafire.com/league-of-legends/champion/{karakter}").content
 soup= BeautifulSoup(a,"html.parser")
 b= soup.find_all("a",{'class': 'mf-listings__item player-diamond'})[0]
 domain= str(re.findall("href=\S+",str(b))[0]).strip('href=">')
 itemleri_cek(domain)
